
# Yowie Tool Scanner Simulator
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 19 November 2020

import copy, sys
import math as maths
from random import seed, random, gauss

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

# The simulator needs its own 3D vector algebra and rotation matrix classes so it can stand alone independently of FreeCAD

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

 def Del(self, v, divisor):
  d = self.Sub(v)
  return d.Multiply(1.0/divisor)

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

# Uniform random number in [-1, 1]

def Random2():
 return random()*2.0 - 1.0

# Generate a random vector of mean length with standard deviation sd
# by rejection sampling in the unit ball

def RandomVector3(mean, sd):
 s = 2.0
 while s > 1.0:
  x = Random2()
  y = Random2()
  z = Random2()
  s = x*x + y*y + z*z
 v = Vector3(x, y, z).Normalize().Multiply(gauss(mean, sd))
 return v

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
   if i != 0:
    result += ',('
   else:
    result += '('
   for j in range(3):
    result += '%.6f' %self.r[i][j]
    if j != 2:
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
  lightAngle = -1, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1, name = ""):

  self.name = name

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

  # Flag for reporting what's going on

  self.debug = False

#-----------------

# Set my name down through my children recursively

 def SetName(self, name):
  self.name = name
  for child in self.children:
   child.SetName(name)

# Turn debugging on and off for me and all my children recursively

 def DebugOn(self):
  self.debug = True
  for child in self.children:
   child.DebugOn()

 def DebugOff(self):
  self.debug = False
  for child in self.children:
   child.DebugOff()

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

# Rotate my coordinates, and the coordinates of all my descendants recursively

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

 def GetCameraRay(self, pixel):
  if self.focalLength <= 0:
   print("Attempt to get a pixel ray from a scanner part that is not a camera.")
  u = self.u.Multiply(pixel[0])
  v = self.v.Multiply(pixel[1])
  newPixel = self.AbsoluteOffset().Add(u).Add(v)
  w = self.w.Multiply(self.focalLength)
  lens = self.AbsoluteOffset().Add(w)
  ray = (newPixel, lens)
  return ray

# As above, but so that parameter values along the ray measure real distance

 def GetCameraRayNormalised(self, pixel):
  ray = self.GetCameraRay(pixel)
  direction = ray[1].Sub(ray[0])
  direction = direction.Normalize()
  newRay = (ray[0], ray[0].Add(direction))
  return newRay

# Find the pixel coordinates point in the image plane (not necessarily an exact pixel) that point p projects into

 def ProjectPointIntoCameraPlane(self, p):
  if self.focalLength <= 0.0:
   print("Attempt to get a pixel from a scanner part that is not a camera.")
  w = self.w.Multiply(self.focalLength)
  pRelativeInv = self.focalLength/p.Sub(self.AbsoluteOffset().Add(w)).Dot(self.w)
  pd = self.AbsoluteOffset().Sub(p)
  u = pd.Dot(self.u)*pRelativeInv
  v = pd.Dot(self.v)*pRelativeInv
  uu = (u + 0.5*self.uMM)*(self.uPixels - 1)/self.uMM
  vv = (v + 0.5*self.vMM)*(self.vPixels - 1)/self.vMM
  pixel = (uu, vv)
  if self.debug:
   print(self.name, " - Point ", p, " projects to pixel ", pixel, "(mm: ", u, ", ", v, ")")
  return pixel

# Find the integer pixel (u, v) in the camera's image plane nearest where the point p projects into

 def ProjectPointIntoCameraPixel(self, p):
  uv = self.ProjectPointIntoCameraPlane(p)
  u = int(round(uv[0]))
  v = int(round(uv[1]))
  return (u, v)

# Find the implicit plane equation of the light sheet, returned as the normal vector and the origin offset constant

 def GetLightPlane(self):
  if self.lightAngle <= 0:
   print("Attempt to get a light plane from a scanner part that is not a light source.")
  uu = copy.deepcopy(self.u)
  pointInPlane = self.AbsoluteOffset()
  offset = -uu.Dot(pointInPlane)
  plane = (uu, offset)
  return plane

# Find the point in space where the ray from a camera pixel (mm coordinates) hits the light sheet from this light source

 def CameraPixelIsPointInMyPlane(self, camera, pixel):
  plane = self.GetLightPlane()
  normal = plane[0]
  d = plane[1]
  ray = camera.GetCameraRay(pixel)
  t0Point = ray[0]
  rayDirection = ray[1].Sub(t0Point)
  sp = rayDirection.Dot(normal)
  if abs(sp) < veryShort2:
   print("Ray is parallel to plane.")
   return Vector3(0, 0, 0)
  inPlane = -(normal.Dot(t0Point) + d)
  t = inPlane/sp
  tPoint = rayDirection.Multiply(t).Add(t0Point)
  if self.debug:
   print("] makes a ray ", ray, " that \n         hits the light plane ", plane, " at: ", tPoint)
  return tPoint

# Find the point in space where the ray from a camera pixel (pixel coordinates; not necessarily integers) hits the light sheet from this light source

 def CameraPixelCoordinatesArePointInMyPlane(self, camera, pixelCoordinates):
  pixelU = camera.uMM*(pixelCoordinates[0]/(camera.uPixels - 1.0) - 0.5)
  pixelV = camera.vMM*(pixelCoordinates[1]/(camera.vPixels - 1.0) - 0.5)
  pixel = (pixelU, pixelV)
  if self.debug:
   print(self.name, "Pixel [", pixelCoordinates[0], ", ", pixelCoordinates[1], end = '')
  tPoint = self.CameraPixelIsPointInMyPlane(camera, pixel)
  return tPoint

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

# Small class to hold the parameters needed to build a complete scanner
# Make a scanner in the standard configuration. The parameters are also recorded in a vector for optimisation.

class Scanner:
 def __init__(self, world, scannerOffset, lightOffset, lightAng, cameraOffset, uPix, vPix, uM, vM, focalLen):
  self.parameters = []

  self.scannerOffset = scannerOffset
  self.parameters.append(scannerOffset.x)
  self.parameters.append(scannerOffset.y)
  self.parameters.append(scannerOffset.z)

  self.lightOffset = lightOffset
  self.parameters.append(lightOffset.x)
  self.parameters.append(lightOffset.y)
  self.parameters.append(lightOffset.z)

  self.cameraOffset = cameraOffset
  self.parameters.append(cameraOffset.x)
  self.parameters.append(cameraOffset.y)
  self.parameters.append(cameraOffset.z)

  self.focalLen = focalLen
  self.parameters.append(focalLen)

  self.lightAng = lightAng
  self.scanner = ScannerPart(offset = self.scannerOffset, parent = world)
  self.lightSource = ScannerPart(offset = self.lightOffset, u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = self.scanner, lightAngle = self.lightAng)
  self.camera = ScannerPart(offset = self.cameraOffset,  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = self.scanner, uPixels = uPix, vPixels = vPix, uMM =  uM, vMM = vM, focalLength = self.focalLen)

  lru = -0.5*maths.pi
  self.parameters.append(lru)
  self.lightSource.RotateU(lru)

  lrw = -0.5*maths.pi
  self.parameters.append(lrw)
  self.lightSource.RotateW(lrw)

  cru = -0.5*maths.pi
  self.parameters.append(cru)
  self.camera.RotateU(cru)

 def SetName(self, name):
  self.scanner.SetName(name)

 def DebugOn(self):
  self.scanner.DebugOn()

 def DebugOff(self):
  self.scanner.DebugOff()

# Make a deep copy of a scanner

 def Copy(self):
  return Scanner(self.scanner.parent, self.scannerOffset, self.lightOffset, self.lightAng, self.cameraOffset, self.camera.uPixels, self.camera.vPixels, self.camera.uMM, self.camera.vMM, self.camera.focalLength)

# Make a copy of a scanner perturbed by small Gaussian amounts with mean and sd standard deviation.

 def PerturbedCopy(self, mean, sd):
  if mean < veryShort2:
   return self.Copy()
  return Scanner(self.scanner.parent, self.scannerOffset.Add(RandomVector3(mean, sd)), self.lightOffset.Add(RandomVector3(mean, sd)), self.lightAng, self.cameraOffset.Add(RandomVector3(mean, sd)),
                 self.camera.uPixels, self.camera.vPixels, self.camera.uMM, self.camera.vMM, self.camera.focalLength + gauss(0.0, sd))


# Take an existing scanner and modify it according to the given parameter vector, assumed to be derived from some optimisation process

 def ImposeParameters(self, parameters):
  self.parameters = copy.deepcopy(parameters)
  self.scannerOffset = Vector3(parameters[0], parameters[1], parameters[2])
  self.lightOffset = Vector3(parameters[3], parameters[4], parameters[5])
  self.cameraOffset = Vector3(parameters[6], parameters[7], parameters[8])
  self.focalLen = parameters[9]
  world = self.scanner.parent
  self.scanner = ScannerPart(offset = self.scannerOffset, parent = world)
  self.lightSource = ScannerPart(offset = self.lightOffset, u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = self.scanner, lightAngle = self.lightAng)
  self.camera = ScannerPart(offset = self.cameraOffset,  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = self.scanner, uPixels = self.camera.uPixels, vPixels = self.camera.vPixels,
                            uMM =  self.camera.uMM, vMM = self.camera.vMM, focalLength = self.focalLen)
  self.lightSource.RotateU(parameters[10])
  self.lightSource.RotateW(parameters[11])
  self.camera.RotateU(parameters[12])

# How different are two scanners?

 def ParameterRMSDifference(self, scanner):
  sum = 0.0
  n = len(self.parameters)
  for p in range(n):
   d = self.parameters[p] - scanner.parameters[p]
   sum += d*d
  return maths.sqrt(sum/n)
