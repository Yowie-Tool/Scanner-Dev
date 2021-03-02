# Simulation of scanner calibration

from YowieScanner import *

r2 = maths.sqrt(2.0)
sideLength = 500

def Triangle(side, angle, apex):
 x = side*maths.cos(angle)
 y = side*maths.sin(angle)
 p0 = Vector3(apex.x - x, apex.y + y, apex.z)
 p2 = Vector3(apex.x + y, apex.y + x, apex.z)
 return (p0, apex, p2)

def TriangleSquaredError(t0, side):
 sum = 0.0
 for i in range(3): 
  if i is not 2:
   s = maths.sqrt(t0[i].Sub(t0[(i+1)%3]).Length2()) - side
  else:
   s = maths.sqrt(t0[i].Sub(t0[(i+1)%3]).Length2()) - side*r2
  sum += s*s
 return sum

def TriangleError(triangle, realCamera, idealLightSource, idealCamera):
 corners = []
 for i in range(3):
  pix = realCamera.ProjectPointIntoCameraPixel(triangle[i])
  spacePoint = idealLightSource.CameraPixelIndicesArePointInMyPlane(idealCamera, pix[0], pix[1])
  corners.append(spacePoint)
 e = TriangleSquaredError(corners, sideLength)
 return e

# Make the scanner

realWorld = ScannerPart()
realScanner = ScannerPart(offset = Vector3(0, -1701, 1001), parent = realWorld)
realLightSource = ScannerPart(offset = Vector3(0, 0, -251), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = realScanner, lightAngle = 2, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1)
realCamera = ScannerPart(offset = Vector3(0, 0, 251),  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = realScanner, lightAngle = -1, uPixels = 2464, vPixels = 3280, uMM =  17.64, vMM = 24.088543586543586, focalLength = 25.1) 
realLightSource.RotateU(-0.5*maths.pi)
realLightSource.RotateW(-0.5*maths.pi)
realCamera.RotateU(-0.5*maths.pi)
#Display(world, showLight = True, showCamera = True)

idealWorld = ScannerPart()
idealScanner = ScannerPart(offset = Vector3(0, -1700, 1000), parent = idealWorld)
idealLightSource = ScannerPart(offset = Vector3(0, 0, -250), u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = idealScanner, lightAngle = 2, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1)
idealCamera = ScannerPart(offset = Vector3(0, 0, 250),  u = Vector3(1, 0, 0), v = Vector3(0, 1, 0), w = Vector3(0, 0, 1), parent = idealScanner, lightAngle = -1, uPixels = 2464, vPixels = 3280, uMM =  17.64, vMM = 24.088543586543586, focalLength = 25) 
idealLightSource.RotateU(-0.5*maths.pi)
idealLightSource.RotateW(-0.5*maths.pi)
idealCamera.RotateU(-0.5*maths.pi)




p0 = Vector3(-400.0, -3500.0, 2000.0)
triangle = Triangle(sideLength, 0.4, p0)
print("Test = 0: ", TriangleSquaredError(triangle, sideLength))
print("Squared error: ", TriangleError(triangle, realCamera, idealLightSource, idealCamera))
