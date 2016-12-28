import bpy
from mathutils import Vector

ob = bpy.context.active_object

#get local bounding box center
centre = sum((Vector(b) for b in ob.bound_box), Vector())
centre /= 8

print(centre)
#translate to world geom

print(ob.location)

xPos = centre[0] + ob.location[0]
yPos = centre[1] + ob.location[1]
zPos = centre[2] + ob.location[2]

print(str(xPos) + ", " + str(yPos) + ", " + str(zPos))

xMin = 0
xMax = 0
yMin = 0
yMax = 0
zMin = 0
zMax = 0

for b in ob.bound_box:
	if(Vector(b)[0] > xMax):
		xMax = Vector(b)[0]
	if(Vector(b)[0] < xMin):
		xMin = Vector(b)[0]

	if(Vector(b)[1] > yMax):
		yMax = Vector(b)[1]
	if(Vector(b)[1] < yMin):
		yMin = Vector(b)[1]

	if(Vector(b)[2] > zMax):
		zMax = Vector(b)[2]
	if(Vector(b)[2] < zMin):
		zMin = Vector(b)[2]
	print(Vector(b))

print(xMax)