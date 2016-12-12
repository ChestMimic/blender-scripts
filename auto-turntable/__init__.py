import bpy
from math import radians

class Orbital:

	def __init__(self):
		self.TT_ANGLE_INCREMENTS = 90
		self.TT_POSITION = (0.0, -5.0, 0.0)	#Camera should be in front (Neg-Y) of model
		self.TT_TARGET_VIEW = (0.0, 0.0, 0.0)	#Default viewpoint to origin
		self.TT_ROTATION_X = 90.0
		self.TT_ROTATION_Y = 0.0
		self.TT_ROTATION_Z = 0.0

	def setToFrontview(self, camera):
		#Move camera front and center
		camera.location = self.TT_POSITION
		camera.rotation_euler = (radians(self.TT_ROTATION_X), 0.0, 0.0)
		#reposition camera to fit selected items
		bpy.ops.view3d.camera_to_view_selected()

	def renderOrbit(self, camera):
		while(self.TT_ROTATION_Z < 360):
			#Take render
			#bpy.ops.render.render(animation=False)
			self.TT_ROTATION_Z = self.TT_ROTATION_Z + self.TT_ANGLE_INCREMENTS
			camera.rotation_euler = (radians(self.TT_ROTATION_X), 0.0, radians(self.TT_ROTATION_Z))
			#Set position

if __name__ == "__main__":
	obj_cam = bpy.data.objects["Camera"]
	orbit = Orbital()
	orbit.setToFrontview(obj_cam)