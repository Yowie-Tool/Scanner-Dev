# Beech Design Scanner Simulation
# Adrian Bowyer
# 19 February 2020

import Part, BOPTools, FreeCAD, math, copy
from FreeCAD import Base

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Useful general functions and numbers

# Length in mm considered to be 0 and its square

tooShort = 0.001
tooShort2 = tooShort*tooShort

# There must be an easier way to make the null set...

def Null():
 n1 = Part.makeBox(1, 1, 1)
 n2 = Part.makeBox(1, 1, 1)
 n2.translate(Base.Vector(10, 10, 10))
 return(n1.common(n2))


# Make a cylinder between two points of a given radius

def Cylinder(p0, p1, r):
 p2 = p1.sub(p0)
 length = p2.Length
 if length < 0.001:
  return Null()
 c = Part.makeCylinder(r, length, p0, p2, 360)
 return c

# Make a plane cross section of a solid, s, and return it as a list of wires
# The plane passes through point p0 and has normal n

def CrossSection(s, p0, n):
 nn = copy.deepcopy(n)
 nn.normalize()
 d = nn.dot(p0)
 wires=list()
 for i in s.slice(nn, d):
  wires.append(i)
 comp=Part.Compound(wires)
 return comp

# Make a model to represent the room being scanned

def MakeRoom():
 b = Part.makeBox(10, 20, 30)
 return b

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Small classes for working with 2D vectors

class Point2D:
 def __init__(self, x = 0, y = 0)
  self.x = x
  self.y = y

 # Vector addition and subtraction

 def Add(self, p):
  result = copy.deepcopy(self)
  result.x = result.x + p.x
  result.y = result.y + p.y
  return result

 def Sub(self, p):
  result = copy.deepcopy(self)
  result.x = result.x - p.x
  result.y = result.y - p.y
  return result

 # Squared magnitude

 def Length2(self):
  return self.x*self.x + self.y*self.y

 # Multiplication by a scalar

 def Multiply(self, m):
  result = copy.deepcopy(self)
  result.x = result.x*m
  result.y = result.y*m
  return result  

 # Inner product

 def Dot(self, p):
  return self.x*p.x + self.y*p.y

 # Outer product

 def Cross(self, p):
  return self.x*p.y - self.y*p.x 

# Small class for working with 2D parametric lines

class Line2D:
 def __init__(self, p0 = Point2D(0, 0), p1 = Point2D(0, 0))
  self.p0 = p0
  self.direction = p1.Sub(p0)
  self.empty = self.Length2() < tooShort2

# The point at parameter value t

 def Point(self, t)
  p = self.direction.Multiply(t)
  return p0.Add(p)

 # Fine the parameter value at which another line crosses me (s) and I cross it (t)

 def Cross(self, otherLine):
  determinant = self.direction.Cross(otherLine.direction)
  if determinant < tooShort2:
   return None, None # Lines parallel
  dp = otherLine.p0.Sub(self.p0)
  s = otherLine.direction.Cross(dp)/determinant
  t = self.direction.Cross(dp)/determinant
  return s, t

 # Squared length

 def Length2(self):
  return self.direction.Length2()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Non-member functions that rely on the definitions above

# Clip line1 by line2, returning the result in r1 and maybe r2

def Clip(line1, line2):
 r1 = Line2D()
 r2 = Line2D()

 lp1 = line2.Point(0)
 lp2 = line2.Point(1)
 see1 = Line2D(Point2D(0, 0), lp1)
 see2 = Line2D(Point2D(0, 0), lp2)
 s1, t1 = line1.Cross(see1)
 if s1 is None: # line1 parallel?
  xxxx
 s2, t2 = line1.Cross(see2)
 if s2 is None: # line1 parallel?
  xxxx

 tMax = t1
 tMin = t1
 if t2 > tMax:
  tMax = t2
 if t2 < tMin:
  tMin = t2

 if tMax <= 1 + tooShort: # Is line1 in front of line2?
  r1 = line1
  return r1, r2

 sMax = s1
 sMin = s1
 if s2 > sMax:
  sMax = s2
 if s2 < sMin:
  sMin = s2

 if sMax <= tooShort || sMin >= 1 - tooShort: # Does line2 lie wholly to one side or the other of line1?
  r1 = line1
  return r1, r2

 if sMin <= tooShort && sMax >= 1 - tooShort: # Is line1 wholly obscured?
  return r1, r2

 if sMin > tooShort && sMax < 1 - tooShort: # Is line1 split in the middle?
  r1 = Line2D(line1.Point(0), line1.Point(sMin))
  r2 = Line2D(line1.Point(sMax), line1.Point(1))
  return r1, r2

 if tMin <= 1 + tooShort: # We already know that tMax is > 1




  

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# The main simulator class - this represents a part of the scanner.  The parts are arranged in a tree.

class ScannerPart:
 def __init__(self, offset = Base.Vector(0, 0, 0), u = Base.Vector(1, 0, 0), v = Base.Vector(0, 1, 0), w = Base.Vector(0, 0, 1), parent = None,\
  lightAngle = -1, uPixels = 0, vPixels = 0, uMM = 0, vMM = 0, focalLength = -1):

  # Offset from the parent in the parent's coordinate system
  # If the parent is None these are absolute cartesian coordinates

  self.offset = offset

  # Local Cartesian coordinates
 
  self.u = u.normalize()
  self.v = v.normalize()
  self.w = w.normalize()

  # If we are a light source (i.e. lightAngle >= 0)

  self.lightAngle = lightAngle

  # If we are a camera (i.e. focalLength >= 0)

  self.uPixels = uPixels
  self.vPixels = vPixels
  self.uMM = uMM
  self.vMM = vMM
  self.focalLength = focalLength

  # Hidden line calculations

  self.lines = []

  # Camera calculations

  # Parent and children in the tree

  self.parent = parent
  self.children = []
  if parent is not None:
   parent.children.append(self)

#-----------------

# Compute my absolute offset from the origin recursively

 def AbsoluteOffset(self):
  if self.parent is None:
   return self.offset
  parentUO = copy.deepcopy(self.parent.u)
  parentVO = copy.deepcopy(self.parent.v)
  parentWO = copy.deepcopy(self.parent.w)
  parentUO = parentUO.multiply(self.offset.x)
  parentVO = parentVO.multiply(self.offset.y)
  parentWO = parentWO.multiply(self.offset.z)
  o = parentUO.add(parentVO.add(parentWO))
  return o.add(self.parent.AbsoluteOffset())

# Rotate my coordinates, and the coordinates of all my descendents recursively

 def Rotate(self, r):
  self.u = r.multVec(self.u).normalize()
  self.v = r.multVec(self.v).normalize()
  self.w = r.multVec(self.w).normalize()
  for child in self.children:
   child.Rotate(r)

 # Rotate about the u axis. angle is in radians

 def RotateU(self, angle):
  r = Base.Rotation(self.u, angle*180/math.pi)
  self.Rotate(r)

 # Rotate about the v axis. angle is in radians

 def RotateV(self, angle):
  r = Base.Rotation(self.v, angle*180/math.pi)
  self.Rotate(r)

 # Rotate about the w axis. angle is in radians

 def RotateW(self, angle):
  r = Base.Rotation(self.w, angle*180/math.pi)
  self.Rotate(r)

 # Project edge onto the plane with axes x and y (usually, though not necessarily, two of u, v, or w)

 def Project(self, edge, x, y):
  v = copy.deepcopy(edge.Vertexes)
  ao = self.AbsoluteOffset()
  v[0] = v[0].sub(ao)
  v[1] = v[1].sub(ao)
  xe0 = x.multiply(v[0])
  ye0 = y.multiply(v[0])
  p0 = Point2D(xe0, ye0)
  xe1 = x.multiply(v[1])
  ye1 = y.multiply(v[1])
  p1 = Point2D(xe1, ye1)
  line = Line2D(p0, p1)
  return line

 # Initialise the hidden line eliminator

 def HideStart(self):
  self.lines = []

 # Visibility of one line against another

 def LinesVisible(self, edge, line):
  edgeA = Line2D(Point2D(0, 0), edge.p0)
  edgeB = Line2D(Point2D(0, 0), edge.Point(1.0))
  lineA = Line2D(Point2D(0, 0), line.p0)
  lineB = Line2D(Point2D(0, 0), line.Point(1.0))
  #...

 # Hide lines behind edge e, or e behind them.
 # Add (what's left of) e to the lines.

 def Hide(self, e):
  edge = self.Project(e, self.v, self.w)
  for line in self.lines:
   if edge.empty:
    break
   self.LinesVisible(edge, line)
   if line.empty:
    self.lines.remove(line)
  if !edge.empty:
   self.lines.append(edge)

 # Take the list of visible edges in x, y space and put it into 3D. x and y are usually, though not necessarily, two of u, v, or w.

 def EdgesTo3D(self, x, y):

 # Turn on the light and make a cross section of a shape, s.
 # The result is a Part consisting of zero (miss) or more wires.

 def LightSlice(self, s):
  p0 = self.AbsoluteOffset()
  cs = CrossSection(s, p0, self.u)
  es = cs.Edges
  self.HideStart()
  for edge in es:
   self.Hide(edge)
  return self.VWEdgesTo3D()

 # Make a picture of the tree recursively

 def Model(self):
  p1 = self.AbsoluteOffset()
  uc = Part.makeCylinder(0.2, 10, p1, self.u, 360)
  vc = Part.makeCylinder(0.2, 10, p1, self.v, 360)
  wc = Part.makeCylinder(0.2, 10, p1, self.w, 360)
  m = uc.fuse(vc)
  m = m.fuse(wc)
  if self.parent is not None:
   p0 = self.parent.AbsoluteOffset()
  else:
   p0 = Base.Vector(0, 0, 0)
  twig = Cylinder(p0, p1, 0.1)
  m = m.fuse(twig)
  for child in self.children:
   m = m.fuse(child.Model())
  return m

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

b = MakeRoom()
Part.show(b)
world = ScannerPart()
twig1 = ScannerPart(offset = Base.Vector(18, 20, 15), parent = world)
twig1.RotateV(1)
c = twig1.LightSlice(b)
es = c.Edges
for edge in es:
 v = edge.Vertexes
 for p in v:
  print(p.Point, end = ' ')
 print()
Part.show(c)
Part.show(world.Model())
twig1.RotateV(0.1)
d = twig1.LightSlice(b)
Part.show(d)

#world = ScannerPart()
#twig1 = ScannerPart(offset = Base.Vector(8, 20, 25), parent = world)
#twig2 = ScannerPart(offset = Base.Vector(10, -5, 6), parent = world)
#twig3 = ScannerPart(offset = Base.Vector(-10, 10, 30), parent = twig1)
#twig1.RotateU(1)
#a = world.Model()
#Part.show(a)



