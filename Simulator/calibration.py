# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *

r2 = maths.sqrt(2.0)
sideLength = 500

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
 s = maths.sqrt(triangle[1].Sub(triangle[0]).Length2()) - side
 sum += s*s
 s = maths.sqrt(triangle[2].Sub(triangle[1]).Length2()) - side
 sum += s*s
 s = maths.sqrt(triangle[0].Sub(triangle[2]).Length2()) - side*r2
 sum += s*s
 return sum

# Take triangles in space, find the pixels in the real camera of their corners, project them back in to the scene using
# the scanner that is to be calibrated, and sum the resulting squared errors.

def TriangleErrors(triangles, realScanner, idealScanner, printTriangles):
 realLightSource = realScanner.lightSource
 realCamera = realScanner.camera
 idealLightSource = idealScanner.lightSource
 idealCamera = idealScanner.camera
 sum = 0.0
 for triangle in triangles:
  corners = []
  for i in range(3):
   pix = realCamera.ProjectPointIntoCameraPlane(triangle[i])
   spacePoint = idealLightSource.CameraPixelCoordinatesArePointInMyPlane(idealCamera, pix[0], pix[1])
   corners.append(spacePoint)
  if printTriangles:
   print(triangle)
   print(corners)
   print()
  sum += TriangleSquaredError(corners, sideLength)
 return sum



def MakeTriangles(apexesAndAngles):
 triangles = []
 for apexAndAngle in apexesAndAngles:
  triangles.append(Triangle(sideLength, apexAndAngle))
 return triangles



#*********************************************************************************************

seed(2)

world = ScannerPart()

# Make the scanner with small errors in its relative positions and angles; that is the scanner as it really is.

realScanner = Scanner(world, Vector3(0, -1700, 1000), Vector3(0, 0, -250), 2, Vector3(0, 0, 250), 2464, 3280, 17.64, 24.088543586543586, 25)

# Make the triangles in the scene

apexesAndAngles = []
apexesAndAngles.append( (Vector3(-400.0, -3500.0, 2000.0), 0.4) )
apexesAndAngles.append( (Vector3(470.0, -3600.0, 2000.0), 0.27) )
apexesAndAngles.append( (Vector3(-40.0, -3400.0, 2000.0), 0.6) )
triangles = MakeTriangles(apexesAndAngles)

# Make an ideal scanner with no errors as a starting point.  This has to be corrected to correspond with the scanner above.

minSE = 100000000000

for i in range(2000):
 idealScanner = realScanner.PurturbedCopy(8.0, 0.5)

 tse = TriangleErrors(triangles, realScanner, idealScanner, False)
 #print("Squared errors: ", tse)
 if tse < minSE:
  print("--------")
  tse = TriangleErrors(triangles, realScanner, idealScanner, True)
  betterScanner = idealScanner
  minSE = tse

print("Min error: ", minSE)
print("Best scanner error: ", TriangleErrors(triangles, realScanner, betterScanner, True))


