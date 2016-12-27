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
yPos = centre[2] + ob.location[2]