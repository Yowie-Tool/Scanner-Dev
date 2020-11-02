
import Part, BOPTools, FreeCAD, math, copy, sys
from FreeCAD import Base
import PySide
from PySide import QtGui, QtCore
from PIL import Image, ImageDraw, ImageFilter

from GraphicsFunctions import *

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
  if self.focalLength <= 0:
   print("Attempt to get a pixel ray from a scanner part that is not a camera.")
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

# Find the implicit plane equation of the light sheet, returned as the normal vector and the origin offset constant

 def GetLightPlane(self):
  if self.lightAngle <= 0:
   print("Attempt to get a light plane from a scanner part that is not a light source.")
  uu = copy.deepcopy(self.u)
  pointInPlane = self.AbsoluteOffset()
  offset = -uu.dot(pointInPlane)
  return (uu, offset)

# Find the point in space where the ray from a camera pixel (mm coordinates) hits the light sheet from this light source

 def CameraPixelIsPointInMyPlane(self, camera, pixelU, pixelV):
  plane = self.GetLightPlane()
  normal = plane[0]
  d = plane[1]
  ray = camera.GetCameraRay(pixelU, pixelV)
  t0Point = ray[0]
  rayDirection = ray[1].sub(ray[0])
  sp = rayDirection.dot(normal)
  if abs(sp) < veryShort2:
   print("Ray is parallel to plane.")
   return Base.Vector(0, 0, 0)
  t = -d/sp
  tPoint = rayDirection.multiply(t).add(t0Point)
  return tPoint

# Find the point in space where the ray from a camera pixel (pixel indices) hits the light sheet from this light source

 def CameraPixelIndicesArePointInMyPlane(self, camera, pixelUIndex, pixelVIndex):
  pixelU = pixelUIndex*self.uMM
  pixelV = pixelVIndex*self.vMM
  return self.CameraPixelIsPointInMyPlane(camera, pixelU, pixelV)

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
