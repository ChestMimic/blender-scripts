import bpy
from math import radians

TT_ANGLE_INCREMENTS = 90

def setToFrontview(camera):
	#Move camera front and center
	camera.location = (0.0, -5.0, 0.0)
	#Orient Camera pointing to Origin (0,0,0)
	camera.rotation_euler = (radians(90), 0.0, 0.0)
	#reposition camera to fit selected items
	bpy.ops.view3d.camera_to_view_selected()

def renderOrbit(camera):
	#Take render
	#bpy.ops.render.render(animation=False)
	pass

if __name__ == "__main__":
	obj_cam = bpy.data.objects["Camera"]
	setToFrontview(obj_cam)