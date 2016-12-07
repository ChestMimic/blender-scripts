import bpy
from bpy import context
from math import radians

obj_cam = bpy.data.objects["Camera"]

obj_cam.location = (0.0, -5.0, 0.0)
obj_cam.rotation_euler = (radians(90), 0.0, 0.0)
bpy.ops.view3d.camera_to_view_selected()
bpy.ops.render.render(animation=False)