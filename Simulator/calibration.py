# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
import numpy as np
from scipy.optimize import minimize

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

# Construct the list of test triangles

def MakeTriangles(apexesAndAngles):
 triangles = []
 for apexAndAngle in apexesAndAngles:
  triangles.append(Triangle(sideLength, apexAndAngle))
 return triangles

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

def TriangleSquaredPositionError(realTriangle, reconstructedTriangle):
 sum = 0.0
 for t in range(3):
  sum += realTriangle[t].Sub(reconstructedTriangle[t]).Length2()
 return sum

# Take triangles in space, find the pixels in the real camera of their corners, project them back in to the scene using
# the scanner that is to be adjusted, so creating a set of reconstructed triangles.

def TriangleReconstructions(triangles, realScanner, ScannerToBeAdjusted, printTriangles):
 realCamera = realScanner.camera
 lightSourceToBeAdjusted = ScannerToBeAdjusted.lightSource
 cameraToBeAdjusted = ScannerToBeAdjusted.camera
 if printTriangles:
  print(" Original and reconstructed triangles: ")
 reconstructedTriangles = []
 for triangle in triangles:
  corners = []
  for i in range(3):
   pixel = realCamera.ProjectPointIntoCameraPlane(triangle[i])
   spacePoint = lightSourceToBeAdjusted.CameraPixelCoordinatesArePointInMyPlane(cameraToBeAdjusted, pixel)
   corners.append(spacePoint)
  if printTriangles:
   print("  ", triangle)
   print("  ", corners)
   print()
  reconstructedTriangles.append(corners)
 return reconstructedTriangles

# Find the mean squared errors in the triangle side lengths.

def TriangleMeanSquaredErrors(triangles, reconstructedTriangles):
 sum = 0.0
 for triangle in reconstructedTriangles:
  sum += TriangleSquaredError(triangle, sideLength)
 return sum/(len(triangles)*3.0)

# Find the mean squared errors in the triangle corner positions.
# NB there is no way we could do this in a real machine, as we cannot know the true positions of the triangles.

def TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles):
 sum = 0.0
 for t in range(len(reconstructedTriangles)):
  realTriangle = triangles[t]
  reconstructedTriangle = reconstructedTriangles[t]
  sum += TriangleSquaredPositionError(realTriangle, reconstructedTriangle)
 return sum/(len(triangles)*3.0)


def CostFunction(parameters, idealScanner, actualScanner, triangles):
 thisScanner = idealScanner.Copy()
 thisScanner.ImposeParameters(parameters)
 reconstructedTriangles = TriangleReconstructions(triangles, actualScanner, thisScanner, False)
 cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
 return cost

# Generate scanners at random, exploring the space of scanners, looking for a chance good fit
# Record the best and the second best, so we can estimate the gradient of the error function

def ScatterGun(idealScanner, actualScanner, triangles, mean, sd, samples, reportProgress):
 minSE = sys.float_info.max
 bestScanner = idealScanner.PerturbedCopy(mean, sd)
 secondBestScanner = bestScanner

 for i in range(samples):
  randomScanner = idealScanner.PerturbedCopy(mean, sd)
  tse = CostFunction(randomScanner.parameters, idealScanner, actualScanner, triangles)
  if tse < minSE:
   secondBestScanner = bestScanner
   bestScanner = randomScanner
   minSE = tse
   if reportProgress:
    print("--------")
    print(minSE)
 return (secondBestScanner, bestScanner)



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
apexesAndAngles.append( (Vector3(-200.0, -3100.0, 750.0), 1.1) )
apexesAndAngles.append( (Vector3(270.0, -3800.0, 750.0), 1.27) )
apexesAndAngles.append( (Vector3(-140.0, -3423.0, 750.0), 0.83) )
apexesAndAngles.append( (Vector3(-300.0, -2900.0, 750.0), 0.71) )
apexesAndAngles.append( (Vector3(170.0, -3812.0, 750.0), 1.02) )
apexesAndAngles.append( (Vector3(-80.0, -4400.0, 750.0), 0.54) )
triangles = MakeTriangles(apexesAndAngles)

print("Sanity check - run the ideal scanner against itself and check the errors are zero:")
reconstructedTriangles = TriangleReconstructions(triangles, idealScanner, idealScanner, False)
tse = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
print("Scanner versus itself RMS side length error (mm, should be 0.0): ", maths.sqrt(tse))
tpe = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
print("Position RMS error (mm, should be 0.0): ", maths.sqrt(tpe))

# make a scanner with small errors

realScanner = idealScanner.PerturbedCopy(3, 0.5)
realScanner.SetName("Purturbed");

# Optimisation

print("************")
parameters = copy.deepcopy(idealScanner.parameters)
res = minimize(CostFunction, x0 = parameters, args = (idealScanner, realScanner, triangles,))
#print(res)
print("************")
#print(res.x)
#print(realScanner.parameters)
finalScanner = idealScanner.Copy()
finalScanner.ImposeParameters(res.x)
reconstructedTriangles = TriangleReconstructions(triangles, realScanner, finalScanner, True)
cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
print("Scanner RMS side length error (mm): ", maths.sqrt(cost))
tpe = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
print("Position RMS error (mm): ", maths.sqrt(tpe))




'''
# Run 2000 purturbed copies of the ideal scanner against it to find a good(ish) match

bestScanners = ScatterGun(idealScanner, realScanner, triangles, 8.0, 0.5, 2000, True)
print("************")
reconstructedTriangles = TriangleReconstructions(triangles, realScanner, bestScanners[1], True)
tse = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
print("Best scanner RMS side-length error (mm): ", maths.sqrt(tse))
tpe = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
print("Position RMS error (mm; couldn't be calculated in real life)", maths.sqrt(tpe))
'''

