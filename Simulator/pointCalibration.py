# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from PIL import Image, ImageDraw, ImageFilter, ImageShow


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Interface to the graphics library (to allow several to be easily substituted)

class Picture:
# New image x by y pixels

 def __init__(self, x, y):
  self.picture = Image.new("RGB", (x, y))

 # The drawable frame of an image

 def Display(self):
  return ImageShow.show(self.picture)

 # Draw a straight line from p0 to p1

 def DrawLine(self, p0, p1, shade):
  self.picture.line([p0, p1], shade, 1)

# Set a single pixel to colour shade

 def SetPixel(self, x, y, shade):
  self.picture.putpixel((x, y), shade)

# Grow the image by width f

 def Filter(self, f):
  return self.picture.filter(ImageFilter.MaxFilter(f))

# Save the image in a file

 def SavePicture(self, fileName):
  self.picture.save(fileName)

def PlotPoint(picture, x, y, original):
 if original:
  picture.SetPixel(x, y, (0,255,0))
  #picture.SetPixel(x, y-1, (0,255,0))
  #picture.SetPixel(x-1, y-1, (0,255,0))
  #picture.SetPixel(x+1, y, (0,255,0))
 else:
  picture.SetPixel(x, y, (255,0,0))
  #picture.SetPixel(x, y+1, (255,0,0))
  #picture.SetPixel(x-1, y+1, (255,0,0))
  #picture.SetPixel(x-1, y, (255,0,0))

def PlotRooms(room1, room2, imageFile, scale):
 minX = sys.float_info.max
 minY = minX
 maxX = sys.float_info.min
 maxY = maxX
 for r in room1:
  if r.x > maxX:
   maxX = r.x
  if r.x < minX:
   minX = r.x
  if r.y > maxY:
   maxY = r.y
  if r.y < minY:
   minY = r.y
 for r in room2:
  if r.x > maxX:
   maxX = r.x
  if r.x < minX:
   minX = r.x
  if r.y > maxY:
   maxY = r.y
  if r.y < minY:
   minY = r.y

 xd = round(scale*(maxX - minX)) + 10
 yd = round(scale*(maxY - minY)) + 10
 print("Image size: [" + str(xd) + ", " + str(yd) + "]")
 picture = Picture(xd, yd)
 minX -= 5
 minY -= 5
 for r in room1:
  x = round(scale*(r.x - minX))
  y = round(scale*(r.y - minY))
  PlotPoint(picture, x, y, True)
 for r in room2:
  x = round(scale*(r.x - minX))
  y = round(scale*(r.y - minY))
  PlotPoint(picture, x, y, False)
 picture.Display()
 if imageFile is not None:
  picture.SavePicture(imageFile)


#***************************************************************************************************************

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

def FakeTriangle(scanner, triangleSideLength):
 triangle = []
 angle = uniform(-0.5, 0.5)
 apex = Vector3(uniform(-500, 500), uniform(1000, 2000), uniform(-3, 3))
 x = triangleSideLength*maths.cos(angle)
 y = triangleSideLength*maths.sin(angle)
 triangle.append(scanner.PointInSpaceToPixel(Vector3(apex.x - x, apex.y + y, apex.z)))
 triangle.append(scanner.PointInSpaceToPixel(apex))
 triangle.append(scanner.PointInSpaceToPixel(Vector3(apex.x + y, apex.y + x, apex.z)))
 return triangle

def DoTriangleOptimisation(pixelsAndAnglesJB, triangleSideLength):

 seed(7)

 world = ScannerPart()

 scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0,
		 cameraOffset = Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

 sv = [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

 scanner.DefineSelectionVector(sv)

 print("Initial scanner:")
 print(str(scanner))

 if pixelsAndAnglesJB is None:
  trianglePixels = []
  angles = []
  for t in range(6):
   trianglePixels.append(FakeTriangle(scanner, triangleSideLength))
   angles.append(0.0)
  pixelsAndAnglesJB = (trianglePixels, angles)

 dataCount = len(pixelsAndAnglesJB[0])
 print("There are " + str(dataCount) + " triangles in the scan.")

 scanner = scanner.MonteCarloTriangles(triangleSideLength, pixelsAndAnglesJB, 8, 3, 100)

 scanner = scanner.OptimiseTriangles(triangleSideLength, pixelsAndAnglesJB)

 return scanner

#******************************************************************************************************************************************

def DoPointsOptimisation(pixelsAndAnglesJB, roomJB):
 seed(7)

 world = ScannerPart()

 scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0,
		 cameraOffset = Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

 sv = [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

 scanner.DefineSelectionVector(sv)

 print("Initial scanner:")
 print(str(scanner))

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

 scanner = scanner.MonteCarloPoints(room, shortPixelsAndAnglesJB, 8, 3, 100)

 scanner = scanner.OptimisePoints(room, shortPixelsAndAnglesJB)

 return scanner
#*********************************************************************************************


'''
parameters = [0, 0, 0, 36, 0, 0, 36.29020647040032, -64.73034918263649, 347.2584403909511, 9.132270456355052, 0.0, 2.536641779027073, 0.09830280745876545, 0.0014337786420365016, 0.007458111749965841, 3.344304399002978, 6.270129696264745, 1.5628220387349634, 6.283153237497993, 6.283152870577741, 6.221876183673617]

scanner.ImposeParameters(parameters)
roomAB = GetRoomFromJamesesScan("RoomReaderScanAB.pts")
'''
def Room():
 pixelsAndAnglesJB = LoadPixelsAndAngles("RoomReaderScanDebug.txt")
 roomJB = GetRoomFromJamesesScan("RoomReaderScan.pts")
 scanner = DoPointsOptimisation(pixelsAndAnglesJB, roomJB)

 print("Final scanner:")
 print(str(scanner))
 recoveredRoom = scanner.ReconstructRoomFromPixelsAndAngles(pixelsAndAnglesJB)

 PlotRooms(roomJB, recoveredRoom, None, 0.5)

def Triangles():
 scanner = DoTriangleOptimisation(None, 200)
 print("Final scanner:")
 print(str(scanner))


Triangles()
#Room()
