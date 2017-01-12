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

verts = []
edges = []
faces = []

mesh_data = bpy.data.meshes.new("mirror_box_mesh_data")
mesh_data.from_pydata(verts, edges, faces)
mesh_data.update()

obj = bpy.data.objects.new("MrBox", mesh_data)

scene = bpy.context.scene
scene.objects.link(obj)
obj.select = True

obj.modifiers.new('MirrorBox', 'MIRROR')