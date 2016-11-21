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
    "name": "Renderwatch",  #Temporary name
    "description": "Watches render usage to notify when a render is complete",
    "author": "Mark 'ibbolia' Fitzgibbon",
    "version": (0, 1),
    "blender": (2, 65, 0),
    "location": "Automatic",
    "warning": "System console must be open for Renderwatch to work currently",
    "support": "TESTING",
    "wiki_url": "https://github.com/ibbolia/Blender_Renderwatch/wiki",
    "category": "Render"}

import bpy, aud, os
from bpy.app.handlers import persistent
from bpy.types import Operator, AddonPreferences, Panel

## ---PREFERENCES---
class RenderWatchPrefs(AddonPreferences):
    bl_idname = __name__
    scriptdir = bpy.path.abspath(os.path.dirname(__file__))
    defsong = bpy.props.StringProperty(
        name = "Render Sound",
        description = "Sound to play when Render completes successfully (render_complete)",
        subtype = 'FILE_PATH',
        default = bpy.path.abspath(os.path.dirname(__file__)) + "/music/b9s.mp3")
    playsong = bpy.props.StringProperty(
        name = "Render Sound",
        description = "Sound to play when Render completes successfully (render_complete)",
        subtype = 'FILE_PATH',
        default = "C:/Users/ibbolia/Downloads/111-pokemon-recovery.mp3")
       
       
## ---HANDLERS---
@persistent
def render_handler(dummy):
    print("Render Complete")
    #locale = "C:/Users/ibbolia/Downloads/111-pokemon-recovery.mp3"#replace with mp3 of choice
    try:
        locale = bpy.context.user_preferences.addons[__name__].preferences.playsong
        sound = aud.Factory.file(locale)
        aud.device().play(sound)
    except:
        print("Reverting to default song. Please confirm file exists")
        locale = bpy.context.user_preferences.addons[__name__].preferences.defsong
        sound = aud.Factory.file(locale)
        aud.device().play(sound)
  
## ---USER INTERFACE---
class UIPanel(bpy.types.Panel):
    bl_label = "Renderwatch"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
 
    def draw(self, context):
        self.layout.operator("renderwatch.hello", text='Servus')
        
## ---OPERATORS---
class OBJECT_OT_PreferenceButton(Operator):
    bl_idname = "renderwatch.hello"
    bl_label = "Say Hello"
    
    def execute(self, context):
        print("Hello World")
        return{'FINISHED'}
        
## ---REGISTER---
def register():
    bpy.utils.register_module(__name__)
    
    bpy.app.handlers.render_complete.append(render_handler)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
    bpy.app.handlers.render_complete.remove(render_handler)

if __name__ == "__main__":
    register()