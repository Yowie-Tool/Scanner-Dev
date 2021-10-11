# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from scipy.optimize import minimize
import numpy

r2 = maths.sqrt(2.0)
sideLength = 500
a4Paper = 297.0

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
   pixel = realCamera.ProjectPointIntoFractionalCameraPixel(triangle[i])
   spacePoint = lightSourceToBeAdjusted.CameraPixelIsPointInMyPlane(cameraToBeAdjusted, pixel)
   corners.append(spacePoint)
  if printTriangles:
   print("  ", str(triangle))
   print("  ", str(corners))
   print()
  reconstructedTriangles.append(corners)
 return reconstructedTriangles

# Take two points in space - the edges of a piece of A4 paper, find the pixels in the real camera of their corners,
# project them back in to the scene using
# the scanner that is to be adjusted, so creating a set of reconstructed triangles.

def A4Reconstructions(a4Points, realScanner, ScannerToBeAdjusted):
 realCamera = realScanner.camera
 lightSourceToBeAdjusted = ScannerToBeAdjusted.lightSource
 cameraToBeAdjusted = ScannerToBeAdjusted.camera
 reconstructedA4Points = []
 for point in a4Points:
  pixel = realCamera.ProjectPointIntoFractionalCameraPixel(point)
  spacePoint = lightSourceToBeAdjusted.CameraPixelIsPointInMyPlane(cameraToBeAdjusted, pixel)
  reconstructedA4Points.append(spacePoint)
 return reconstructedA4Points

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

# Find the mean squared errors in the A4 edge positions.

def A4MeanSquaredPositionErrors(a4Points, reconstructedA4Points):
 sum = 0.0
 for p in range(2):
  realPoint = a4Points[p]
  reconstructedPoint = reconstructedA4Points[p]
  sum += realPoint.Sub(reconstructedPoint).Length2()
 return sum*0.5


def CostFunction(parameters, idealScanner, actualScanner, triangles, sides):
 thisScanner = idealScanner.Copy()
 thisScanner.ImposeParameters(parameters)
 reconstructedTriangles = TriangleReconstructions(triangles, actualScanner, thisScanner, False)
 if sides:
  cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
 else:
  cost = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
 return cost

# Generate scanners at random, exploring the space of scanners, looking for a chance good fit

def ScatterGun(idealScanner, actualScanner, triangles, mean, sd, samples, reportProgress, sides):
 minCost = sys.float_info.max
 bestScanner = idealScanner.PerturbedCopy(mean, sd)

 for i in range(samples):
  randomScanner = idealScanner.PerturbedCopy(mean, sd)
  cost = CostFunction(randomScanner.parameters, idealScanner, actualScanner, triangles, sides)
  if cost < minCost:
   bestScanner = randomScanner
   minCost = cost
   if reportProgress:
    print("--------")
    print(minCost)
 return bestScanner

# Generate a scanner with random errors then try to find out what they are and make a scanner model that fits it

def Optimise(idealScanner, triangles, sides, mean, sd):
 # make a scanner with small errors

 realScanner = idealScanner.PerturbedCopy(mean, sd)
 realScanner.SetName("Purturbed")
 print("Purturbed scanner: \n" + str(realScanner))

 print("First stage - scattergun to find a good (if random) starting point for the optimisation")
 bestScanner = ScatterGun(idealScanner, realScanner, triangles, 8.0, 0.5, 30, True, sides)
 reconstructedTriangles = TriangleReconstructions(triangles, realScanner, bestScanner, False)
 cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
 print("Best scatter scanner RMS side-length error (mm): ", maths.sqrt(cost))
 cost = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
 print("Scatter scanner triangle corner position RMS error (mm)", maths.sqrt(cost))

 print("Second stage - whatever the scipy minimise() function does (presumably gradient descent)...")
 minResult = minimize(CostFunction, x0 = bestScanner.parameters, args = (idealScanner, realScanner, triangles, sides,))
 finalScanner = idealScanner.Copy()
 finalScanner.ImposeParameters(minResult.x)
 reconstructedTriangles = TriangleReconstructions(triangles, realScanner, finalScanner, False)
 cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
 print("Scanner RMS side length error (mm): ", maths.sqrt(cost))
 cost = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
 print("Position RMS error (mm): ", maths.sqrt(cost))
 print("RMS difference between the actual scanner and the fitted model of it: ", realScanner.ParameterRMSDifference(finalScanner))
 return finalScanner

# Generate a series of scanners with increasing errors and print how those errors correlate
# with a measurement of the two edges of a piece of A4 paper.

def FieldTest(idealScanner, triangles, a4Points):
 for mean in numpy.arange(0.0,0.5,0.01):
  sd = mean/6.0
  cSum = 0.0
  aSum = 0.0
  #for tests in range(0, 10):
  randomScanner = idealScanner.PerturbedCopy(mean, sd)
  reconstructedTriangles = TriangleReconstructions(triangles, randomScanner, idealScanner, False)
  cSum += TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
  reconstructedA4Points = A4Reconstructions(a4Points, randomScanner, idealScanner)
  aSum += A4MeanSquaredPositionErrors(a4Points, reconstructedA4Points)
  #cSum = cSum/10.0
  #aSum = aSum/10.0
  print(maths.sqrt(aSum), maths.sqrt(cSum))

#*********************************************************************************************
#def __init__(self, world, scannerOffset, lightOffset, lightAng, cameraOffset, uPix, vPix, uM, vM, focalLen)

seed(7)

world = ScannerPart()

# Make the scanner as we would like it to be.

#idealScanner = Scanner(world, scannerOffset = Vector3(0, -1700, 1000), lightOffset = Vector3(0, 0, -250), lightAng = 2, lightToeIn = 0, cameraOffset =
#		 Vector3(0, 0, 250), cameraToeIn = 0, uPix = 2464, vPix = 3280, uMM = 17.64, vMM = 24.088543586543586, focalLen = 25)

idealScanner = Scanner(world, scannerOffset = Vector3(0, -1700, 1000), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0, cameraOffset =
		 Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

idealScanner.SetName("Ideal")

print("Initial scanner: \n" + str(idealScanner))

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

# Two edges of a piece of A4 paper 2m in front of the scanner

a4Points = []
a4Points.append(Vector3(-a4Paper/2.0, -3700.0, 750.0))
a4Points.append(Vector3(a4Paper/2.0, -3700.0, 750.0))

print("Sanity check - run the ideal scanner against itself and check the errors are zero:")
reconstructedTriangles = TriangleReconstructions(triangles, idealScanner, idealScanner, False)
cost = TriangleMeanSquaredErrors(triangles, reconstructedTriangles)
print("Scanner versus itself RMS side length error (mm, should be 0.0): ", maths.sqrt(cost))
cost = TriangleMeanSquaredPositionErrors(triangles, reconstructedTriangles)
print("Position RMS error (mm, should be 0.0): ", maths.sqrt(cost))

# Set this true to optimise against triangle side lengths
# or False to optimise against the actual triangle corner positions
# The latter would be physically much more difficult to do.

sides = True

finalScanner = Optimise(idealScanner, triangles, sides, 3, 0.5)

#FieldTest(idealScanner, triangles, a4Points)

print("Final scanner: \n" + str(finalScanner))



