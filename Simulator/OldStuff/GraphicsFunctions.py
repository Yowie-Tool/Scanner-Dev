import Part, BOPTools, FreeCAD, math, copy, sys
from FreeCAD import Base
import PySide
from PySide import QtGui, QtCore
from PIL import Image, ImageDraw, ImageFilter

# Unique count as a string

objectCount = -1

def UniqueNumber():
 global objectCount
 objectCount += 1
 return str(objectCount)

# Display a FreeCAD shape with a given colour as an RGB tripple like (0.0, 1.0, 0.0)

def DisplayShape(shape, colour):
 obj = FreeCAD.ActiveDocument.addObject("Part::Feature" ,"Shape"+UniqueNumber())
 obj.Shape = shape
 obj.ViewObject.ShapeColor = colour
 obj.ViewObject.LineColor = colour

# There must be an easier way to make the FreeCAD null set...

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
