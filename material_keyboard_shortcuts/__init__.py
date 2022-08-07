#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

import bpy
import math

# Version History
# 1.0.0 - 2020-09-16: Created.
# 1.0.1 - 2022-08-07: Misc formatting cleanup before uploading to GitHub.

bl_info = {
    "name": "Material Keyboard Shortcuts",
    "author": "Jeff Boller",
    "version": (1, 0, 1),
    "blender": (2, 93, 0),
    "location": "",
    "description": "This Blender add-on will cycle through the alpha value for all Principled BSDF materials of the currently-selected object. " \
                   "To run this, make a Blender keyboard shortcut and use the following command: wm.material_keyboard_shortcuts_toggle_alpha_value " \
                   "If you want to call this manually from Python, use the following command: bpy.ops.wm.material_keyboard_shortcuts_toggle_alpha_value() ",
    "wiki_url": "https://github.com/sundriftproductions/blenderaddon-material-keyboard-shortcuts/wiki",
    "tracker_url": "https://github.com/sundriftproductions/blenderaddon-material-keyboard-shortcuts",
    "category": "System"}

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

class WM_OT_material_keyboard_shortcuts_toggle_alpha_value(bpy.types.Operator):
    bl_idname = 'wm.material_keyboard_shortcuts_toggle_alpha_value'
    bl_label = 'Material Keyboard Shortcuts - Toggle Principled BSDF Alpha'
    bl_description = 'Call bpy.ops.wm.material_keyboard_shortcuts_toggle_alpha_value()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.material_keyboard_shortcuts_toggle_alpha_value')

        firstValue = None

        # We'll go through our materials and use the first one we find as the main value for all of our materials.
        # We don't want to have different materials with varying alpha levels -- they all need to be the same.
        for material in bpy.context.active_object.data.materials:
            try:
                if firstValue == None:
                    compare = material.node_tree.nodes["Principled BSDF"].inputs[19].default_value
                    
                    if compare >= 1.0:
                        firstValue = 0.95
                    elif compare >= 0.90:
                        firstValue = 0.85
                    elif compare >= 0.80:
                        firstValue = 0.75
                    elif compare >= 0.70:
                        firstValue = 0.65
                    elif compare >= 0.60:
                        firstValue = 0.55
                    elif compare >= 0.50:
                        firstValue = 0.45
                    elif compare >= 0.40:
                        firstValue = 0.35
                    elif compare >= 0.30:
                        firstValue = 0.25
                    elif compare >= 0.20:
                        firstValue = 0.15
                    elif compare >= 0.10:
                        firstValue = 0.05
                    else:
                        firstValue = 1.0

                material.node_tree.nodes["Principled BSDF"].inputs[19].default_value = firstValue
            except:
                placeholder = 0  # There is no Principled BSDF shader here.

            self.report({'INFO'}, 'wm.wm.material_keyboard_shortcuts_toggle_alpha_value: ' + str(truncate(firstValue, 2)))
        return {'FINISHED'}

def register():
    bpy.utils.register_class(WM_OT_material_keyboard_shortcuts_toggle_alpha_value)

def unregister():
    bpy.utils.unregister_class(WM_OT_material_keyboard_shortcuts_toggle_alpha_value)

if __name__ == "__main__":
    register()
