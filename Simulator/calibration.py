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
 if printTriangles:
  print(" Original and reconstructed triangles: ")
 sum = 0.0
 for triangle in triangles:
  corners = []
  for i in range(3):
   pix = realCamera.ProjectPointIntoCameraPlane(triangle[i])
   spacePoint = idealLightSource.CameraPixelCoordinatesArePointInMyPlane(idealCamera, pix[0], pix[1])
   corners.append(spacePoint)
  if printTriangles:
   print("  ", triangle)
   print("  ", corners)
   print()
  sum += TriangleSquaredError(corners, sideLength)
 return sum



def MakeTriangles(apexesAndAngles):
 triangles = []
 for apexAndAngle in apexesAndAngles:
  triangles.append(Triangle(sideLength, apexAndAngle))
 return triangles

# Generate scanners at random, exploring the space of scanners, looking for a chance good fit

def ScatterGun(idealScanner, actualScanner, mean, sd, samples, reportProgress):
 minSE = 100000000000

 for i in range(samples):
  randomScanner = idealScanner.PurturbedCopy(mean, sd)

  tse = TriangleErrors(triangles, actualScanner, randomScanner, False)
  #print("Squared errors: ", tse)
  if tse < minSE and reportProgress:
   print("--------")
   #tse = TriangleErrors(triangles, actualScanner, realScanner, True)
   betterScanner = randomScanner
   minSE = tse
   print(minSE)
 return betterScanner

#*********************************************************************************************

seed(2)

world = ScannerPart()

# Make the scanner as we would like it to be.

idealScanner = Scanner(world, Vector3(0, -1700, 1000), Vector3(0, 0, -250), 2, Vector3(0, 0, 250), 2464, 3280, 17.64, 24.088543586543586, 25)
idealScanner.SetName("Ideal");

# Make the triangles in the scene

apexesAndAngles = []
apexesAndAngles.append( (Vector3(-400.0, -3500.0, 750.0), 0.4) )
apexesAndAngles.append( (Vector3(470.0, -3600.0, 750.0), 0.27) )
apexesAndAngles.append( (Vector3(-40.0, -3400.0, 750.0), 0.6) )
triangles = MakeTriangles(apexesAndAngles)

# make a scanner with small errors

realScanner = idealScanner.PurturbedCopy(3, 0.5)
realScanner.SetName("Purturbed");
#idealScanner.DebugOn()
#copiedScanner.DebugOn()

#tse = TriangleErrors(triangles, idealScanner, copiedScanner, True)
#print("Copied scanner RMS error: ", maths.sqrt(tse/(len(triangles)*3.0)))


bestScanner = ScatterGun(idealScanner, realScanner, 8.0, 0.5, 2000, True)
print("************")
tse = TriangleErrors(triangles, realScanner, bestScanner, True)
print("Best scanner RMS error (mm): ", maths.sqrt(tse/(len(triangles)*3.0)))
print("NB: the error is the error in side lengths, not corner positions (we don't \"know\" the latter).")


