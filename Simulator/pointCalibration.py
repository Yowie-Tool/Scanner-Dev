# Simulation of scanner calibration
# Adrian Bowyer
# RepRap Ltd
# https://reprapltd.com
# 2 March 2021

from YowieScanner import *
from PIL import Image, ImageDraw, ImageFilter, ImageShow, ImageTk
import tkinter
from scipy.spatial import ConvexHull


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

# Find the minimum enclosing rectangle round the room

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
 def __init__(self, scanner, triangleSideLength, triangleFileNames, imageScale, sample):
  self.box = None
  self.recoveredRooms = []
  self.scanner = scanner
  self.sample = sample
  self.triangleSideLength = triangleSideLength
  for name in triangleFileNames:
   pixelsAndAngles = LoadPixelsAndAngles(triangleFileNames[0])
   recoveredRoom = scanner.ReconstructRoomFromPixelsAndAngles(pixelsAndAngles)
   self.box = RoomXY(recoveredRoom, self.box)
   self.recoveredRooms.append(recoveredRoom)
  self.currentScan = -1;

  name = "Calibrate scanner"
  self.min = self.box[0]
  self.max = self.box[1]
  self.imageScale = imageScale
  self.window = tkinter.Tk(className=name)
  topCorner = self.PointToPixel((self.max[0], self.max[1]))
  self.image = Image.new("RGB", (topCorner[0] + 10, topCorner[1] + 10))
  self.draw = ImageDraw.Draw(self.image)
  self.canvas = tkinter.Canvas(self.window, width=topCorner[0] + 160, height=topCorner[1] + 10)
  self.canvas.pack()
  self.image_tk = ImageTk.PhotoImage(self.image)
  self.image_on_canvas = self.canvas.create_image(self.image.size[0]//2, self.image.size[1]//2, image=self.image_tk)

  self.canvas.bind("<ButtonPress-1>", self.OnButtonPress)
  self.canvas.bind("<B1-Motion>", self.OnMovePressing)
  self.canvas.bind("<ButtonRelease-1>", self.OnButtonRelease)

  self.rect = None

  self.rectangleStartX = None
  self.rectangleStartY = None

  self.nextScan = tkinter.Button(text="next scan", width=10, height=3, bg="grey", fg="white", command=self.NextScan)
  self.nextScan.pack()
  yPos = 10
  self.nextScan.place(x=self.image.size[0] + 20, y = yPos)

  self.quit = tkinter.Button(text="Quit", width=10, height=3, bg="grey", fg="white",command=self.Quit)
  self.quit.pack()
  yPos += 70
  self.quit.place(x=self.image.size[0] + 20, y=yPos)

  self.window.mainloop()

 def PointToPixel(self, point):
  x1 = round(self.imageScale * (point[0] - self.min[0])) + 5
  y1 = round(self.imageScale * (point[1] - self.min[1])) + 5
  return (x1, y1)

 def PixelToPoint(self, pixel):
  x1 = self.min[0] + (pixel[0] - 5)/self.imageScale
  y1 = self.min[1] + (pixel[1] - 5)/self.imageScale
  return (x1, y1)


 def PlotRoom(self):
  room = self.recoveredRooms[self.currentScan]
  for r in room:
   pixel = self.PointToPixel((r.x, r.y))
   self.image.putpixel(pixel, (255,0,0))
  self.image_tk = ImageTk.PhotoImage(self.image)
  self.canvas.itemconfig(self.image_on_canvas, image = self.image_tk)


 def OnButtonPress(self, event):
  # save mouse drag start position
  self.rectangleStartX = self.canvas.canvasx(event.x)
  self.rectangleStartY = self.canvas.canvasy(event.y)
  self.rectangleEndX = self.rectangleStartX
  self.rectangleEndY = self.rectangleStartY
  if self.rect is not None:
   self.canvas.delete(self.rect)
  self.rect = self.canvas.create_rectangle(self.rectangleStartX, self.rectangleStartY, 1, 1, outline='yellow')

 def OnMovePressing(self, event):
  curX = self.canvas.canvasx(event.x)
  curY = self.canvas.canvasy(event.y)
  # expand rectangle as you drag the mouse
  self.canvas.coords(self.rect, self.rectangleStartX, self.rectangleStartY, curX, curY)
  self.rectangleEndX = curX
  self.rectangleEndY = curY


 def OnButtonRelease(self, event):
    self.GatherTriangle()


 def NextScan(self):
  self.currentScan += 1
  if self.currentScan >= len(self.recoveredRooms):
   print("No more scans left.")
  else:
   self.PlotRoom()

 def Quit(self):
  quit()

 def MeasureTriangleFit(self, triangle, points):
  self.triangle = triangle
  sum = 0.0
  tPoint0 = Point2D(self.triangle[0], self.triangle[1])
  tPoint1 = Point2D(self.triangle[2], self.triangle[3])
  tPoint2 = Point2D(self.triangle[4], self.triangle[5])
  corners = [tPoint0, tPoint1, tPoint2]
  edges = [Line2D(tPoint0, tPoint1), Line2D(tPoint1, tPoint2), Line2D(tPoint2, tPoint0)]
  for point in points:
   p = Point2D(point[0], point[1])
   nearestD2 = sys.float_info.max
   for edge in edges:
    nearD2 = edge.DistanceToPoint2(p)
    #print("e: " + str(nearD2[0]) + ", " + str(nearD2[1]))
    if nearD2[0] < nearestD2:
     if nearD2[1] >= 0.0 and nearD2[1] <= 1.0:
      nearestD2 = nearD2[0]
   for corner in corners:
    cornerD2 = p.Sub(corner).Length2()
    #print("c: " + str(cornerD2))
    if cornerD2 < nearestD2:
     nearestD2 = cornerD2
   sum += nearestD2
  self.lastTriangleCost = sum
  return sum

 def Progress(self, x):
  self.progressCount += 1
  if not self.progressCount % 5 == 0:
   return
  print("Triangle sum of squares: " + str(self.lastTriangleCost) + " after " + str(self.progressCount) + " iterations.")
  #self.PlotTriangle((255,255,0))

 def PlotTriangle(self, colour):
  point0= (self.triangle[0], self.triangle[1])
  point1 = (self.triangle[2], self.triangle[3])
  point2 = (self.triangle[4], self.triangle[5])
  pixel0 = self.PointToPixel(point0)
  pixel1 = self.PointToPixel(point1)
  pixel2 = self.PointToPixel(point2)
  self.draw.line([pixel0, pixel1], fill = colour, width=1)
  self.draw.line([pixel1, pixel2], fill = colour, width=1)
  self.draw.line([pixel2, pixel0], fill = colour, width=1)
  self.image_tk = ImageTk.PhotoImage(self.image)
  self.canvas.itemconfig(self.image_on_canvas, image = self.image_tk)
  self.canvas.update_idletasks()

 def ScaleTriangle(self, scale):
  point0 = Point2D(self.triangle[0], self.triangle[1])
  point1 = Point2D(self.triangle[2], self.triangle[3])
  point2 = Point2D(self.triangle[4], self.triangle[5])
  centre = (point0.Add(point1).Add(point2)).Multiply(1.0/3.0)
  point0 = centre.Add(point0.Sub(centre).Multiply(scale))
  point1 = centre.Add(point1.Sub(centre).Multiply(scale))
  point2 = centre.Add(point2.Sub(centre).Multiply(scale))
  self.triangle[0] = point0.x
  self.triangle[1] = point0.y
  self.triangle[2] = point1.x
  self.triangle[3] = point1.y
  self.triangle[4] = point2.x
  self.triangle[5] = point2.y

 # TODO - this should fit a plane through the data and use Zs from that.
 # It should then project the three points back into pixels for
 # use in the second stage of the optimisation.
 def TriangleTo3D(self, z0, z1, z2):
  triangle3D = []
  triangle3D.append(Vector3(self.triangle[0], self.triangle[1], z0))
  triangle3D.append(Vector3(self.triangle[2], self.triangle[3], z1))
  triangle3D.append(Vector3(self.triangle[4], self.triangle[5], z2))
  return triangle3D

 def GatherTriangle(self):

  # Find all the scanned points in the user's dragged rectangle and
  # change their colour so we can see what's going on.

  cornerA = self.PixelToPoint((self.rectangleStartX, self.rectangleStartY))
  cornerB = self.PixelToPoint((self.rectangleEndX, self.rectangleEndY))
  minX = min(cornerA[0], cornerB[0])
  maxX = max(cornerA[0], cornerB[0])
  minY = min(cornerA[1], cornerB[1])
  maxY = max(cornerA[1], cornerB[1])
  perimiterXY = []
  perimiterPoints = []
  room = self.recoveredRooms[self.currentScan]
  count = 0
  for r in room:
   if r.x > minX and r.x < maxX and r.y > minY and r.y < maxY:
    count += 1
    if count%self.sample == 0:
     perimiterXY.append((r.x, r.y))
     perimiterPoints.append(r)
     pixel = self.PointToPixel((r.x, r.y))
     self.image.putpixel(pixel, (0,128,0))

  # Find the Convex Hull of those points

  hull = ConvexHull(perimiterXY)

  # Find the triangle in the convex hull with the biggest area

  biggestArea = -1.0
  corners = (-1, -1, -1)
  for t0 in range(len(hull.vertices) - 2):
   v0 = hull.vertices[t0]
   for t1 in range(t0 + 1, len(hull.vertices) - 1):
    v1 = hull.vertices[t1]
    for t2 in range(t1 + 1, len(hull.vertices)):
     v2 = hull.vertices[t2]
     xd1 =  perimiterXY[v1][0] - perimiterXY[v0][0]
     yd1 =  perimiterXY[v1][1] - perimiterXY[v0][1]
     xd2 =  perimiterXY[v2][0] - perimiterXY[v0][0]
     yd2 =  perimiterXY[v2][1] - perimiterXY[v0][1]
     area = abs(xd1*yd2 - yd1*xd2)
     if area > biggestArea:
      biggestArea = area
      corners = (v0, v1, v2)

  # Plot that triangle (diagnostic)

  if corners[0] >= 0:
   self.triangle = [perimiterXY[corners[0]][0], perimiterXY[corners[0]][1], perimiterXY[corners[1]][0], perimiterXY[corners[1]][1], perimiterXY[corners[2]][0], perimiterXY[corners[2]][1]]
   #self.PlotTriangle((0,0,255))
   self.ScaleTriangle(0.8)
   self.PlotTriangle((0,0,255))
   print("Starting sum of squares: " + str(self.MeasureTriangleFit(self.triangle, perimiterXY)))
   self.progressCount = 0
   minResult = minimize(self.MeasureTriangleFit, x0 = self.triangle, args = (perimiterXY,), callback = self.Progress)
   self.triangle = minResult.x
   print("Final sum of squares: " + str(self.lastTriangleCost))
   self.PlotTriangle((255,0,0))
   triangle3D = self.TriangleTo3D(perimiterPoints[corners[0]].z, perimiterPoints[corners[1]].z, perimiterPoints[corners[2]].z)
   print("Triangle cost relative to true sidelength: " + str(self.scanner.OneTriangleCost(self.triangleSideLength, triangle3D)))
  else:
   print("No biggest triangle found!")


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

c = Calibrate(scanner, 500, triangleFileNames, 0.5, 10)
