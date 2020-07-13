# Beech Design Scanner Simulation
# Adrian Bowyer
# 19 February 2020

import Part, BOPTools, FreeCAD, math, copy, sys
from FreeCAD import Base
import PySide
from PySide import QtGui, QtCore
from PIL import Image, ImageDraw, ImageFilter

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Useful general functions and numbers
# -----------------------------------------------

# When True, output useful diagnostic information

debug = True

# Length in mm considered to be 0 and its square

veryShort = 0.001
veryShort2 = veryShort*veryShort

# Roughly the largest dimension in mm of anything that will be dealt with

veryLong = 80

# The standard deviation width of a light stripe on a surface in mm

lightSD = 0.05
gaussDivide = 1.0/(lightSD*math.sqrt(2.0*math.pi))

# Unique count as a string

objectCount = -1

def UniqueNumber():
 global objectCount
 objectCount += 1
 return str(objectCount)

# There must be an easier way to make the FreeCAD null set...

def Null():
 n1 = Part.makeBox(1, 1, 1)
 n2 = Part.makeBox(1, 1, 1)
 n2.translate(Base.Vector(10, 10, 10))
 return(n1.common(n2))


# Make a cylinder between two points of a given radius

def Cylinder(p0, p1, r):
 p2 = p1.sub(p0)
 length = p2.Length
 if length < 0.001:
  return Null()
 c = Part.makeCylinder(r, length, p0, p2, 360)
 return c

# Make a plane cross section of FreeCAD geometry s, and return it as a list of wires
# The plane passes through point p0 and has normal n

def CrossSection(s, p0, n):
 nn = copy.deepcopy(n)
 nn.normalize()
 d = nn.dot(p0)
 wires=[]
 for i in s.slice(nn, d):
  wires.append(i)
 return wires

# Display a FreeCAD shape with a given colour as an RGB tripple like (0.0, 1.0, 0.0)

def DisplayShape(shape, colour):
 obj = FreeCAD.ActiveDocument.addObject("Part::Feature" ,"Shape"+UniqueNumber())
 obj.Shape = shape
 obj.ViewObject.ShapeColor = colour
 obj.ViewObject.LineColor = colour

# Clean out the active document and the text windows

def ClearAll():
 doc = FreeCAD.ActiveDocument
 for obj in doc.Objects:
  doc.removeObject(obj.Name)
 mw=Gui.getMainWindow()
 c=mw.findChild(QtGui.QPlainTextEdit, "Python console")
 c.clear()
 r=mw.findChild(QtGui.QTextEdit, "Report view")
 r.clear()

# The intensity of the light sheet at distance d from where its centre hits a surface

def GaussianLightIntensity(d):
 e = d/lightSD
 return math.exp(-0.5*(e*e))*gaussDivide

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Interface to the graphics library (to allow several to be easily substituted)

# New image x by y pixels

def NewImage(x, y):
 return Image.new("L", (x, y))

# The drawable frame of an image

def Draw(picture):
 return ImageDraw.Draw(picture)

# Draw a straight line from p0 to p1

def DrawLine(picture, p0, p1, shade):
 picture.line([p0, p1], shade, 1)

# Set a single pixel to colour shade

def SetPixel(picture, x, y, shade):
 picture.putpixel((x, y), shade)

# Grow the image by width f

def Filter(picture, f):
 return picture.filter(ImageFilter.MaxFilter(f))

# Save the image in a file

def SavePicture(picture, fileName):
 picture.save(fileName)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Small classes for working with 2D vectors
# -----------------------------------------------------

class Point2D:
 def __init__(self, x = 0, y = 0, f = None):
  self.x = x
  self.y = y
  self.face = f

 def __repr__(self):
  return "<Point2D x:%s y:%s>" % (self.x, self.y)

 def Print(self):
  print(self.x, ',' , self.y)

 # Vector addition and subtraction

 def Add(self, p):
  result = copy.deepcopy(self)
  result.x = result.x + p.x
  result.y = result.y + p.y
  return result

 def Sub(self, p):
  result = copy.deepcopy(self)
  result.x = result.x - p.x
  result.y = result.y - p.y
  return result

 # Squared magnitude

 def Length2(self):
  return self.x*self.x + self.y*self.y

 # Multiplication by a scalar

 def Multiply(self, m):
  result = copy.deepcopy(self)
  result.x = result.x*m
  result.y = result.y*m
  return result  

 # Inner product

 def Dot(self, p):
  return self.x*p.x + self.y*p.y

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

 # Fine the parameter value at which another line crosses me (s) and I cross it (t)

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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2D functions for dealing with visibility polygons for the light sheet.
# --------------------------------------------------------------------------------------

# The light sheet hits everything to be scanned in a slicing plane.  But not everything
# the slice cuts will be illuminated; some will be in shadow.  This deals with what
# the light source can see, and therefore what it actually illuminates.

# Each line in the section polygon should join to another as the polygon
# is a section through a solid.  Find the other line.

def FindOtherLineAtPoint(p0, line0, lines):
 for line in lines:
  if line is not line0:
   for a in (0, 1):
    pa = line.Point(a).Sub(p0)
    if pa.Length2() < veryShort2:
     return line
 print("FindOtherLineAtPoint - coincident line end not found!")
 return line0

# A ray through a polygon vertex can go into solid, or it can
# just kiss the vertex and carry on in space. This categorises
# that situation.

def ExtremePoint(p1, ray, lineWithEnds, otherLine, r, lines):
 q = 1 - r
 otherEnd1 = lineWithEnds.Point(q)
 for a in (0, 1):
  pa = otherLine.Point(a).Sub(p1)
  if pa.Length2() < veryShort2:
   b = 1 - a
   otherEnd2 = otherLine.Point(b)
   s0 = ray.direction.Cross(otherEnd1.Sub(ray.p0))
   s1 = ray.direction.Cross(otherEnd2.Sub(ray.p0))
   sign = s0*s1
   if sign <= 0:
    return 0
   return s0
 print("ExtremePoint - other line does not touch original line!")
 return 0


# Find out if p is in a face of the 3D model

def PointIsInAFace(p, faces):
 v = Part.Vertex(p)
 for face in faces:
  if face.distToShape(v)[0] < veryShort:
   return face
 return None

# We have a set of points on the visible polygon in 2D, sorted by angle.
# Add lines between them in 3D that are in actual faces to output, together.
# with their face.  Join contiguous lines that share a face.
# This actually works in 3D, as we need a 3D result.  But all the logic
# is 2D because we know all the points lie in a plane.

def Make3DPolygons(angleTripples, faces, lightSource):

# Make a list of all the 3D points and which faces (if any) the lines
# between them lie in.

 if len(angleTripples) <= 0:
  return

 allPolygons = []
 tripple1 = angleTripples[0] 
 p3D1 = lightSource.vwPoint(tripple1[1])
 allPolygons.append((p3D1, None))
 for i in range(1, len(angleTripples)):
  tripple2 = angleTripples[i] 
  p3D2 = lightSource.vwPoint(tripple2[1])
  halfWayPoint = copy.deepcopy(p3D1)
  halfWayPoint = halfWayPoint.add(p3D2)
  halfWayPoint.multiply(0.5)
  face = PointIsInAFace(halfWayPoint, faces)
  allPolygons.append((p3D2, face))
  p3D1 = p3D2

# Go through and split the list at lines in free space that so have face set to None

  polygon = []
  polygons = []
  pair1 = allPolygons[0]
  polygon.append(pair1)
  for i in range (1, len(allPolygons)):
   pair2 = allPolygons[i]
   if pair2[1] is not None:
     polygon.append(pair2)
   else:
    if len(polygon) >= 2:
     polygons.append(polygon)
    polygon = []
    polygon.append(pair2)
   pair1 = pair2
  if len(polygon) >= 2:
   polygons.append(polygon)

# Now correct the faces of points with faces still set to None

 for polygon in polygons:
  for i in range(1, len(polygon)):
   newPair = (polygon[i-1][0], polygon[i][1])
   polygon[i-1] = newPair

# Now remove points internal to faces, just leaving those at the coreners or ends.

 for k in range(0, len(polygons)):
  polygon = polygons[k]
  newPolygon = []
  newPolygon.append(polygon[0])
  for i in range(1, len(polygon) - 1):
   if polygon[i-1][1] is not polygon[i][1]:
    newPolygon.append(polygon[i])
  newPolygon.append(polygon[len(polygon) - 1])
  polygons[k] = newPolygon

 return polygons

# Plot the 3D polygons (mainly for checking; not actually 2D but 3D...)

def PlotPolygons(polygons):
 if polygons is None:
  return
 if len(polygons) <= 0:
  return
 for polygon in polygons:
  wire = []
  for pair in polygon:
   wire.append(pair[0])
  DisplayShape(Part.makePolygon(wire), (1.0, 0.0, 0.0))

# Find the point on the line from previous to current where a line at angle crosses

def CrossingPoint(previous, current, angle):
 line1 = Line2D(Point2D(0, 0), Point2D(math.cos(angle), math.sin(angle)))
 line2 = Line2D(previous[1], current[1])
 s, t = line2.Cross(line1)
 if s < 0 or s > 1:
  print("CrossingPoint - parameter not in [0, 1]: ", s)
 return (previous[0], line2.Point(s), True)

# We have the visibility polygon, but it is in random order. Sort the points
# by swept angle from the origin (which is where the light is). Also
# categorise the points as being inside or outside the light sheet angle.

def SortByAngle(visibiltyPolygon, lightSource):
 angleTripples = []
 halfAngle = 0.5*lightSource.lightAngle
 for p in visibiltyPolygon:
  line = Line2D(Point2D(0, 0), p)
  angle = math.atan2(line.direction.y, line.direction.x)
  inside = angle >= -halfAngle and angle <= halfAngle
  angleTripples.append((angle, p, inside))
 if len(angleTripples) <= 0:
  return angleTripples
 angleTripples.sort(key=lambda tup: tup[0])

# Remove duplicates (note separate points may share
# the same angle, so we use inter-point distance to discriminate).

 oldTripple = angleTripples[0]
 newAngleTripples = []
 newAngleTripples.append(oldTripple)
 for tripple in angleTripples:
  diff = tripple[1].Sub(oldTripple[1])
  d2 = diff.Length2()
  if d2 > veryShort2:
   newAngleTripples.append(tripple)
   oldTripple = tripple

# Eliminate everything outside the angle of the light sheet

 angleTripples = []
 beenInside = False
 for i in range (0, len(newAngleTripples)):
  tripple = newAngleTripples[i]
  if tripple[2]:
   if i > 0:
    previous = newAngleTripples[i - 1]
    if not previous[2]:
     angleTripples.append(CrossingPoint(previous, tripple, -halfAngle))
   angleTripples.append(tripple)
   beenInside = True
  elif beenInside:
   if i < len(newAngleTripples) - 1:
    previous = newAngleTripples[i - 1]
    if previous[2]:
     angleTripples.append(CrossingPoint(previous, tripple, halfAngle))  
 
 return angleTripples  
     
# Cast rays from the origin (where the light is) through the points lineWithEnds(r), find
# what they hit, add that to the output polygon, sort that into angle order, then
# convert it back to 3D.  Almost all this function and the functions it calls work
# in 2D except for the very last line.

def RayCast2D(lines, faces, lightSource):
 visibilityPolygon = []
 for lineWithEnds in lines:
  for r in (0, 1): 
   p1 = lineWithEnds.Point(r)

 # Find the other line at this point

   otherLine = FindOtherLineAtPoint(p1, lineWithEnds, lines)
   ray = Line2D(Point2D(0, 0), p1)

 # s is the ray's parameter. We need to know the closest hit to 
 # p0, and possibly (if that is a projecting vertex) the point hit
 # behind that.

   minS = 1
   minFace = lineWithEnds.face
   minBehind = sys.float_info.max
   behindFace = None
   for line1 in lines:
    if line1 is not lineWithEnds and line1 is not otherLine:
     s, t = ray.Cross(line1)
     if s is not None:
      if t >= 0 and t <= 1:
       if s > 0:
        if s < minBehind:
         minBehind = s
         behindFace = line1.face
        if s < minS:
         minS = s
         minFace = line1.face
     else:
      if ray.IsSameLine(line1):
       minS = 0
       minFace = line1.face
   classification = 0
   if (abs(minS - 1) < veryShort) and (behindFace is not None):
    classification = ExtremePoint(p1, ray, lineWithEnds, otherLine, r, lines)
   if classification > 0:
    p2 = ray.Point(minBehind)
    p2.SetFace(behindFace)
    visibilityPolygon.append(p2)
    p3 = ray.Point(minS)
    p3.SetFace(minFace)
    visibilityPolygon.append(p3)
   elif classification is 0:
    p2 = ray.Point(minS)
    p2.SetFace(minFace)
    visibilityPolygon.append(p2)
   else:     
    p2 = ray.Point(minS)
    p2.SetFace(minFace)
    visibilityPolygon.append(p2)
    p3 = ray.Point(minBehind)
    p3.SetFace(behindFace)
    visibilityPolygon.append(p3)
 angleTripples = SortByAngle(visibilityPolygon, lightSource)
 return Make3DPolygons(angleTripples, faces, lightSource) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3D functions for simulating cameras by ray tracing
# ----------------------------------------------------------------

# Cast a ray and find the distance to the first solid 3D thing it hits
# The ray is turned into a FreeCAD line segment longer
# than the space being probed.  4 items are returned:
#
# (distance between ray and shape, distance to hit point from ray start point, normal at hit point, hit point)
#
# Note that the ray-shape distance will be (aproximately) 0 if the ray hits, and the second distance returned
# will be what is usually wanted.

def RayIntoSolid(ray, solid):
 direction = ray[1].sub(ray[0])
 direction.normalize()
 newEnd = ray[0].add(direction.multiply(veryLong))
 fcRay = Part.makeLine(ray[0],newEnd)
 distss = solid.Shells[0].distToShape(fcRay)
 if distss[0] < veryShort:
  info = distss[2][0]
  normal = solid.Shells[0].Faces[info[1]].normalAt(info[2][0],info[2][1])
  hitPoint = distss[1][0][0]
  rayHitD = hitPoint.sub(ray[0]).Length
  return (distss[0], rayHitD, normal, hitPoint)
 else:
  return (None, None, None, None)

# Work out Lambert's Law illumination intensity at point with surface normal
# normal from a light soutce at lightSource. Answer is in [0.0, 1.0].

def Illumination(point, normal, lightSource):
 lightPoint = lightSource.AbsoluteOffset()
 iRay = point.sub(lightPoint).normalize()
 normal.normalize()
 i = normal.dot(iRay)
 if i < 0.0:
  i = 0.0
 return i

# Find the parameter values along two lines in space at their closest point.
# The standard way to find the distance between two such lines is to find the
# two parallel planes in which they lie, then work out the distance between those.
# Here we find one such plane, project the lines into it, then find
# the parameter values where those two 2D lines cross.
# The lines are defined by endpoint pairs: (Base.Vector(), Base.Vector())

def ClosestPointsParameters(line1, line2):
 d1 = line1[1].sub(line1[0])
 d2 = line2[1].sub(line2[0])
 planeNormal = d1.cross(d2)

 if planeNormal.Length < veryShort:
  return None, None # Lines parallel

 # Gram–Schmidt orthonormalise to get a 2D coordinate system in the plane

 planeX = planeNormal.cross(d1)
 planeX.normalize()
 planeY = planeNormal.cross(planeX)
 planeY.normalize()

 # Project the lines into the plane and find the parameters where they intersect

 origin1 = Point2D(planeX.dot(line1[0]), planeY.dot(line1[0]))
 origin2 = Point2D(planeX.dot(line2[0]), planeY.dot(line2[0]))
 second1 = Point2D(planeX.dot(line1[1]), planeY.dot(line1[1]))
 second2 = Point2D(planeX.dot(line2[1]), planeY.dot(line2[1]))
 line1 = Line2D(origin1, second1)
 line2 = Line2D(origin2, second2)
 return line1.Cross(line2)

# Return the point on a ray with a given parameter value

def RayPoint(ray, s):
 direction = ray[1].sub(ray[0])
 direction.multiply(s)
 return ray[0].add(direction) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The main simulator class - this represents a part of the scanner.  The parts are arranged in a tree.
# ------------------------------------------------------------------------------------------------------------------------------

class ScannerPart:
 def __init__(self, offset = Base.Vector(0, 0, 0), u = Base.Vector(1, 0, 0), v = Base.Vector(0, 1, 0), w = Base.Vector(0, 0, 1), parent = None,\
  lightAngle = -1, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1):

  # Offset from the parent in the parent's coordinate system
  # If the parent is None these are absolute cartesian coordinates

  self.offset = offset

  # Local Cartesian coordinates
 
  self.u = u.normalize()
  self.v = v.normalize()
  self.w = w.normalize()

  # If we are a light source (i.e. lightAngle >= 0)

  if lightAngle > math.pi:
   print("Light source with angle > pi: ", lightAngle)

  self.lightAngle = lightAngle

  # If we are a camera (i.e. focalLength >= 0)

  self.uPixels = uPixels
  self.vPixels = vPixels
  self.uMM = uMM
  self.vMM = vMM
  self.focalLength = focalLength

  # Orientation

  self.orientation = Base.Placement()

  # Parent and children in the tree

  self.parent = parent
  self.children = []
  if parent is not None:
   parent.children.append(self)

  # Used for lazy evaluation of position

  self.notMoved = False
  self.position = Base.Vector(0, 0, 0)

#-----------------

# Compute my absolute offset from the origin recursively
# Use lazy evaluation if I haven't moved.

 def AbsoluteOffset(self):
  if self.notMoved:
   return self.position

  if self.parent is None:
   self.position = self.offset
  else:
   parentUO = copy.deepcopy(self.parent.u)
   parentVO = copy.deepcopy(self.parent.v)
   parentWO = copy.deepcopy(self.parent.w)
   parentUO = parentUO.multiply(self.offset.x)
   parentVO = parentVO.multiply(self.offset.y)
   parentWO = parentWO.multiply(self.offset.z)
   o = parentUO.add(parentVO.add(parentWO))
   self.position = o.add(self.parent.AbsoluteOffset())
  self.notMoved = True
  return self.position

# Rotate my coordinates, and the coordinates of all my descendents recursively

 def Rotate(self, r):
  self.notMoved = False
  self.u = r.multVec(self.u).normalize()
  self.v = r.multVec(self.v).normalize()
  self.w = r.multVec(self.w).normalize()
  p = Base.Placement(Base.Vector(0, 0, 0), r)
  self.orientation = p.multiply(self.orientation)
  for child in self.children:
   child.Rotate(r)

# Take any piece of FreeCAD geometry, s, in the World coordinate system and put it in my coordinate system.

 def PutShapeInMyCoordinates(self, s):
  s.transformShape(self.orientation.toMatrix())
  s.translate(self.AbsoluteOffset())

# Rotate about the u axis. angle is in radians

 def RotateU(self, angle):
  self.notMoved = False
  r = Base.Rotation(self.u, angle*180/math.pi)
  self.Rotate(r)

# Rotate about the v axis. angle is in radians

 def RotateV(self, angle):
  self.notMoved = False
  r = Base.Rotation(self.v, angle*180/math.pi)
  self.Rotate(r)

# Rotate about the w axis. angle is in radians

 def RotateW(self, angle):
  self.notMoved = False
  r = Base.Rotation(self.w, angle*180/math.pi)
  self.Rotate(r)

# Draw a line to represent the camera ray from the pixel through the lens

 def DisplayCameraRay(self, ray):
  pixel = ray[0]
  lens = ray[1]
  direction = lens.sub(pixel)
  direction.multiply(veryLong)
  DisplayShape(Part.LineSegment(pixel, pixel.add(direction)).toShape(), (0.0, 0.0, 0.5))

# Create the ray from a pixel in a camera's [u, v] plane through the centre of the lens.

 def GetCameraRay(self, pixelU, pixelV):
   u = copy.deepcopy(self.u)
   u.multiply(pixelU)
   v = copy.deepcopy(self.v)
   v.multiply(pixelV)
   pixel = self.AbsoluteOffset().add(u).add(v)  
   w = copy.deepcopy(self.w)
   w.multiply(self.focalLength)
   lens = self.AbsoluteOffset().add(w)
   return (pixel, lens)

# As above, but so that parameter values along the ray measure real distance

 def GetCameraRayNormalised(self, pixelU, pixelV):
  ray = self.GetCameraRay(pixelU, pixelV)
  direction = ray[1].sub(ray[0])
  direction.normalize()
  newRay = (ray[0], ray[0].add(direction))
  return newRay

# Find the pixel (u, v) in the camera's image plane that the point p projects into

 def ProjectPointIntoCameraPixel(self, p):
  w = copy.deepcopy(self.w)
  w.multiply(self.focalLength)
  pRelativeInv = self.focalLength/p.sub(self.AbsoluteOffset().add(w)).dot(self.w)
  pd = self.AbsoluteOffset().sub(p)
  u = pd.dot(self.u)*pRelativeInv
  v = pd.dot(self.v)*pRelativeInv
  u = int(round((u + 0.5*self.uMM)*(self.uPixels - 1)/self.uMM))
  v = int(round((v + 0.5*self.vMM)*(self.vPixels - 1)/self.vMM))
  return (u, v)

# Make a 3D model of the tree recursively and plot it to check
# what we've got.

 def Display(self, showLight = False, showCamera = False):
  p1 = self.AbsoluteOffset()
  uc = Part.makeCylinder(0.2, 5, p1, self.u, 360)
  DisplayShape(uc, (1.0, 0.0, 0.0))
  vc = Part.makeCylinder(0.2, 5, p1, self.v, 360)
  DisplayShape(vc, (0.0, 1.0, 0.0))
  wc = Part.makeCylinder(0.2, 5, p1, self.w, 360)
  DisplayShape(wc, (0.0, 0.0, 1.0))
  
  # Light source - display the light sheet

  if self.lightAngle > 0 and showLight:
   vv = copy.deepcopy(self.v)
   ww = copy.deepcopy(self.w)
   vv.multiply(veryLong*math.sin(self.lightAngle*0.5))
   ww.multiply(veryLong*math.cos(self.lightAngle*0.5))
   p2 = p1.add(vv).add(ww)
   p3 = p1.sub(vv).add(ww)
   e1 = Part.makeLine(p1, p2)
   e2 = Part.makeLine(p2, p3)
   e3 = Part.makeLine(p3, p1)
   DisplayShape(Part.Wire([e1,e2,e3]), (0.5, 0.0, 0.0))

  # Camera - display the view pyramid

  if self.focalLength > 0 and showCamera:
   for u in (-1, 1):
    for v in (-1, 1):
     ray = self.GetCameraRay(self.uMM*0.5*u, self.vMM*0.5*v)
     self.DisplayCameraRay(ray)

  if self.parent is not None:
   p0 = self.parent.AbsoluteOffset()
  else:
   p0 = Base.Vector(0, 0, 0)
  twig = Cylinder(p0, p1, 0.1)
  DisplayShape(twig, (1.0, 1.0, 0.0))
  for child in self.children:
   child.Display(showLight, showCamera)

# Convert a point p in the [v, w] plane into a point in absolute 3D space.
# The [v, w] plane is the light sheet for a light source.  Remember that
# w is the plane's x axis because w is the centre of the beam.  
# This and the next function are for the light sheet simulation.

 def vwPoint(self, p):
  w = copy.deepcopy(self.w)
  w.multiply(p.x)
  v = copy.deepcopy(self.v)
  v.multiply(p.y)
  return self.AbsoluteOffset().add(v).add(w)

# Project a 3D point into the [v, w] plane.  Again w is the x axis.

 def xyPoint(self, p3D):
  x = self.w.dot(p3D)
  y = self.v.dot(p3D)
  p = Point2D(x, y)
  return p

# Convert a point p in the [u, v] plane into a point in absolute 3D space.
# The [u, v] plane is the focal plane of a camera, which points along the
# w axis.  The lens (or pinhole) is self.focalLength along w.  

 def uvPoint(self, p):
  u = copy.deepcopy(self.u)
  u.multiply(p.x)
  v = copy.deepcopy(self.v)
  v.multiply(p.y)
  return self.AbsoluteOffset().add(u).add(v)

# Generate the polygon mask - the projection of the polygons into the
# image plane of the camera dilated by an appropriate width to allow for
# the width of the light sheet.  We only need to raytrace
# the resulting pixels to find the actual image of the polygon.
# Why can't we use this as the image of the polygon (it'd be quicker)? - Because it does not
# allow for parts of the room obscuring a camera's view, and because rays from
# camera pixels will not in general intersect the polygons; they will just run
# near them.

 def PolygonMask(self, polygons):
  mask = NewImage(self.uPixels, self.vPixels)
  draw = Draw(mask)
  for polygon in polygons:
   pair = polygon[0]
   p0 = pair[0]
   for i in range(1, len(polygon)):
    pair = polygon[i]
    p1 = pair[0]
    uv0 = self.ProjectPointIntoCameraPixel(p0)
    uv1 = self.ProjectPointIntoCameraPixel(p1)
    DrawLine(draw, uv0, uv1, 255)
    p0 = p1
  return Filter(mask, 3)

# Cast a single ray into the scene and find the bit of polygon it hits.
# startingPolygonDistance is the closest thing to the camera along the
# ray already found in the room; anything behind that is invisible.

 def CastRay(self, ray, room, polygons, startingPolygonDistance):
  minPolygonDistance = startingPolygonDistance
  rayHitPolygon = False
  for polygon in polygons:
   pair = polygon[0]
   firstPoint = pair[0]
   for i in range(1, len(polygon)):
    pair = polygon[i]
    secondPoint = pair[0]
    polygonLine = (firstPoint, secondPoint)
    s, t = ClosestPointsParameters(ray, polygonLine)
    if s is not None:
     if s > 0:
      if t < 0:
       t = 0
      elif t > 1:
       t = 1
      rayPoint = RayPoint(ray, s)
      uv0 = self.ProjectPointIntoCameraPixel(rayPoint)
      testObstructionRay = self.GetCameraRayNormalised(uv0[0], uv0[1])
      testObstruction = RayIntoSolid(testObstructionRay, room)[1]
      if testObstruction is None or testObstruction + veryShort > s: # NB - relies on OR operator not bothering with second argument if first is True
       polygonPoint = RayPoint(polygonLine, t)
       rayLightDistance = rayPoint.sub(polygonPoint).Length
       if s < minPolygonDistance and rayLightDistance < 3*lightSD:
        minRayLightDistance = rayLightDistance
        rayHitPolygon = True
        minPolygonDistance = s
    firstPoint = secondPoint
  if rayHitPolygon:
    return int(round(255.0*GaussianLightIntensity(minRayLightDistance)))
  return 0
  

# If we are a camera...
# Take a visibilityPolygon from a light source and find what it looks like.

 def SaveCameraImageLights(self, room, polygons, fileName):
  if self.focalLength <= 0:
   print("Light image requested for non camera.")
  polygonMask = self.PolygonMask(polygons)
  uInc = self.uMM/(self.uPixels - 1)
  vInc = self.vMM/(self.vPixels - 1)
  v = -self.vMM*0.5
  image = NewImage(self.uPixels, self.vPixels)
  for row in range(0, self.vPixels): 
   u = -self.uMM*0.5
   for column in range(0, self.uPixels):
    if polygonMask.getpixel((column, row)) != 0:
     ray = self.GetCameraRayNormalised(u, v)
     minRoomDistance = RayIntoSolid(ray, room)[1]
     if minRoomDistance is None:
      startingPolygonDistance = sys.float_info.max
     else:
      startingPolygonDistance = minRoomDistance + veryShort # We want a surface the light sheet hits to be just behind the line of light in it, so that is seen not the surface.
     hit = self.CastRay(ray, room, polygons, startingPolygonDistance)
     if hit != 0:
      SetPixel(image, column, row, hit)
    u += uInc
   v += vInc
  SavePicture(image, fileName + "-light.png")
  if debug:
   SavePicture(polygonMask, fileName + "-light-mask.png")

# If we are a camera...
# Save a ray-traced image of the room.

 def SaveCameraImageRoom(self, room, light, fileName):
  if self.focalLength <= 0:
   print("Room image requested for non camera.")
  polygonMask = self.PolygonMask(polygons)
  uInc = self.uMM/(self.uPixels - 1)
  vInc = self.vMM/(self.vPixels - 1)
  v = -self.vMM*0.5
  image = NewImage(self.uPixels, self.vPixels)
  for row in range(0, self.vPixels): 
   u = -self.uMM*0.5
   for column in range(0, self.uPixels):
    ray = self.GetCameraRayNormalised(u, v)
    rayHit = RayIntoSolid(ray, room)
    minRoomDistance = rayHit[1]
    if minRoomDistance is None:
     SetPixel(image, column, row, 0)
    else:
     if rayHit[2] is not None:
      i = 125 + int(round(Illumination(rayHit[3], rayHit[2], light)*125.0))
      SetPixel(image, column, row, i)
     else:
      SetPutpixel(image, column, row, 50)
    u += uInc
   v += vInc
  SavePicture(image, fileName + "-room.png")
   

# If we are a light source...
# Turn on the light and make a cross section of a shape, s.
# Then compute its visibility polygon in the 2D plane of the light
# sheet (the [v, w] plane) and return that as a FreeCAD object in 3D.
# (See: https://en.wikipedia.org/wiki/Visibility_polygon)

 def GetVisibilityPolygons(self, room):
  if self.lightAngle <= 0:
   print("Illuminated polygon requested for non light source.")

  # The edges of the beam - not used, but left here as may be useful
  """
  wall1 = Part.makeBox(4, 1, veryLong)
  wall2 = Part.makeBox(4, 1, veryLong)
  wall1.translate(Base.Vector(-2, -1, -3))
  wall2.translate(Base.Vector(-2, 0, -3))
  wall1.rotate(Base.Vector(0, 0, 0),Base.Vector(1, 0, 0), 0.5*self.lightAngle*180/math.pi)
  wall2.rotate(Base.Vector(0, 0, 0),Base.Vector(1, 0, 0), -0.5*self.lightAngle*180/math.pi)
  self.PutShapeInMyCoordinates(wall1)
  self.PutShapeInMyCoordinates(wall2)
  s = s.fuse(wall1)
  s = s.fuse(wall2)
  Part.show(s)
  """

  # The origin of coordinates in the 2D light sheet (x0, y0) is the projection of the position
  # of the light source in 3D into the light source's [v, w] plane.  We use (x, y) for
  # coordinates in the plane to avoid confuusion with the u, v, and w vectors.

  p0 = self.AbsoluteOffset()

  origin2D = self.xyPoint(p0)
  lines = []

 # We have to visit each face of object s in turn and compute the line of
 # intersection of the light sheet plane with it because the FreeCAD CrossSection
 # function for whole objects creates internal triangulations in cross-section polygons,
 # which we don't want.

  faces = room.Faces

  for face in faces:

   # Where does the plane cut the face? Note that line may have
   # more than one section if the face has a hole in it.

   faceLines = CrossSection(face, p0, self.u)

   for line in faceLines:
    vertexes = line.Vertexes
    if len(vertexes) is not 2:
     print("Line without 2 ends!", len(vertexes))
    else:

    # Find the projection of line into the light sheet plane.
    # The projection of the light source point is the origin
    # of coordinates.

    # We keep track of the face each line came from, though (perhaps surprisingly)
    # that is not much use.

     v2D0 = self.xyPoint(vertexes[0].Point).Sub(origin2D)
     v2D1 = self.xyPoint(vertexes[1].Point).Sub(origin2D)     

     line = Line2D(v2D0, v2D1, face)
     lines.append(line)

  # Cast a ray from the light source through each line end in turn and add what it hits
  # to the visibility polygons.  Process those polygons back into 3D.

  return RayCast2D(lines, faces, self)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Testing, testing...

ClearAll()

# Make the scanner

world = ScannerPart()
scanner = ScannerPart(offset = Base.Vector(38, 12, 10), parent = world)
lightSource = ScannerPart(offset = Base.Vector(0, 10, 0), parent = scanner, lightAngle = 1)
camera = ScannerPart(offset = Base.Vector(0, -10, 0), parent = scanner, uPixels = 75, vPixels = 100, uMM = 1.5, vMM = 2, focalLength = 5) 
lightSource.RotateV(-0.5*math.pi)
lightSource.RotateW(0.5*math.pi)
lightSource.RotateV(-0.5)
camera.RotateV(-0.5*math.pi)
camera.RotateU(-0.1)
camera.RotateW(-0.5*math.pi)

world.Display(showCamera = True)

# Make the room

a = Part.makeBox(10, 4, 12)
a.translate(Base.Vector(0, 3, 0))
b = Part.makeBox(10, 8, 30)
c =  Part.makeBox(10, 8, 30)
c.translate(Base.Vector(0, 16, 0))
b = b.fuse(c)
b = b.cut(a)
d = Part.makeBox(7, 4, 2)
d.translate(Base.Vector(1, 1, 9))
room = b.fuse(d)

roomLight = ScannerPart(offset = Base.Vector(200, 200, 1000), parent = world)

Part.show(room)

# Run a scan and save the image

polygons = lightSource.GetVisibilityPolygons(room)
PlotPolygons(polygons)
camera.SaveCameraImageLights(room, polygons, "/home/ensab/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator/scan")
#camera.SaveCameraImageRoom(room, roomLight, "/home/ensab/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator/scan")







