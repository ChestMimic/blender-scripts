# BEGIN GPL BLOCK    
#    Blender Renderwatch monitors the status of the Render operation
#    Copyright (C) 2015  Mark Fitzgibbon
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
    "name": "Select All Children",
    "category": "Object",
    "author": "ibbolia"}

import bpy

def getChildren(target):
    res = []
    scene = bpy.data.objects
    for OBJ in scene:
        if OBJ.parent == target:
            res.append(OBJ)
            OBJ.select = True
    return res

def selectChildrenR(target):
    if target == []:
        return []
    else:
        for PARENT in target:
            childLst = getChildren(PARENT)
            selectChildrenR(childLst)

class SelectChildren(bpy.types.Operator):
    bl_idname = "object.select_children"
    bl_label = "Select All Children"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        lst = bpy.context.selected_objects
        childlist = getChildren(lst[0])
        selectChildrenR(lst)
        return {'FINISHED'}

    

def register():
    bpy.utils.register_class(SelectChildren)
    
def unregister():
    bpy.utils.unregister_class(SelectChildren)
    
if __name__ == "__main__":
    register()