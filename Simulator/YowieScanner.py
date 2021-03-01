
# Yowie Tool Scanner Simulator
# Adrian Bowyer
# 19 November 2020

import copy, sys
import math as maths

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Useful general functions and numbers
# -----------------------------------------------

# Length in mm considered to be 0 and its square

veryShort = 0.001
veryShort2 = veryShort*veryShort

# Roughly the largest dimension in mm of anything that will be dealt with

veryLong = 6000

# The standard deviation width of a light stripe on a surface in mm

lightSD = 0.05
gaussDivide = 1.0/(lightSD*maths.sqrt(2.0*maths.pi))

# Unique count as a string

objectCount = -1

def UniqueNumber():
 global objectCount
 objectCount += 1
 return str(objectCount)

# The intensity of the light sheet at distance d from where its centre hits a surface

def GaussianLightIntensity(d):
 e = d/lightSD
 return maths.exp(-0.5*(e*e))*gaussDivide

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Small classes for working with 2D vectors
# -----------------------------------------------------

# Each point optionally stores the face of the FreeCAD model in which it lies.

class Point2D:
 def __init__(self, x = 0, y = 0, f = None):
  self.x = x
  self.y = y
  self.face = f

 def __repr__(self):
  return "(Point2D x:%s y:%s)" % (self.x, self.y)

 # Vector addition and subtraction

 def Add(self, p):
  return Point2D(self.x + p.x, self.y + p.y)

 def Sub(self, p):
  return Point2D(self.x - p.x, self.y - p.y)

 # Inner product

 def Dot(self, p):
  return self.x*p.x + self.y*p.y

 # Squared magnitude

 def Length2(self):
  return self.Dot(self)

 # Multiplication by a scalar

 def Multiply(self, m):
  return Point2D(self.x*m, self.y*m)

 # Outer product

 def Cross(self, p):
  return self.x*p.y - self.y*p.x

# Set or change the associated face

 def SetFace(self, f):
  self.face = f

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Small class for working with 2D parametric lines
# --------------------------------------------------------------


# Lines are defined by a start and end point.  The parameterisation
# is such that the start point has parameter = 0, and the end parameter = 1.

class Line2D:
 def __init__(self, p0 = Point2D(0, 0), p1 = Point2D(0, 0), f = None):
  self.p0 = p0
  self.direction = p1.Sub(p0)
  self.face = f
  self.empty = self.Length2() < veryShort2

 def __repr__(self):
  return "<Line2D p0:%s direction:%s>" % (self.p0, self.direction)

# The point at parameter value t

 def Point(self, t):
  p = self.direction.Multiply(t)
  return self.p0.Add(p)

 # Find the parameter value at which another line crosses me (s) and I cross it (t)

 def Cross(self, otherLine):
  determinant = otherLine.direction.Cross(self.direction)
  if abs(determinant) < veryShort2:
   return None, None # Lines parallel
  dp = otherLine.p0.Sub(self.p0)
  s = otherLine.direction.Cross(dp)/determinant
  t = self.direction.Cross(dp)/determinant
  return s, t

 # Are two lines the same (within tolerance)?

 def IsSameLine(self, otherLine):
  determinant = otherLine.direction.Cross(self.direction)
  if abs(determinant) > veryShort2:
   return False
  if self.p0.Sub(otherLine.p0).Length2() > veryShort2:
   return False
  return True

 # Squared length

 def Length2(self):
  return self.direction.Length2()

#----------------------------------------------------------------------------------------------------------------------------

# The simulator needs its own 3D vector algebra and rotation matrix classes so it can stand alone independently of FreeCad

class Vector3:
 def __init__(self, x = 0, y = 0, z = 0):
  self.x = x
  self.y = y
  self.z = z

 def Multiply(self, a):
  return Vector3(self.x*a, self.y*a, self.z*a)

 def Add(self, v):
  return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

 def Sub(self, v):
  return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

 def Dot(self, v):
  return self.x*v.x + self.y*v.y + self.z*v.z

 def Cross(self, v):
  return Vector3(
   self.y*v.z - self.z*v.y, 
   -self.x*v.z + self.z*v.x, 
   self.x*v.y - self.y*v.x
   )

 def Length2(self):
  return self.Dot(self)

 def Normalize(self):
  d = self.Length2()
  if d <= 0.0:
   print("Attempt to normalize zero-length vector")
  return self.Multiply(1.0/maths.sqrt(d))

 def __repr__(self):
  return 'Vector3(' + str(self.x) + ', ' +  str(self.y) + ', ' +  str(self.z) + ')' 

#---

class RotationM:

# Rotation from axis vector and angle (see https://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle)
# Note we need minus the angle as the Wikipedia entry is using left-handed coordinates (dunno why).

 def __init__(self, vec, ang):
  v = vec.Normalize()
  c = maths.cos(-ang)
  c1 = 1.0 - c
  s = maths.sin(-ang)
  x = v.x
  y = v.y
  z = v.z
  self.r = ( 
   [x*x*c1 + c, x*y*c1 - z*s, x*z*c1 + y*s],
   [y*x*c1 + z*s, y*y*c1 + c, y*z*c1 - x*s],
   [z*x*c1 - y*s, z*y*c1 + x*s, z*z*c1 + c]
  )

# Rotate a vector

 def MultVec(self, v):
  return Vector3(
   self.r[0][0]*v.x + self.r[1][0]*v.y + self.r[2][0]*v.z,
   self.r[0][1]*v.x + self.r[1][1]*v.y + self.r[2][1]*v.z,
   self.r[0][2]*v.x + self.r[1][2]*v.y + self.r[2][2]*v.z
  )

# Product of two matrices

 def Multiply(self, rot):
  result = RotationM(Vector3(0,0,1), 0)
  for i in range(3):
   for j in range(3):
    s = 0.0
    for k in range(3):
     s += self.r[i][k]*rot.r[k][j]
    result.r[i][j] = s
  return result

 def __repr__(self):
  result = 'RotationM('
  for i in range(3):
   if i is not 0:
    result += ',('
   else:
    result += '('
   for j in range(3):
    result += '%.6f' %self.r[i][j]
    if j is not 2:
     result += ','
    else:
     result += ')'
  result += ')'
  return result

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The main simulator class - this represents a part of the scanner.  The parts are arranged in a tree.
#
# offset is the vector in the parent's space that gives our position in that space. If there is no parent the offset is in World coordinates.
# u, v, and w are three orthogonal vectors that define our coordinate system
# parent is the ScannerPart above us in the tree (if any)
# lightAngle is the width of the beam in radians if we are a sheet light source; negative if we aren't
# uPixels, vPixels are the image plane pixel counts if we are a camera
# uMM, vMM are the distance between one pixel and the next if we are a camera
# focalLength is our focal length if we are a camera, negative if we aren't
#

class ScannerPart:
 def __init__(self, offset = Vector3(0, 0, 0), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = None,\
  lightAngle = -1, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1):

  # Offset from the parent in the parent's coordinate system
  # If the parent is None these are absolute cartesian coordinates

  self.offset = offset

  # Local Cartesian coordinates
 
  self.u = u.Normalize()
  self.v = v.Normalize()
  self.w = w.Normalize()

  # If we are a light source (i.e. lightAngle >= 0) check we're not projecting backwards

  if lightAngle > maths.pi:
   print("Light source with angle > pi: ", lightAngle)

  self.lightAngle = lightAngle

  # If we are a camera (i.e. focalLength >= 0)

  self.uPixels = uPixels
  self.vPixels = vPixels
  self.uMM = uMM
  self.vMM = vMM
  self.focalLength = focalLength

  # Orientation - start with the identity matrix

  self.orientation = RotationM(Vector3(0,0,1), 0)

  # Parent and children in the tree

  self.parent = parent
  self.children = []
  if parent is not None:
   parent.children.append(self)

  # Used for lazy evaluation of position

  self.notMoved = False
  self.position = Vector3(0, 0, 0)

#-----------------

# Compute my absolute offset from the origin recursively
# Use lazy evaluation if I haven't moved.

 def AbsoluteOffset(self):
  if self.notMoved:
   return self.position

  if self.parent is None:
   self.position = self.offset
  else:
   parentUO = self.parent.u.Multiply(self.offset.x)
   parentVO = self.parent.v.Multiply(self.offset.y)
   parentWO = self.parent.w.Multiply(self.offset.z)
   o = parentUO.Add(parentVO.Add(parentWO))
   self.position = o.Add(self.parent.AbsoluteOffset())
  self.notMoved = True
  return self.position

# Rotate my coordinates, and the coordinates of all my descendents recursively

 def Rotate(self, r):
  self.notMoved = False
  self.u = r.MultVec(self.u).Normalize()
  self.v = r.MultVec(self.v).Normalize()
  self.w = r.MultVec(self.w).Normalize()
  self.orientation = r.Multiply(self.orientation)
  for child in self.children:
   child.Rotate(r)

# Rotate about the u axis. angle is in radians

 def RotateU(self, angle):
  self.notMoved = False
  r = RotationM(self.u, angle)
  self.Rotate(r)

# Rotate about the v axis. angle is in radians

 def RotateV(self, angle):
  self.notMoved = False
  r = RotationM(self.v, angle)
  self.Rotate(r)

# Rotate about the w axis. angle is in radians

 def RotateW(self, angle):
  self.notMoved = False
  r = RotationM(self.w, angle)
  self.Rotate(r)

# Create the ray from a pixel in mm in a camera's [u, v] plane through the centre of the lens.

 def GetCameraRay(self, pixelU, pixelV):
  if self.focalLength <= 0:
   print("Attempt to get a pixel ray from a scanner part that is not a camera.")
  u = self.u.Multiply(pixelU)
  v = self.v.Multiply(pixelV)
  pixel = self.AbsoluteOffset().Add(u).Add(v)  
  w = self.w.Multiply(self.focalLength)
  lens = self.AbsoluteOffset().Add(w)
  return (pixel, lens)

# As above, but so that parameter values along the ray measure real distance

 def GetCameraRayNormalised(self, pixelU, pixelV):
  ray = self.GetCameraRay(pixelU, pixelV)
  direction = ray[1].Sub(ray[0])
  direction = direction.Normalize()
  newRay = (ray[0], ray[0].Add(direction))
  return newRay

# Find the pixel (u, v) in the camera's image plane that the point p projects into

 def ProjectPointIntoCameraPixel(self, p):
  w = self.w.Multiply(self.focalLength)
  pRelativeInv = self.focalLength/p.Sub(self.AbsoluteOffset().Add(w)).Dot(self.w)
  pd = self.AbsoluteOffset().Sub(p)
  u = pd.Dot(self.u)*pRelativeInv
  v = pd.Dot(self.v)*pRelativeInv
  u = int(round((u + 0.5*self.uMM)*(self.uPixels - 1)/self.uMM))
  v = int(round((v + 0.5*self.vMM)*(self.vPixels - 1)/self.vMM))
  return (u, v)

# Find the implicit plane equation of the light sheet, returned as the normal vector and the origin offset constant

 def GetLightPlane(self):
  if self.lightAngle <= 0:
   print("Attempt to get a light plane from a scanner part that is not a light source.")
  uu = copy.deepcopy(self.u)
  pointInPlane = self.AbsoluteOffset()
  offset = -uu.Dot(pointInPlane)
  return (uu, offset)

# Find the point in space where the ray from a camera pixel (mm coordinates) hits the light sheet from this light source

 def CameraPixelIsPointInMyPlane(self, camera, pixelU, pixelV):
  plane = self.GetLightPlane()
  normal = plane[0]
  d = plane[1]
  ray = camera.GetCameraRay(pixelU, pixelV)
  t0Point = ray[0]
  rayDirection = ray[1].Sub(ray[0])
  sp = rayDirection.Dot(normal)
  if abs(sp) < veryShort2:
   print("Ray is parallel to plane.")
   return Vector3(0, 0, 0)
  t = -d/sp
  tPoint = rayDirection.Multiply(t).Add(t0Point)
  return tPoint

# Find the point in space where the ray from a camera pixel (pixel indices) hits the light sheet from this light source

 def CameraPixelIndicesArePointInMyPlane(self, camera, pixelUIndex, pixelVIndex):
  pixelU = camera.uMM*(pixelUIndex/(camera.uPixels - 1.0) - 0.5)
  pixelV = camera.vMM*(pixelVIndex/(camera.vPixels - 1.0) - 0.5)
  return self.CameraPixelIsPointInMyPlane(camera, pixelU, pixelV)

# Convert a point p in the [v, w] plane into a point in absolute 3D space.
# The [v, w] plane is the light sheet for a light source.  Remember that
# w is the plane's x axis because w is the centre of the beam.  
# This and the next function are for the light sheet simulation.

 def vwPoint(self, p):
  w = self.w.Multiply(p.x)
  v = self.v.Multiply(p.y)
  return self.AbsoluteOffset().Add(v).Add(w)

# Project a 3D point into the [v, w] plane.  Again w is the x axis.

 def xyPoint(self, p3D):
  p3 = p3D.Sub(self.AbsoluteOffset())
  x = self.w.Dot(p3)
  y = self.v.Dot(p3)
  p = Point2D(x, y)
  return p

# Convert a 2D point p in the [u, v] plane into a point in absolute 3D space.
# The [u, v] plane is the focal plane of a camera, which points along the
# w axis.  The lens (or pinhole) is self.focalLength along w.  

 def uvPoint(self, p):
  u = self.u.Multiply(p.x)
  v = self.v.Multiply(p.y)
  return self.AbsoluteOffset().add(u).add(v)

#-----------------------------------------------------------------------------------------------------------------------------------------

# Short demonstration of how to use this.
# Uncomment it to run it

# Make the scanner

world = ScannerPart()
scanner = ScannerPart(offset = Vector3(0, -1700, 1000), parent = world)
lightSource = ScannerPart(offset = Vector3(0, 0, -250), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = scanner, lightAngle = 2, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1)
camera = ScannerPart(offset = Vector3(0, 0, 250),  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = scanner, lightAngle = -1, uPixels = 2464, vPixels = 3280, uMM =  17.64, vMM = 24.088543586543586, focalLength = 25) 
lightSource.RotateU(-0.5*maths.pi)
lightSource.RotateW(-0.5*maths.pi)
camera.RotateU(-0.5*maths.pi)
#Display(world, showLight = True, showCamera = True)
spacePoint = lightSource.CameraPixelIndicesArePointInMyPlane(camera, 390, 170)
print("Point in space: ", spacePoint)
pix = camera.ProjectPointIntoCameraPixel(spacePoint)
print("Camera pixel: ", pix)

'''
world = ScannerPart()
scanner = ScannerPart(offset = Vector3(38, 12, 10), parent = world)
lightSource = ScannerPart(offset = Vector3(0, 10, 0), parent = scanner, lightAngle = 1)
camera = ScannerPart(offset = Vector3(0, -10, 0), parent = scanner, uPixels = 75, vPixels = 100, uMM = 1.5, vMM = 2, focalLength = 5) 
lightSource.RotateV(-0.5*maths.pi)
lightSource.RotateW(0.5*maths.pi)
lightSource.RotateV(-0.5)
camera.RotateV(-0.5*maths.pi)
camera.RotateU(-0.1)
camera.RotateW(-0.5*maths.pi)

# Find the point in the light sheet corresponding to the pixel indices (3, 17) in the camera

print(lightSource.CameraPixelIndicesArePointInMyPlane(camera, 3, 17))
'''



