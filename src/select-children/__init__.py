# BEGIN GPL BLOCK    
#    Blender Renderwatch monitors the status of the Render operation
#    Copyright (C) 2016  Mark Fitzgibbon
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
    res = []                                #Initialize empty list
    scene = bpy.data.objects                #Assign scene, most useful root position
    for OBJ in scene:                       #Run check against all object in scene
        if OBJ.parent == target:            #An object's parent data matches given target
            res.append(OBJ)                 #Add to list
            OBJ.select = True               #Select object in Blender UI
    return res                              #Return objects

def selectChildrenR(target):
    if target == []:                        #Nothing to work with
        return []                           #Return empty list
    else:
        for PARENT in target:               #Each possible parent in list
            childLst = getChildren(PARENT)  #Get the object's children as a list
            selectChildrenR(childLst)       #Call function on all of object's children

class SelectChildren(bpy.types.Operator):
    bl_idname = "object.select_children"    #id name
    bl_label = "Select All Children"        #Display Label
    bl_options = {"REGISTER", "UNDO"}       #Possible operations
    
    def execute(self, context):
        lst = bpy.context.selected_objects  #List of all selected objects
        #TODO: Next 2 lines look off...
        childlist = getChildren(lst[0])     
        selectChildrenR(lst)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SelectChildren)
    
def unregister():
    bpy.utils.unregister_class(SelectChildren)
    
if __name__ == "__main__":
    register()