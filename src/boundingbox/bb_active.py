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
	loc, rot, scale = ob.matrix_world.decompose();
	

	for b in ob.bound_box:
		globalPos = lambda i: (Vector(b)[i])*scale[i] + loc[i]
		if xMax is None or globalPos(0) > xMax:
			xMax = globalPos(0)
		if xMin is None or globalPos(0) < xMin:
			xMin = globalPos(0)

		if yMax is None or globalPos(1) > yMax :
			yMax = globalPos(1)
		if yMin is None or globalPos(1) < yMin:
			yMin = globalPos(1)

		if zMax is None or globalPos(2) > zMax:
			zMax = globalPos(2)
		if zMin is None or globalPos(2) < zMin:
			zMin = globalPos(2)


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
