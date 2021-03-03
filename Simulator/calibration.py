# Simulation of scanner calibration

from YowieScanner import *

r2 = maths.sqrt(2.0)
sideLength = 500
2.21576925

# Make a 45, 45, 90 triangle in space at angle apexAndAngle[1] to the X axis with the right angle at apexAndAngle[0]

def Triangle(side, apexAndAngle):
 triangle = []
 x = side*maths.cos(apexAndAngle[1])
 y = side*maths.sin(apexAndAngle[1])
 triangle.append(Vector3(apexAndAngle[0].x - x, apexAndAngle[0].y + y, apexAndAngle[0].z))
 triangle.append(apexAndAngle[0])
 triangle.append(Vector3(apexAndAngle[0].x + y, apexAndAngle[0].y + x, apexAndAngle[0].z))
 return triangle

# Sum the squared errors in the lengths of a triangles sides compared with the ideal 45, 45, 90 triangle

def TriangleSquaredError(triangle, side):
 sum = 0.0
 for i in range(3): 
  if i is not 2:
   s = maths.sqrt(triangle[i].Sub(triangle[(i+1)%3]).Length2()) - side
  else:
   s = maths.sqrt(triangle[i].Sub(triangle[(i+1)%3]).Length2()) - side*r2
  sum += s*s
 return sum

# Take triangles in space, find the pixels in the real camera of their corners, project them back in to the scene using
# the scanner that is to be calibrated, and sum the resulting squared errors.

def TriangleErrors(triangles, realCamera, idealLightSource, idealCamera):
 sum = 0.0
 for triangle in triangles:
  corners = []
  for i in range(3):
   pix = realCamera.ProjectPointIntoCameraPixel(triangle[i])
   spacePoint = idealLightSource.CameraPixelIndicesArePointInMyPlane(idealCamera, pix[0], pix[1])
   corners.append(spacePoint)
  sum += TriangleSquaredError(corners, sideLength)
 return sum

def MakeTriangles(apexesAndAngles):
 triangles = []
 for apexAndAngle in apexesAndAngles:
  triangles.append(Triangle(sideLength, apexAndAngle))
 return triangles

# Make the scanner with small errors in its relative positions and angles; that is the scanner as it really is.

realWorld = ScannerPart()
realScanner = ScannerPart(offset = Vector3(0, -1701, 1001), parent = realWorld)
realLightSource = ScannerPart(offset = Vector3(0, 0, -251), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = realScanner, lightAngle = 2, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1)
realCamera = ScannerPart(offset = Vector3(0, 0, 251),  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = realScanner, lightAngle = -1, uPixels = 2464, vPixels = 3280, uMM =  17.64, vMM = 24.088543586543586, focalLength = 25.1) 
realLightSource.RotateU(-0.5*maths.pi)
realLightSource.RotateW(-0.5*maths.pi)
realCamera.RotateU(-0.5*maths.pi)
#Display(world, showLight = True, showCamera = True)

# Make an ideal scanner with no errors as a starting point.  This has to be corrected to correspond with the scanner above.

idealWorld = ScannerPart()
idealScanner = ScannerPart(offset = Vector3(0, -1700, 1000), parent = idealWorld)
idealLightSource = ScannerPart(offset = Vector3(0, 0, -250), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = idealScanner, lightAngle = 2, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1)
idealCamera = ScannerPart(offset = Vector3(0, 0, 250),  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = idealScanner, lightAngle = -1, uPixels = 2464, vPixels = 3280, uMM =  17.64, vMM = 24.088543586543586, focalLength = 25) 
idealLightSource.RotateU(-0.5*maths.pi)
idealLightSource.RotateW(-0.5*maths.pi)
idealCamera.RotateU(-0.5*maths.pi)


apexesAndAngles = []

apexesAndAngles.append( (Vector3(-400.0, -3500.0, 2000.0), 0.4) )
apexesAndAngles.append( (Vector3(470.0, -3600.0, 2000.0), 0.27) )
apexesAndAngles.append( (Vector3(-40.0, -3400.0, 2000.0), 0.6) )


triangles = MakeTriangles(apexesAndAngles)


print("Squared errors: ", TriangleErrors(triangles, realCamera, idealLightSource, idealCamera))


