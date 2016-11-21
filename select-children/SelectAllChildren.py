bl_info = {
    "name": "Select All Children",
    "category": "Object",
}

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