# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from random import seed, random, gauss
from YowieScanner import *

r2 = maths.sqrt(2.0)
sideLength = 500

# Sum the squared errors in the lengths of a triangles sides compared with the ideal 45, 45, 90 triangle

def TriangleSquaredError(triangle, side):
 sum = 0.0
 s = maths.sqrt(triangle[1].Sub(triangle[0]).Length2()) - side
 print(s)
 sum += s*s
 s = maths.sqrt(triangle[2].Sub(triangle[1]).Length2()) - side
 print(s)
 sum += s*s
 s = maths.sqrt(triangle[0].Sub(triangle[2]).Length2()) - side*r2
 print(s)
 print()
 sum += s*s
 return sum

# Take triangles in space, find the pixels in the real camera of their corners, project them back in to the scene using
# the scanner that is to be calibrated, and sum the resulting squared errors.

def TriangleErrors(triangles, realLightSource, realCamera, idealLightSource, idealCamera):
 plane = realLightSource.GetLightPlane()
 planeDVector = plane[0].Multiply(-plane[1])
 sum = 0.0
 for triangle in triangles:
  corners = []
  for i in range(3):
   #v = triangle[i]
   vOffset = planeDVector.Sub(plane[0].Multiply(triangle[i].Dot(plane[0])))
   #print(vOffset)
   v = triangle[i].Add(vOffset)
   pix = realCamera.ProjectPointIntoCameraPlane(v)
   spacePoint = idealLightSource.CameraPixelIndicesArePointInMyPlane(idealCamera, pix[0], pix[1])
   corners.append(spacePoint)
  sum += TriangleSquaredError(corners, sideLength)
 return sum

# Uniform random number in [-1, 1]

def Random2():
 return random()*2.0 - 1.0

# Generate a random vector of mean length with standard deviation sd
# by rejection sampling in the unit ball

def RandomVector(mean, sd):
 s = 2.0
 while s > 1.0:
  x = Random2()
  y = Random2()
  z = Random2()
  s = x*x + y*y + z*z
 v = Vector3(x, y, z).Normalize().Multiply(gauss(mean, sd))
 return v

# Make a 45, 45, 90 triangle in space at angle apexAndAngle[1] to the X axis with the right angle at apexAndAngle[0]

def Triangle(apexAndAngle):
 triangle = []
 x = sideLength*maths.cos(apexAndAngle[1])
 y = sideLength*maths.sin(apexAndAngle[1])
 triangle.append(Vector3(apexAndAngle[0].x - x, apexAndAngle[0].y + y, apexAndAngle[0].z))
 triangle.append(apexAndAngle[0])
 triangle.append(Vector3(apexAndAngle[0].x + y, apexAndAngle[0].y + x, apexAndAngle[0].z))
 return triangle

def MakeTriangles(apexesAndAngles):
 triangles = []
 for apexAndAngle in apexesAndAngles:
  triangles.append(Triangle(apexAndAngle))
 return triangles

def MakeScanner(world, scannerOffset, lightOffset, lightAng, cameraOffset, uPix, vPix, uM, vM, focalLen, mean, sd):
 if mean < veryShort2:
  so = scannerOffset
  lo = lightOffset
  la = lightAng
  co = cameraOffset
  fl = focalLen
 else:
  so = scannerOffset.Add(RandomVector(mean, sd))
  lo = lightOffset.Add(RandomVector(mean, sd))
  la = lightAng # + gauss(0.0, sd)  #???
  co = cameraOffset.Add(RandomVector(mean, sd))
  fl = focalLen + gauss(0.0, sd)  #???
 scanner = ScannerPart(offset = so, parent = world)
 lightSource = ScannerPart(offset = lo, u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = scanner, lightAngle = la)
 camera = ScannerPart(offset = co,  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = scanner, uPixels = uPix, vPixels = vPix, uMM =  uM, vMM = vM, focalLength = fl)
 lightSource.RotateU(-0.5*maths.pi)
 lightSource.RotateW(-0.5*maths.pi)
 camera.RotateU(-0.5*maths.pi)
 return (scanner, lightSource, camera)

#*********************************************************************************************

seed(1)

world = ScannerPart()

# Make the scanner with small errors in its relative positions and angles; that is the scanner as it really is.

realWorld = ScannerPart()
realScanner = MakeScanner(world, Vector3(0, -1700, 1000), Vector3(0, 0, -250), 2, Vector3(0, 0, 250), 2464, 3280, 17.64, 24.088543586543586, 25, 0.0, 0.0)
realLightSource = realScanner[1]
realCamera = realScanner[2]

# Make an ideal scanner with no errors as a starting point.  This has to be corrected to correspond with the scanner above.

idealScanner = MakeScanner(world, Vector3(0, -1700, 1000), Vector3(0, 0, -250), 2, Vector3(0, 0, 250), 2464, 3280, 17.64, 24.088543586543586, 25, 0.0, 0.0)
idealLightSource = idealScanner[1]
idealCamera = idealScanner[2]

apexesAndAngles = []

apexesAndAngles.append( (Vector3(-400.0, -3500.0, 750.0), 0.4) )
apexesAndAngles.append( (Vector3(470.0, -3600.0, 750.0), 0.27) )
apexesAndAngles.append( (Vector3(-40.0, -3400.0, 750.0), 0.6) )


triangles = MakeTriangles(apexesAndAngles)


print("Squared errors: ", TriangleErrors(triangles, realLightSource, realCamera, idealLightSource, idealCamera))


