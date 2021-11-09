# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from PIL import Image, ImageDraw, ImageFilter, ImageShow, ImageTk
import tkinter



#******************************************************************************************************

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

#*********************************************************************************************************

def OptimiseFromTriangleScans(scanner, triangleSideLength, triangleFileNames):
 print("Triangle optimisation - initial scanner:")
 print(str(scanner))
 pixelsAndAnglesJB = LoadPixelsAndAngles(triangleFileNames[0])
 recoveredRoom = scanner.ReconstructRoomFromPixelsAndAngles(pixelsAndAnglesJB)

 PlotRooms(recoveredRoom, None, "triscan.png", 0.5)
 return

 #TODO put some code in here...

 dataCount = len(pixelsAndAnglesJB[0])
 print("There are " + str(dataCount) + " triangles in the scan.")

 scanner = scanner.OptimiseTriangles(triangleSideLength, pixelsAndAnglesJB)
 print("Final scanner:")
 print(str(scanner))
 return scanner

#***************************************************************************************************************

def FakeTriangle(scanner, triangleSideLength):
 triangle = []
 angle = uniform(-0.5, 0.5)
 apex = Vector3(uniform(-500, 500), uniform(1000, 2000), 0)#uniform(-3, 3))
 x = triangleSideLength*maths.cos(angle)
 y = triangleSideLength*maths.sin(angle)
 v0 = Vector3(apex.x - x, apex.y + y, apex.z)
 v2 = Vector3(apex.x + y, apex.y + x, apex.z)
 triangle.append(scanner.PointInSpaceToPixel(v0))
 triangle.append(scanner.PointInSpaceToPixel(apex))
 triangle.append(scanner.PointInSpaceToPixel(v2))
 return triangle

def OptimiseFromSimulatedTriangleScan(scanner, triangleSideLength, triangleCount):
 print("Simulated triangle optimisation - initial scanner:")
 print(str(scanner))

 trianglePixels = []
 angles = []
 for t in range(triangleCount):
  trianglePixels.append(FakeTriangle(scanner, triangleSideLength))
  angles.append(0.0)
 pixelsAndAnglesJB = (trianglePixels, angles)

 dataCount = len(pixelsAndAnglesJB[0])
 print("There are " + str(dataCount) + " triangles in the scan.")

 scanner = scanner.MonteCarloTriangles(triangleSideLength, pixelsAndAnglesJB, 8, 3, 100)

 scanner = scanner.OptimiseTriangles(triangleSideLength, pixelsAndAnglesJB)
 print("Final scanner:")
 print(str(scanner))
 return scanner

#******************************************************************************************************************************************

def GetRoomFromJamesesScan(scanFile):
 room = []
 with open(scanFile) as scnFile:
  for line in scnFile:
   point = line.split()
   point = Vector3(float(point[0]), float(point[1]), float(point[2]))
   room.append(point)
 return room

def OptimiseFromRoomScan(scanner):
 pixelsAndAnglesJB = LoadPixelsAndAngles("RoomReaderScanDebug.txt")
 roomJB = GetRoomFromJamesesScan("RoomReaderScan.pts")
 print("Point optimisation - initial scanner:")
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

 print("Final scanner:")
 print(str(scanner))
 recoveredRoom = scanner.ReconstructRoomFromPixelsAndAngles(pixelsAndAnglesJB)

 PlotRooms(roomJB, recoveredRoom, None, 0.5)

 return scanner

#***************************************************************************************************************************************************

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

def RoomXY(room, fromBefore):
 if fromBefore is None:
  minX = sys.float_info.max
  minY = minX
  maxX = sys.float_info.min
  maxY = maxX
 else:
  m = fromBefore[0]
  minX = m[0]
  minY = m[1]
  m = fromBefore[1]
  maxX = m[0]
  maxY = m[1]
 for r in room:
  if r.x > maxX:
   maxX = r.x
  if r.x < minX:
   minX = r.x
  if r.y > maxY:
   maxY = r.y
  if r.y < minY:
   minY = r.y
 return [[minX, minY], [maxX, maxY]]

def PlotRooms(room1, room2, imageFile, scale):
 if room1 is not None:
  box = RoomXY(room1, None)
 if room2 is not None:
  if room1 is not None:
   box = RoomXY(room2, box)
  else:
   box = RoomXY(room2, None)
 min = box[0]
 max = box[1]
 xd = round(scale*(max[0] - min[0])) + 10
 yd = round(scale*(max[1] - min[1])) + 10
 print("Image size: [" + str(xd) + ", " + str(yd) + "]")
 picture = Picture(xd, yd)
 min[0] -= 5
 min[1] -= 5
 if room1 is not None:
  for r in room1:
   x = round(scale*(r.x - min[0]))
   y = round(scale*(r.y - min[1]))
   PlotPoint(picture, x, y, True)
 if room2 is not None:
  for r in room2:
   x = round(scale*(r.x - min[0]))
   y = round(scale*(r.y - min[1]))
   PlotPoint(picture, x, y, False)
 picture.Display()
 if imageFile is not None:
  picture.SavePicture(imageFile)

class Calibrate:
 def __init__(self, scanner, triangleSideLength, triangleFileNames, scale):
  self.box = None
  self.recoveredRooms = []
  self.scanner = scanner
  for name in triangleFileNames:
   pixelsAndAngles = LoadPixelsAndAngles(triangleFileNames[0])
   recoveredRoom = scanner.ReconstructRoomFromPixelsAndAngles(pixelsAndAngles)
   self.box = RoomXY(recoveredRoom, self.box)
   self.recoveredRooms.append(recoveredRoom)
  self.currentScan = -1;

  name = "Calibrate scanner"
  self.min = self.box[0]
  self.max = self.box[1]
  self.scale = scale
  self.window = tkinter.Tk(className=name)
  topCorner = self.Pixel(self.max[0], self.max[1])
  self.image = Image.new("RGB", (topCorner[0] + 10, topCorner[1] + 10))
  self.canvas = tkinter.Canvas(self.window, width=topCorner[0] + 160, height=topCorner[1] + 10)
  self.canvas.pack()
  self.image_tk = ImageTk.PhotoImage(self.image)
  self.image_on_canvas = self.canvas.create_image(self.image.size[0]//2, self.image.size[1]//2, image=self.image_tk)

  self.nextScan = tkinter.Button(text="next room", width=10, height=3, bg="grey", fg="white", command=self.NextScan)
  self.nextScan.pack()
  yPos = 10
  self.nextScan.place(x=self.image.size[0] + 20, y = yPos)

  self.quit = tkinter.Button(text="Quit", width=10, height=3, bg="grey", fg="white",command=self.Quit)
  self.quit.pack()
  yPos += 70
  self.quit.place(x=self.image.size[0] + 20, y=yPos)

  self.canvas.bind("<Button-1>", self.callback)

  self.window.mainloop()

 def Pixel(self, x, y):
  x1 = round(self.scale*(x - self.min[0])) + 5
  y1 = round(self.scale*(y - self.min[1])) + 5
  return (x1, y1)

 def PlotRoom(self, r):
  room = self.recoveredRooms[r]
  for r in room:
   pixel = self.Pixel(r.x, r.y)
   self.image.putpixel(pixel, (255,0,0))
  self.image_tk = ImageTk.PhotoImage(self.image)
  self.canvas.itemconfig(self.image_on_canvas, image = self.image_tk)

 def callback(self):
  x = 1

 def NextScan(self):
  self.currentScan += 1
  self.PlotRoom(self.currentScan)

 def Quit(self):
  quit()

#***************************************************************************************************************************************************

seed(7)
world = ScannerPart()
scanner = Scanner(world, scannerOffset = Vector3(0, 0, 0), lightOffset = Vector3(36, 0, 0), lightAng = 0.454, lightToeIn = 0,
		 cameraOffset = Vector3(-7.75, 0, 352.0), cameraToeIn = -20.32*maths.pi/180.0, uPix = 2464, vPix = 3280, uMM = 2.76, vMM = 3.68, focalLen = 8)

# From the optimiser. RMS = 2.52mm
parameters = [0, 0, 0, 36, 0, 0, 12.439261507779436, 85.07398479331971, 307.37393494542715, 8, 0.0, 1.0145322214287944, 0.011076482035381101, -7.119938967292683e-07, -2.7645354041538894e-06, -1.441521377175576, -0.15282795801825255, 1.4866218267968678, -9.38482980217259e-09, -2.8090019199566996e-09, -0.22434910788453966]
scanner.ImposeParameters(parameters)

sv = [6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
scanner.DefineSelectionVector(sv)

#scanner.CheckPoint(Vector3(-384.202311310053, 1847.839001639, 0), None, True)
#scanner = OptimiseFromSimulatedTriangleScan(scanner, 200, 1)
#OptimiseFromRoomScan(scanner)
triangleFileNames = []
triangleFileNames.append("RoomReaderScanDebug.txt")
#OptimiseFromTriangleScans(scanner, 500, triangleFileNames)

c = Calibrate(scanner, 500, triangleFileNames, 0.5)
