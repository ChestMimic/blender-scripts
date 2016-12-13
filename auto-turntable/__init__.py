bl_info = {
	"name":"Automatic Turntable",
	"description":"Automatically focus camera to rotate around a selected object in a scene",
	"version":(1,0),
	"blender":(2,78,0),
	"support":"TESTING",
	"category":"Render",
	"author":"ibbolia"
}
import bpy
import math
import mathutils
from math import radians

class Orbital:

	def __init__(self):
		self.TT_FILEPATH_ROOT = "/tmp\\"
		self.TT_FILEPATH_ITERATOR = "1"
		self.TT_FILEPATH_EXT  =".png"
		self.TT_ANGLE_INCREMENTS = 90
		self.TT_POSITION = (0.0, -5.0, 0.0)	#Camera should be in front (Neg-Y) of model
		self.TT_TARGET_VIEW = (0.0, 0.0, 0.0)	#Default viewpoint to origin
		self.TT_ROTATION_X = 90.0
		self.TT_ROTATION_Y = 0.0
		self.TT_ROTATION_Z = 0.0
		self.TT_RADIUS = 0.0

	def setToFrontview(self, camera):
		#Move camera front and center
		camera.location = self.TT_POSITION
		camera.rotation_euler = (radians(self.TT_ROTATION_X), 0.0, 0.0)
		#reposition camera to fit selected items
		bpy.ops.view3d.camera_to_view_selected()
		self.TT_POSITION = camera.location
		self.TT_RADIUS = camera.location[1]	#currently, Y coordinate == radius

	def renderOrbit(self, camera):
		while(self.TT_ROTATION_Z < 270):
			#Take render
			print("Camera at (" +str(self.TT_POSITION[0]) +"," + str(self.TT_POSITION[1]) +"," + str(self.TT_POSITION[2])  +")" )
			print("Camera heading: " + str(self.TT_ROTATION_Z))
			bpy.data.scenes['Scene'].render.filepath = self.TT_FILEPATH_ROOT + self.TT_FILEPATH_ITERATOR + self.TT_FILEPATH_EXT
			bpy.ops.render.render( write_still=True ) 
			self.TT_FILEPATH_ITERATOR = str(int(self.TT_FILEPATH_ITERATOR)+1)
			self.TT_ROTATION_Z = self.TT_ROTATION_Z + self.TT_ANGLE_INCREMENTS
			camera.rotation_euler = (radians(self.TT_ROTATION_X), 0.0, radians(self.TT_ROTATION_Z))
			#Set position
			self.TT_POSITION[0] = (self.TT_RADIUS * math.cos(radians(self.TT_ROTATION_Z+self.TT_ANGLE_INCREMENTS)))
			self.TT_POSITION[1] =  (self.TT_RADIUS * math.sin(radians(self.TT_ROTATION_Z+self.TT_ANGLE_INCREMENTS)))
			camera.location= mathutils.Vector(self.TT_POSITION)
			#bpy.ops.mesh.primitive_cube_add(location=self.TT_POSITION) 

class OrbitalOperator(bpy.types.Operator):
	
	bl_idname = "object.automatic_turntable"    #id name
	bl_label = "Orbit selected object and render"        #Display Label
	bl_options = {"REGISTER"}       #Possible operations

	def execute(self, context):
		obj_cam = bpy.data.objects["Camera"]
		orbit = Orbital()
		orbit.setToFrontview(obj_cam)
		orbit.renderOrbit(obj_cam)
		return {"FINISHED"}

def register():
	bpy.utils.register_class(OrbitalOperator)

def unregister():
	bpy.utils.unregister_class(OrbitalOperator)

if __name__ == "__main__":
	register()