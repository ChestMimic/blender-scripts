# BEGIN GPL BLOCK    
#    Generates a mirrored cube at 3D Cursor location
#    Copyright (C) 2017  Mark Fitzgibbon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# END GPL BLOCK
bl_info = {
	"name":"Mirror Box",
	"description":"Generates a mirrored cube at 3D Cursor location",
	"location":"Add",
	"tracker_url":"https://github.com/ibbolia/blender-scripts/issues",
	"version":(1,0,0),
	"blender":(2,78,0),
	"support":"COMMUNITY",
	"category":"Objects",
	"author":"Mark Fitzgibbon"
}
import bpy
from bpy.props import FloatProperty

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

	radius = FloatProperty(
		name = "radius",
		default = 1.0)

	def execute(self, context):
		mesh_data = bpy.data.meshes.new("mirror_box_mesh_data")
		meshInfo = MirrorBoxInfo(self.radius)
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
		text = "MrBox",
		icon = "MOD_MIRROR")

addon_keymaps = []

def register():
	bpy.utils.register_class(MirrorBoxOperator)
	bpy.types.INFO_MT_add.append(add_MirrorBox_button) 

	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

	kmi = km.keymap_items.new(MirrorBoxOperator.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
	kmi.properties.radius = 1

	addon_keymaps.append((km, kmi))

def unregister():
	bpy.utils.unregister_class(MirrorBoxOperator)
	bpy.types.INFO_MT_add.remove(add_MirrorBox_button)
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()

if __name__ == "__main__":
	register()