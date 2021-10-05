# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from scipy.optimize import minimize

# Generate scanners at random, exploring the space of scanners, looking for a chance good fit

def ScatterGun(startScanner, room, pixels, angles, mean, sd, samples, reportProgress):
 bestScanner = startScanner.Copy()
 recoveredRoom = ReconstructRoomFromPixels(pixels, angles, bestScanner)
 minCost = MSRoomDifferences(room, recoveredRoom)
 if reportProgress:
  print("Intitial MS error: " + str(minCost))

 for i in range(samples):
  randomScanner = startScanner.PerturbedCopy(mean, sd)
  recoveredRoom = ReconstructRoomFromPixels(pixels, angles, randomScanner)
  cost = MSRoomDifferences(room, recoveredRoom)
  if cost < minCost:
   bestScanner = randomScanner
   minCost = cost
   if reportProgress:
    print("--------")
    print(minCost)
 return (bestScanner, minCost)

def CostFunction(parameters, scanner, room, pixels, angles):
 thisScanner = scanner.Copy()
 thisScanner.ImposeParameters(parameters)
 recoveredRoom = ReconstructRoomFromPixels(pixels, angles, thisScanner)
 return MSRoomDifferences(room, recoveredRoom)

count = 0
scannerCopy = None
report = False
rm = None
px = None
ag = None

def Progress(parameters):
 global count, scannerCopy, report, rm, px, ag
 if not report:
  return
 count += 1
 if not count % 10 == 0:
  return
 scannerCopy.ImposeParameters(parameters)
 cost = CostFunction(scannerCopy.parameters, scannerCopy, rm, px, ag)
 print("Scanner MS error (mm^2): " + str(cost) + " after " + str(count) + " iterations.")

# Generate a scanner with random errors then try to find out what they are and make a scanner model that fits it

def Optimise(startScanner, room, pixels, angles, mean, sd, samples, reportProgress):
 global count, scannerCopy, report, rm, px, ag
 report = reportProgress
 rm = room
 px = pixels
 ag = angles
 if reportProgress:
  print("First stage - scattergun to find a good (if random) starting point for the optimisation")
 scatterResult = ScatterGun(startScanner, room, pixels, angles, mean, sd, samples, reportProgress)
 bestScanner = scatterResult[0]
 scannerCopy = bestScanner.Copy()

 if reportProgress:
  print("MS error after scattergun: " + str(scatterResult[1]))
  print("Second stage - scipy.optimize.minimize using Broyden–Fletcher–Goldfarb–Shanno algorithm ...")
 minResult = minimize(CostFunction, x0 = bestScanner.parameters, args = (bestScanner, room, pixels, angles), callback = Progress)
 finalScanner = bestScanner.Copy()
 finalScanner.ImposeParameters(minResult.x)
 cost = CostFunction(finalScanner.parameters, finalScanner, room, pixels)
 if reportProgress:
  print("Final scanner RMS error (mm): ", maths.sqrt(cost))
 return finalScanner


def LoadPixels(pixelFile):
 pixels = []
 angles = []
 with open(pixelFile) as pxFile:
  for line in pxFile:
   numbers = line.split()
   pixel = [float(numbers[1]), float(numbers[0])]
   pixels.append(pixel)
   angles.append(float(numbers[2]))
 return (pixels, angles)

def ReconstructRoomFromPixels(pixels, angles, scanner):
 room = []
 for p in range(len(pixels)):
   pixel = pixels[p]
   angle = angles[p]
   scanner.Turn(angle)
   room.append(scanner.PixelToPointInSpace(pixel))
 return room

def GetRoomFromJamesesScan(scanFile):
 room = []
 with open(scanFile) as scnFile:
  for line in scnFile:
   point = line.split()
   point = Vector3(float(point[0]), float(point[1]), float(point[2]))
   room.append(point)
 return room

def MSRoomDifferences(room1, room2):
 if not len(room1) == len(room2):
  print("Room point lists are not equal length! " + str(len(room1)) + ", " + str(len(room2)))
  return 0
 sum = 0.0
 for r in range(len(room1)):
  r1 = room1[r]
  r2 = room2[r]
  rd = r1.Sub(r2)
  sum += rd.Length2()
 sum = sum/len(room1)
 return sum



#*********************************************************************************************

seed(7)

world = ScannerPart()

scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0, cameraOffset =
		 Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

#scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 23.15), lightAng = 0.454, lightToeIn = 0, cameraOffset =
#		 Vector3(-24.8, 0, 436.0), cameraToeIn = -10.94*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 25)

pixel = (2889.0227882037534, 0.0)
# point -230.4857937468226 1622.395309211286 0
point = Vector3(-230.4857937468226, 1622.395309211286, 0)
'''points = [
 Vector3(-50, 1000, 0),
 Vector3(0, 1000, 0),
 Vector3(50, 1000, 0),
 Vector3(-50, 2000, 0),
 Vector3(0, 2000, 0),
 Vector3(50, 2000, 0)
]'''
#for point in points:
scanner.CheckPoint(point, pixel, True)
print()

'''
print("Initial scanner:")
print(str(scanner))

roomJB = GetRoomFromJamesesScan("RoomReaderScan-JB.pts")
scanner.SelfCheck(roomJB)

dataJB = LoadPixels("RoomReaderScanCamera1-pixels.txt")
pixelsJB = dataJB[0]
anglesJB = dataJB[1]

print("There are " + str(len(pixelsJB)) + " pixels in the scan.")

coarse = 30
sample = int(len(pixelsJB)/coarse)

room = []
pixels = []
angles = []
for s in range(0, len(pixelsJB), coarse):
 room.append(roomJB[s])
 pixels.append(pixelsJB[s])
 angles.append(anglesJB[s])

print("Sampled " + str(len(pixels)) + " pixels for the optimisation.")

bestScanner = Optimise(scanner, room, pixels, angles, 5, 2, 20, True)
print("Final scanner:")
print(str(bestScanner))

'''
