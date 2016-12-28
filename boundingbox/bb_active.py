import bpy
from mathutils import Vector

lst = bpy.context.selected_objects

xMin = None
xMax = None
yMin = None
yMax = None
zMin = None
zMax = None

print("RUN")
#Obtain bounding box in an object's local space
for ob in lst:
	
	print(ob.location)
	loc = ob.location

	for b in ob.bound_box:
		if xMax is None or ((Vector(b)[0] + ob.location[0]) > xMax):
			xMax = Vector(b)[0] + ob.location[0]
		if xMin is None or ((Vector(b)[0] + ob.location[0]) < xMin):
			xMin = Vector(b)[0] + ob.location[0]

		if yMax is None or ((Vector(b)[1] + ob.location[1]) > yMax) :
			yMax = Vector(b)[1] + ob.location[1]
		if yMin is None or ((Vector(b)[1] + ob.location[1]) < yMin):
			yMin = Vector(b)[1] + ob.location[1]

		if zMax is None or ((Vector(b)[2] + ob.location[2]) > zMax):
			zMax = Vector(b)[2] + ob.location[2]
		if zMin is None or ((Vector(b)[2] + ob.location[2]) < zMin):
			zMin = Vector(b)[2] + ob.location[2]
		print(Vector(b))

	print(zMax)
	#print(str(zMax + loc[2]))


xMid = (xMin + xMax)/2
yMid = (yMin + yMax)/2
zMid = (zMin + zMax)/2

minimum = (xMin, yMin, zMin)
maximum = (xMax, yMax, zMax)
midpoint = (xMid, yMid, zMid)

print("Minimum:")
print(minimum)

print("Maximum:")
print(maximum)

print("Midpoint:")
print(midpoint)
