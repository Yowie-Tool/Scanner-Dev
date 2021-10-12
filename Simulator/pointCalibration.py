# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *



def LoadPixelsAndAngles(pixelFile):
 pixels = []
 angles = []
 with open(pixelFile) as pxFile:
  for line in pxFile:
   numbers = line.split()
   pixel = [float(numbers[1]), float(numbers[0])]
   pixels.append(pixel)
   angles.append(-float(numbers[2])*maths.pi/180.0)
 return (pixels, angles)

def GetRoomFromJamesesScan(scanFile):
 room = []
 with open(scanFile) as scnFile:
  for line in scnFile:
   point = line.split()
   point = Vector3(float(point[0]), float(point[1]), float(point[2]))
   room.append(point)
 return room


#*********************************************************************************************

seed(7)

world = ScannerPart()

scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0, cameraOffset =
		 Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)
'''
scanner = Scanner(world,
                  scannerOffset = Vector3(-863.612446147733, 2547.3621918921745, 119.50872958629937),
                  lightOffset = Vector3(-1351.1344535599703, -660.9864964136729, -122.71266770495758),
                  lightAng = 0.454,
                  lightToeIn = -0.2509728303244617,
                  cameraOffset = Vector3(519.652379926871, 3209.7700491595915, 598.1087874460901),
                  cameraToeIn = -0.32785573647400157,
                  uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68,
                  focalLen = 18.944401990122746)

#scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 23.15), lightAng = 0.454, lightToeIn = 0, cameraOffset =
#		 Vector3(-24.8, 0, 436.0), cameraToeIn = -10.94*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 25)

pixel = (0, 2573.0036496350367)
#pixel = (2464/2.0, 3280/2.0)
#pixel = (0, 0)
point = Vector3(-188.85944094399068, 1348.9119290579144, 0)
scanner.CheckPoint(point, pixel, True)
#scanner.CheckCornersAndMiddle()

points = [
 Vector3(-50, 1000, 0),
 Vector3(0, 1000, 0),
 Vector3(50, 1000, 0),
 Vector3(-50, 2000, 0),
 Vector3(0, 2000, 0),
 Vector3(50, 2000, 0)
]
for point in points:
 scanner.CheckPoint(point, None, True)
 print()
'''

sv = [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

scanner.DefineSelectionVector(sv)

print("Initial scanner:")
print(str(scanner))

roomJB = GetRoomFromJamesesScan("RoomReaderScan-JB.pts")
scanner.SelfCheck(roomJB)

pixelsAndAnglesJB = LoadPixelsAndAngles("RoomReaderScanCamera1-pixels.txt")
pixelsJB = pixelsAndAnglesJB[0]
anglesJB = pixelsAndAnglesJB[1]

dataCount = len(pixelsAndAnglesJB[0])
print("There are " + str(dataCount) + " pixels in the scan.")

coarse = 30
sample = int(dataCount/coarse)

room = []
pixels = []
angles = []
for s in range(0, len(pixelsJB), coarse):
 room.append(roomJB[s])
 pixels.append(pixelsJB[s])
 angles.append(anglesJB[s])

shortPixelsAndAnglesJB = (pixels, angles)

print("Sampled " + str(len(pixels)) + " pixels for the optimisation.")

betterScanner = scanner.MonteCarlo(room, shortPixelsAndAnglesJB, 8, 3, 100)

bestScanner = betterScanner.Optimise(room, shortPixelsAndAnglesJB)
print("Final scanner:")
print(str(bestScanner))


