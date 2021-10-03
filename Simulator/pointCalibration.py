# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from scipy.optimize import minimize

# Generate scanners at random, exploring the space of scanners, looking for a chance good fit

def ScatterGun(startScanner, room, pixels, mean, sd, samples, reportProgress):
 bestScanner = startScanner.Copy()
 recoveredRoom = ReconstructRoomFromPixels(pixels, bestScanner)
 minCost = MSRoomDifferences(room, recoveredRoom)
 if reportProgress:
  print("Intitial MS error: " + str(minCost))

 for i in range(samples):
  randomScanner = startScanner.PerturbedCopy(mean, sd)
  recoveredRoom = ReconstructRoomFromPixels(pixels, randomScanner)
  cost = MSRoomDifferences(room, recoveredRoom)
  if cost < minCost:
   bestScanner = randomScanner
   minCost = cost
   if reportProgress:
    print("--------")
    print(minCost)
 return (bestScanner, minCost)

def CostFunction(parameters, scanner, room, pixels):
 thisScanner = scanner.Copy()
 thisScanner.ImposeParameters(parameters)
 recoveredRoom = ReconstructRoomFromPixels(pixels, thisScanner)
 return MSRoomDifferences(room, recoveredRoom)

count = 0
scannerCopy = None
report = False
rm = None
px = None

def Progress(parameters):
 global count, scannerCopy, report, rm, px
 if not report:
  return
 count += 1
 if not count % 10 == 0:
  return
 scannerCopy.ImposeParameters(parameters)
 cost = CostFunction(scannerCopy.parameters, scannerCopy, rm, px)
 print("Scanner MS error (mm^2): " + str(cost) + " after " + str(count) + " iterations.")

# Generate a scanner with random errors then try to find out what they are and make a scanner model that fits it

def Optimise(startScanner, room, pixels, mean, sd, samples, reportProgress):
 global count, scannerCopy, report, rm, px
 report = reportProgress
 rm = room
 px = pixels
 if reportProgress:
  print("First stage - scattergun to find a good (if random) starting point for the optimisation")
 scatterResult = ScatterGun(startScanner, room, pixels, mean, sd, samples, reportProgress)
 bestScanner = scatterResult[0]
 scannerCopy = bestScanner.Copy()

 if reportProgress:
  print("MS error after scattergun: " + str(scatterResult[1]))
  print("Second stage - scipy.optimize.minimize using Broyden–Fletcher–Goldfarb–Shanno algorithm ...")
 minResult = minimize(CostFunction, x0 = bestScanner.parameters, args = (bestScanner, room, pixels,), callback = Progress)
 finalScanner = bestScanner.Copy()
 finalScanner.ImposeParameters(minResult.x)
 cost = CostFunction(finalScanner.parameters, finalScanner, room, pixels)
 if reportProgress:
  print("Final scanner RMS error (mm): ", maths.sqrt(cost))
 return finalScanner


def LoadPixels(pixelFile):
 pixels = []
 with open(pixelFile) as pxFile:
  for line in pxFile:
   pixel = line.split()
   pixel = [float(pixel[1]), float(pixel[2])]
   pixels.append(pixel)
 return pixels

def ReconstructRoomFromPixels(pixels, scanner):
 room = []
 for p in pixels:
   room.append(scanner.PixelToPointInSpace(p))
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
#def __init__(self, world, scannerOffset, lightOffset, lightAng, cameraOffset, uPix, vPix, uM, vM, focalLen)

seed(7)

world = ScannerPart()


scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 23.15), lightAng = 0.454, lightToeIn = 0, cameraOffset =
		 Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

#InitialRealScanner = Scanner(self.world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 23.15), lightAng = 0.454, lightToeIn = 0, cameraOffset =
#		 Vector3(-24.8, 0, 436.0), cameraToeIn = -10.94*math.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 25)

roomJB = GetRoomFromJamesesScan("RoomReaderScan-JB.pts")
pixelsJB = LoadPixels("RoomReaderScanCamera1-pixels.txt")

coarse = 30
sample = int(len(pixelsJB)/coarse)

room = []
pixels = []
for s in range(0, len(pixelsJB), coarse):
 room.append(roomJB[s])
 pixels.append(pixelsJB[s])

bestScanner = Optimise(scanner, room, pixels, 5, 2, 20, True)




