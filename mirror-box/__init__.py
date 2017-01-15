bl_info = {
	"name":"Mirror Box",
	"description":"Generate a mirrored, subdivided version of the starting cube",
	"version":(0,1,0),
	"blender":(2,78,0),
	"support":"TESTING",
	"category":"Objects",
	"author":"Mark Fitzgibbon"
}
import bpy



class MirrorBox(bpy.types.Operator):
	bl_idname="object.mirrorbox"
	bl_label = "Add MirrorBox"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		#Right half of a once subdivided cube
		verts = [(0.0, -1.0, 1.0),	#0
			(1.0, -1.0, 1.0),		#1
			(1.0, 0.0, 1.0),		#2
			(0.0, 0.0, 1.0),		#3
			(0.0, 1.0, 1.0),		#4
			(1.0, 1.0, 1.0),		#5
			(0.0, -1.0, 0.0),		#6
			(1.0, -1.0, 0.0),		#7
			(1.0, 0.0, 0.0),		#8
			(1.0, 1.0, 0.0),		#9
			(0.0, 1.0, 0.0),		#10
			(0.0, -1.0, -1.0),		#11
			(1.0, -1.0, -1.0),		#12
			(1.0, 0.0, -1.0),		#13
			(1.0, 1.0, -1.0),		#14
			(0.0, 1.0, -1.0),		#15
			(0.0, 0.0, -1.0)]		#16
		edges = []
		faces = [(0,1,2,3),
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

		mesh_data = bpy.data.meshes.new("mirror_box_mesh_data")
		mesh_data.from_pydata(verts, edges, faces)
		mesh_data.update()

		obj = bpy.data.objects.new("MrBox", mesh_data)

		scene = bpy.context.scene
		scene.objects.link(obj)
		obj.select = True

		obj.modifiers.new('MirrorBox', 'MIRROR')
		return {'FINISHED'}

def register():
	bpy.utils.register_class(MirrorBox)

def unregister():
	bpy.utils.unregister_class(MirrorBox)

if __name__ == "__main__":
	register()