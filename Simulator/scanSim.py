# Beech Design Scanner Simulation
# Adrian Bowyer
# 19 February 2020

sys.path.append('/home/ensab/Desktop/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator')

import Part, BOPTools, FreeCAD, copy, sys
import math as maths
from FreeCAD import Base
#import PySide
#from PySide import QtGui, QtCore
from PIL import Image, ImageDraw, ImageFilter
from YowieScanner import *

# When True, output useful diagnostic information

debug = True

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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Functions that work with the main ScannerPart simulator class and FreeCAD, but are not part of the class.  This allows that class to stand alone
# without FreeCAD for other uses.

#-----------------

# Turn a ScannerPart vector or matrix into a FreeCAD vector or homogeneous matrix, and vectors the other way

def FreeCADv(v):
 if not isinstance(v, Vector3):
  raise Exception('Converting ' + str(type(v)) + ' to Base.Vector!')
 return Base.Vector(v.x, v.y, v.z)

def Simv(v):
 if not isinstance(v, Base.Vector):
  raise Exception('Converting ' + str(type(v)) + ' to Vector3!')
 return Vector3(v.x, v.y, v.z)

def FreeCADm(m):
 if not isinstance(m, RotationM):
  raise Exception('Converting ' + str(type(m)) + ' to FreeCAD.Matrix!')
 result = FreeCAD.Matrix()
 result.A11 = m.r[0][0]
 result.A21 = m.r[1][0]
 result.A31 = m.r[2][0]
 result.A41 = 0

 result.A12 = m.r[0][1]
 result.A22 = m.r[1][1]
 result.A32 = m.r[2][1]
 result.A42 = 0

 result.A13 = m.r[0][2]
 result.A23 = m.r[1][2]
 result.A33 = m.r[2][2]
 result.A43 = 0

 result.A14 = 0
 result.A24 = 0
 result.A34 = 0
 result.A44 = 1 
 return result

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Useful general FreeCAD functions
# There must be an easier way to make the FreeCAD null set...

def Null():
 n1 = Part.makeBox(1, 1, 1)
 n2 = Part.makeBox(1, 1, 1)
 n2.translate(Base.Vector(10, 10, 10))
 return(n1.common(n2))


# Make a cylinder between two points of a given radius

def Cylinder(p0, p1, r):
 p2 = p1.Sub(p0)
 length = maths.sqrt(p2.Length2())
 if length < 0.0001:
  return Null()
 c = Part.makeCylinder(r, length, FreeCADv(p0), FreeCADv(p2), 360)
 return c

# Make a plane cross section of FreeCAD geometry s, and return it as a list of 2d line segments
# The plane passes through point p0 and has normal n

def CrossSection(scannerPart, s, p0, n):
 nn = n.Normalize()
 d = nn.Dot(p0)
 wires=[]
 sl = s.slice(FreeCADv(nn), d)
 for wire in sl:
  wires.append(wire)
 lineEnds = []
 for line in wires:
  vertexes = line.Vertexes
  if len(vertexes) != 2:
   print("Line without 2 ends!", len(vertexes))
  else:

   # Find the projection of line into the light sheet plane.
   # The projection of the light source point is the origin
   # of coordinates.

   # We keep track of the FreeCAD geometry each line came from, though (perhaps surprisingly)
   # that is not much use.

   v2D0 = scannerPart.xyPoint(Simv(vertexes[0].Point))
   v2D1 = scannerPart.xyPoint(Simv(vertexes[1].Point))
   ln = Line2D(v2D0, v2D1, s)
   lineEnds.append(ln)
 return lineEnds

# Display a FreeCAD shape with a given colour as an RGB float tripple like (0.0, 1.0, 0.0)

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

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
 v = Part.Vertex(FreeCADv(p))
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
  halfWayPoint = p3D1.Add(p3D2)
  halfWayPoint = halfWayPoint.Multiply(0.5)
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
   wire.append(FreeCADv(pair[0]))
  DisplayShape(Part.makePolygon(wire), (1.0, 0.0, 0.0))

# Find the point on the line from previous to current where a line at angle crosses

def CrossingPoint(previous, current, angle):
 line1 = Line2D(Point2D(0, 0), Point2D(maths.cos(angle), maths.sin(angle)))
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
  angle = maths.atan2(line.direction.y, line.direction.x)
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
   elif classification == 0:
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
 direction = ray[1].Sub(ray[0])
 direction = direction.Normalize()
 newEnd = ray[0].Add(direction.Multiply(veryLong))
 fcRay = Part.makeLine(FreeCADv(ray[0]), FreeCADv(newEnd))
 distss = solid.Shells[0].distToShape(fcRay)
 if distss[0] < veryShort:
  info = distss[2][0]
  normal = Simv(solid.Shells[0].Faces[info[1]].normalAt(info[2][0],info[2][1]))
  hitPoint = Simv(distss[1][0][0])
  rayHitD = maths.sqrt(hitPoint.Sub(ray[0]).Length2())
  return (distss[0], rayHitD, normal, hitPoint)
 else:
  return (None, None, None, None)

# Draw a line to represent the camera ray from the pixel through the lens

def DisplayCameraRay(ray):
 pixel = ray[0]
 lens = ray[1]
 direction = lens.Sub(pixel)
 direction = direction.Multiply(veryLong)
 DisplayShape(Part.LineSegment(FreeCADv(pixel), FreeCADv(pixel.Add(direction))).toShape(), (0.0, 0.0, 0.5))

# Work out Lambert's Law illumination intensity at point with surface normal
# normal from a light soutce at lightSource. Answer is in [0.0, 1.0].

def Illumination(point, normal, lightSource):
 lightPoint = lightSource.AbsoluteOffset()
 iRay = point.Sub(lightPoint).Normalize()
 normal = normal.Normalize()
 i = normal.Dot(iRay)
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
 d1 = line1[1].Sub(line1[0])
 d2 = line2[1].Sub(line2[0])
 planeNormal = d1.Cross(d2)

 if planeNormal.Length2() < veryShort2:
  return None, None # Lines parallel

 # Gram–Schmidt orthonormalise to get a 2D coordinate system in the plane

 planeX = planeNormal.Cross(d1)
 planeX = planeX.Normalize()
 planeY = planeNormal.Cross(planeX)
 planeY = planeY.Normalize()

 # Project the lines into the plane and find the parameters where they intersect

 origin1 = Point2D(planeX.Dot(line1[0]), planeY.Dot(line1[0]))
 origin2 = Point2D(planeX.Dot(line2[0]), planeY.Dot(line2[0]))
 second1 = Point2D(planeX.Dot(line1[1]), planeY.Dot(line1[1]))
 second2 = Point2D(planeX.Dot(line2[1]), planeY.Dot(line2[1]))
 line1 = Line2D(origin1, second1)
 line2 = Line2D(origin2, second2)
 return line1.Cross(line2)

# Return the point on a ray with a given parameter value

def RayPoint(ray, s):
 direction = ray[1].Sub(ray[0])
 direction = direction.Multiply(s)
 return ray[0].Add(direction) 


# Generate the polygon mask - the projection of the polygons into the
# image plane of the camera dilated by an appropriate width to allow for
# the width of the light sheet.  We only need to raytrace
# the resulting pixels to find the actual image of the polygon.
# Why can't we use this as the image of the polygon (it'd be quicker)? - Because it does not
# allow for parts of the room obscuring a camera's view, and because rays from
# camera pixels will not in general intersect the polygons; they will just run
# near them.

def PolygonMask(scannerPart, polygons):
 mask = NewImage(scannerPart.uPixels, scannerPart.vPixels)
 draw = Draw(mask)
 for polygon in polygons:
  pair = polygon[0]
  p0 = pair[0]
  for i in range(1, len(polygon)):
   pair = polygon[i]
   p1 = pair[0]
   uv0 = scannerPart.ProjectPointIntoIntegerCameraPixel(p0)
   uv1 = scannerPart.ProjectPointIntoIntegerCameraPixel(p1)
   DrawLine(draw, uv0, uv1, 255)
   p0 = p1
 return Filter(mask, 3)

# Take any piece of FreeCAD geometry, s, in the World coordinate system and put it in my coordinate system.

def PutShapeInMyCoordinates(scannerPart, s):
 s.transformShape(FreeCADm(scannerPart.orientation))
 s.translate(scannerPart.AbsoluteOffset())

# Make a 3D model of the tree recursively and plot it to check
# what we've got.

def Display(scannerPart, showLight = False, showCamera = False):
 p1 = scannerPart.AbsoluteOffset()
 uc = Part.makeCylinder(0.2, 50, FreeCADv(p1), FreeCADv(scannerPart.u), 360)
 DisplayShape(uc, (1.0, 0.0, 0.0))
 vc = Part.makeCylinder(0.2, 50, FreeCADv(p1), FreeCADv(scannerPart.v), 360)
 DisplayShape(vc, (0.0, 1.0, 0.0))
 wc = Part.makeCylinder(0.2, 50, FreeCADv(p1), FreeCADv(scannerPart.w), 360)
 DisplayShape(wc, (0.0, 0.0, 1.0))
  
  # Light source - display the light sheet

 if scannerPart.lightAngle > 0 and showLight:
  vv = scannerPart.v
  ww = scannerPart.w
  vv = vv.Multiply(veryLong*maths.sin(scannerPart.lightAngle*0.5))
  ww = ww.Multiply(veryLong*maths.cos(scannerPart.lightAngle*0.5))
  p2 = p1.Add(vv).Add(ww)
  p3 = p1.Sub(vv).Add(ww)
  e1 = Part.makeLine(FreeCADv(p1), FreeCADv(p2))
  e2 = Part.makeLine(FreeCADv(p2), FreeCADv(p3))
  e3 = Part.makeLine(FreeCADv(p3), FreeCADv(p1))
  DisplayShape(Part.Wire([e1,e2,e3]), (0.5, 0.0, 0.0))

  # Camera - display the view pyramid

 if scannerPart.focalLength > 0 and showCamera:
  for u in (-1, 1):
   for v in (-1, 1):
    ray = scannerPart.GetCameraRay((scannerPart.uMM*0.5*u, scannerPart.vMM*0.5*v))
    DisplayCameraRay(ray)

 if scannerPart.parent is not None:
  p0 = scannerPart.parent.AbsoluteOffset()
 else:
  p0 = Vector3(0, 0, 0)
 twig = Cylinder(p0, p1, 0.1)
 DisplayShape(twig, (1.0, 1.0, 0.0))
 for child in scannerPart.children:
  Display(child, showLight, showCamera)

# Cast a single ray into the scene and find the bit of polygon it hits.
# startingPolygonDistance is the closest thing to the camera along the
# ray already found in the room; anything behind that is invisible.

def CastRay(scannerPart, ray, room, polygons, startingPolygonDistance):
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
     uv0 = scannerPart.ProjectPointIntoIntegerCameraPixel(rayPoint)
     testObstructionRay = scannerPart.GetCameraRayNormalised(uv0[0], uv0[1])
     testObstruction = RayIntoSolid(testObstructionRay, room)[1]
     if testObstruction is None or testObstruction + veryShort > s: # NB - relies on OR operator not bothering with second argument if first is True
      polygonPoint = RayPoint(polygonLine, t)
      rayLightDistance = maths.sqrt(rayPoint.Sub(polygonPoint).Length2())
      if s < minPolygonDistance and rayLightDistance < 3*lightSD:
       minRayLightDistance = rayLightDistance
       rayHitPolygon = True
       minPolygonDistance = s
   firstPoint = secondPoint
 if rayHitPolygon:
   return int(round(255.0*GaussianLightIntensity(minRayLightDistance)))
 return 0
  
def DisplayScanner(scanner, showLight = False, showCamera = False):
 Display(scanner.world, showLight, showCamera)

# If we are a camera...
# Take a visibilityPolygon from a light source and find what it looks like.

def SaveCameraImageLights(scannerPart, room, polygons, fileName):
 if scannerPart.focalLength <= 0:
  print("Light image requested for non camera.")
 polygonMask = PolygonMask(scannerPart, polygons)
 uInc = scannerPart.uMM/(scannerPart.uPixels - 1)
 vInc = scannerPart.vMM/(scannerPart.vPixels - 1)
 v = -scannerPart.vMM*0.5
 image = NewImage(scannerPart.uPixels, scannerPart.vPixels)
 for row in range(0, scannerPart.vPixels): 
  u = -scannerPart.uMM*0.5
  for column in range(0, scannerPart.uPixels):
   if polygonMask.getpixel((column, row)) != 0:
    ray = scannerPart.GetCameraRayNormalised(u, v)
    minRoomDistance = RayIntoSolid(ray, room)[1]
    if minRoomDistance is None:
     startingPolygonDistance = sys.float_info.max
    else:
     startingPolygonDistance = minRoomDistance + veryShort # We want a surface the light sheet hits to be just behind the line of light in it, so that is seen not the surface.
    hit = CastRay(scannerPart, ray, room, polygons, startingPolygonDistance)
    if hit != 0:
     SetPixel(image, column, row, hit)
   u += uInc
  v += vInc
 SavePicture(image, fileName + "-light.png")
 if debug:
  SavePicture(polygonMask, fileName + "-light-mask.png")

# If we are a camera...
# Save a ray-traced image of the room.

def SaveCameraImageRoom(scannerPart, room, light, fileName):
 if scannerPart.focalLength <= 0:
  print("Room image requested for non camera.")
 polygonMask = PolygonMask(scannerPart, polygons)
 uInc = scannerPart.uMM/(scannerPart.uPixels - 1)
 vInc = scannerPart.vMM/(scannerPart.vPixels - 1)
 v = -scannerPart.vMM*0.5
 image = NewImage(scannerPart.uPixels, scannerPart.vPixels)
 for row in range(0, scannerPart.vPixels): 
  u = -scannerPart.uMM*0.5
  for column in range(0, scannerPart.uPixels):
   ray = scannerPart.GetCameraRayNormalised(u, v)
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

def GetVisibilityPolygons(scannerPart, room):
 if scannerPart.lightAngle <= 0:
  print("Illuminated polygon requested for non light source.")

  # The edges of the beam - not used, but left here as may be useful
  """
  wall1 = Part.makeBox(4, 1, veryLong)
  wall2 = Part.makeBox(4, 1, veryLong)
  wall1.translate(Base.Vector(-2, -1, -3))
  wall2.translate(Base.Vector(-2, 0, -3))
  wall1.rotate(Base.Vector(0, 0, 0),Base.Vector(1, 0, 0), 0.5*self.lightAngle*180/maths.pi)
  wall2.rotate(Base.Vector(0, 0, 0),Base.Vector(1, 0, 0), -0.5*self.lightAngle*180/maths.pi)
  self.PutShapeInMyCoordinates(wall1)
  self.PutShapeInMyCoordinates(wall2)
  s = s.fuse(wall1)
  s = s.fuse(wall2)
  Part.show(s)
  """

  # The origin of coordinates in the 2D light sheet (x0, y0) is the projection of the position
  # of the light source in 3D into the light source's [v, w] plane.  We use (x, y) for
  # coordinates in the plane to avoid confuusion with the u, v, and w vectors.

 p0 = scannerPart.AbsoluteOffset()

 origin2D = scannerPart.xyPoint(p0)
 lines = []

 # We have to visit each face of object s in turn and compute the line of
 # intersection of the light sheet plane with it because the FreeCAD CrossSection
 # function for whole objects creates internal triangulations in cross-section polygons,
 # which we don't want.

 faces = room.Faces

 for face in faces:

   # Where does the [v, w] plane cut the face? Note that line may have
   # more than one section if the face has a hole in it.

  crossLines = CrossSection(scannerPart, face, p0, scannerPart.u)
  for line in crossLines:
   #print(line)
   lines.append(line)


  # Cast a ray from the light source through each line end in turn and add what it hits
  # to the visibility polygons.  Process those polygons back into 3D.
 castLines = RayCast2D(lines, faces, scannerPart)
 #print(castLines)
 return castLines

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Testing, testing...

#ClearAll()

# Initial test setup
'''
# Make the scanner

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

Display(world, showLight = True, showCamera = True)

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

roomLight = ScannerPart(offset = Vector3(200, 200, 1000), parent = world)

Part.show(room)

# Find the point in the light sheet corresponding to the pixel indices (3, 17) in the camera

#print(lightSource.CameraPixelIndicesArePointInMyPlane(camera, 3, 17))

# Run a scan and save the image

polygons = GetVisibilityPolygons(lightSource, room)
PlotPolygons(polygons)
#SaveCameraImageLights(camera, room, polygons, "/home/ensab/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator/scan")
#SaveCameraImageRoom(camera, room, roomLight, "/home/ensab/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator/scan")
'''

# Realistic (?) simulation

# Make the room

a = Part.makeBox(4200, 3400, 2000)
a.translate(Base.Vector(-2100, 0, -500))
b = Part.makeBox(4000, 3600, 3000)
b.translate(Base.Vector(-2000, -300, -400))
room = a.cut(b)

calibration1 = Part.makeBox(500, 500, 2000)
calibration2 = Part.makeBox(500, 500, 2000)
calibration1.rotate(Base.Vector(0,0,0), Base.Vector(0,0,1), 25)
calibration2.rotate(Base.Vector(0,0,0), Base.Vector(0,0,1), 37)
calibration2.translate(Base.Vector(-400, 2500, -500))
calibration1.translate(Base.Vector(300, 2200, -500))
room = room.fuse(calibration1)
room = room.fuse(calibration2)

#roomLight = ScannerPart(offset = Vector3(200, 200, 1000), parent = world)

Part.show(room)

# Make the scanner

world = ScannerPart()

#scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(0, 0, -250), lightAng = 2, lightToeIn = 0, cameraOffset =
#		 Vector3(0, 0, 250), cameraToeIn = 0, uPix = 2464, vPix = 3280, uMM = 17.64, vMM = 24.088543586543586, focalLen = 25)

scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0, cameraOffset =
		 Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)


#parameters = [0, 0, 0, 36, 0, 0, 51.39949028832171, -218.6961204575926, 367.2294799139914, 10.49632835398877, 0.0, 3.1383388276659403, 0.0, 0.0, 0.0, 2.77501898418852, 0.027515107997151313, 1.5761757832773262]
#parameters =  [0, 0, 0, 36, 0, 0, 32.30692113512267, 82.30888164978587, 314.7026063287078, 8, 0.0, 1.737705486220911, 0.0, 0.0, 0.0, 4.1162333257310015, 0.050328169663177, 1.5829233965668246]

#parameters = [0, 0, 0, 36, 0, 0, -7.75, 0, 875.9251317989438, 8, 0.0, 5.726812341092995, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#parameters = [0, 0, 0, 36, 0, 0, -22.6444682294842, 85.47764627601349, 314.70025105565344, 8, 0.0, 3.9169581470319557, 0.0, 0.0, 0.0, 1.8668307363657561, 5.763450253256094, 1.2953212901441151, 6.283185216960153, 6.283185301025465, 5.650195866143518]

#parameters = [0, 0, 0, 36, 0, 0, 36.29020647040032, -64.73034918263649, 347.2584403909511, 9.132270456355052, 0.0, 2.536641779027073, 0.09830280745876545, 0.0014337786420365016, 0.007458111749965841, 3.344304399002978, 6.270129696264745, 1.5628220387349634, 6.283153237497993, 6.283152870577741, 6.221876183673617]

#parameters = [0, 0, 0, 36, 0, 0, 40.54412310218522, -331.14949869349306, 434.9368429812787, 11.501019648483128, 0.0, 2.7961872422342324, -0.049942519168004296, 4.802122945945603e-05, 7.675507770043922e-05, 3.1044214707741418, 0.009270538980067768, 1.5618374951458351, -1.0888452878887733e-05, 6.518284688115558e-06, -0.030034593669476806]
# parameters = [0, 0, 0, 36, 0, 0, 12.439261507779436, 85.07398479331971, 307.37393494542715, 8, 0.0, 1.0145322214287944, 0.011076482035381101, -7.119938967292683e-07, -2.7645354041538894e-06, -1.441521377175576, -0.15282795801825255, 1.4866218267968678, -9.38482980217259e-09, -2.8090019199566996e-09, -0.22434910788453966]
#parameters = [0, 0, 0, 36, 0, 0, 12.439261507779436, 85.07398479331971, 307.37393494542715, 8, 0.0, 1.0145322214287944, 0.011076482035381101, -7.119938967292683e-07, -2.7645354041538894e-06, -1.441521377175576, -0.15282795801825255, 1.4866218267968678, -9.38482980217259e-09, -2.8090019199566996e-09, -0.22434910788453966]
#parameters = [0, 0, 0, 36, 0, 0, -77.67100925938196, -115.57042340022296, -525.6018350503149, 8, 0.0, 0.7949931635258309, 0.4371185980733179, -0.011053886932275603, -3.080439164519182, -0.241633574142341, 0.5167833476863131, 2.915309983252303, -5.1632179266292155e-05, 0.00046850441466618687, 0.5573723618476397]
#parameters = [0, 0, 0, 36, 0, 0, -32.4977147802834, -16.63998754693417, 298.236151091774, 8, 0.0, -2.4268965162273943, 2.57670132757694, -1.9969680291609393e-06, -2.5722462151378522e-06, -2.642905334121849, 2.379907610603964, 2.066092949859189, -1.1350292261624872e-08, 6.773814736074422e-09, 1.9214760641142357]

#scanner.MakeScannerFromParameters(parameters, scanner.world, scanner.lightAng, scanner.uPix, scanner.vPix, scanner.uMM, scanner.vMM)


#parameters= [0, 0, 0, 36, 0, 0, 12.439261507779436, 85.07398479331971, 307.37393494542715, 8, 0.0, 1.0145322214287944, 0.011076482035381101, -7.119938967292683e-07, -2.7645354041538894e-06, -1.441521377175576, -0.15282795801825255, 1.4866218267968678, -9.38482980217259e-09, -2.8090019199566996e-09, -0.22434910788453966]

#parameters = [0, 0, 0, 36, 0, 0, 12.439261507779436, 85.07398479331971, 307.37393494542715, 8, 0.0, 1.0145322214287944, 0.011076482035381101, -7.119938967292683e-07, -2.7645354041538894e-06, -1.441521377175576, -0.15282795801825255, 1.4866218267968678, -9.38482980217259e-09, -2.8090019199566996e-09, -0.22434910788453966]

#parameters= [0, 0, 0, 36, 0, 0, -77.67100925938196, -115.57042340022296, -525.6018350503149, 8, 0.0, 0.7949931635258309, 0.4371185980733179, -0.011053886932275603, -3.080439164519182, -0.241633574142341, 0.5167833476863131, 2.915309983252303, -5.1632179266292155e-05, 0.00046850441466618687, 0.5573723618476397]
#parameters =[0, 0, 0, 36, 0, 0, -79.58930233478465, -119.94335530872235, 368.6182785062867, 8, 0.0, 2.3206832323695252, 0.2811842094602123, -0.005962432978913412, 0.03621106569121504, -3.021600105450851, 0.05843739090765727, -1.3674886460585478, 1.8004012199709043e-05, -0.00015473789777598057, 0.46722109901716335]

#parameters= [0, 0, 0, 36, 0, 0, -437.56452815603717, -2480.1147480051973, -865.9332876861472, 8, 0.0, 2.699086327628919, 2.7417224694285585, 3.127680528185189, -0.03343328375210497, 0.49334390183699384, 2.7213947667062457, 0.1408775722546084, -0.0026426447724254842, 0.0010206268566795517, -2.9824265912628443]

parameters= [0, 0, 0, 36, 0, 0, -40.7096641297556, -20.738066413228175, -368.4363531881588, 8, 0.0, 2.002769048771704, 1.114123094161437, -2.4887863769862406e-07, -3.14159038520326, -1.442800871793672, 0.6918499805373136, -2.060428548071253, -6.787762352189475e-09, 2.6747457373792136e-09, 1.159718012175121]

scanner.ImposeParameters(parameters)

DisplayScanner(scanner, showLight = True, showCamera = True)

#roomLight = ScannerPart(offset = Vector3(0, 0, 3000), parent = world)

polygons = GetVisibilityPolygons(scanner.lightSource, room)
PlotPolygons(polygons)
SaveCameraImageLights(scanner.camera, room, polygons, "/home/ensab/rrlOwncloud/RepRapLtd/Engineering/External-Projects/Scantastic/Scanner-Dev/Simulator/calibrate")






