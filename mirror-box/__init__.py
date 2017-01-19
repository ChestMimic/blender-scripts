bl_info = {
	"name":"Mirror Box",
	"description":"Generate a mirrored, subdivided version of the starting cube",
	"version":(0,1,1),
	"blender":(2,78,0),
	"support":"TESTING",
	"category":"Objects",
	"author":"Mark Fitzgibbon"
}
import bpy

class MirrorBoxInfo:
	def __init__(self, radius=1.0):
		#Right half of a once subdivided cube
		self.verts = [
			(0.0, -radius, radius),			#0
			(radius, -radius, radius),		#1
			(radius, 0.0, radius),			#2
			(0.0, 0.0, radius),				#3
			(0.0, radius, radius),			#4
			(radius, radius, radius),		#5
			(0.0, -radius, 0.0),			#6
			(radius, -radius, 0.0),			#7
			(radius, 0.0, 0.0),				#8
			(radius, radius, 0.0),			#9
			(0.0, radius, 0.0),				#10
			(0.0, -radius, -radius),		#11
			(radius, -radius, -radius),		#12
			(radius, 0.0, -radius),			#13
			(radius, radius, -radius),		#14
			(0.0, radius, -radius),			#15
			(0.0, 0.0, -radius)]			#16
		self.edges = []
		self.faces = [(0,1,2,3),
			(5, 4, 3, 2),
			(1, 0, 6, 7),
			(7, 8, 2, 1),
			(8, 9, 5, 2),
			(5, 9, 10, 4),
			(6, 11, 12, 7),
			(7, 12, 13, 8),
			(8, 13, 14, 9),
			(9, 14, 15, 10),
			(16, 13, 12, 11),
			(16, 15, 14, 13)]


class MirrorBoxOperator(bpy.types.Operator):
	bl_idname="object.mirrorbox"
	bl_label = "Add MirrorBox"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		

		mesh_data = bpy.data.meshes.new("mirror_box_mesh_data")
		meshInfo = MirrorBoxInfo()
		mesh_data.from_pydata(meshInfo.verts, meshInfo.edges, meshInfo.faces)
		mesh_data.update()

		obj = bpy.data.objects.new("MrBox", mesh_data)
		obj.location = bpy.context.scene.cursor_location

		scene = bpy.context.scene
		scene.objects.link(obj)
		obj.select = True

		obj.modifiers.new('MirrorBox', 'MIRROR')
		return {'FINISHED'}

def add_MirrorBox_button(self, context):
	self.layout.operator(
		MirrorBoxOperator.bl_idname,
		text = "TBD",
		icon = "PLUGIN")

def register():
	bpy.utils.register_class(MirrorBoxOperator)
	bpy.types.INFO_MT_add.append(add_MirrorBox_button)  

def unregister():
	bpy.utils.unregister_class(MirrorBoxOperator)

if __name__ == "__main__":
	register()