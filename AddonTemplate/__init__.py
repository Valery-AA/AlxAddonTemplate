# AlxModuleAutoloader
import importlib
from .AlxModuleManager import (
    Alx_Module_Manager
)

import bpy


bl_info = {
    "name": "",
    "author": "(developer) your_name_here, (automation) Valeria Bosco[Valy Arhal]",
    "description": "",
    "warning": "",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),  # minimum version AUTOMATION WILL CRASH IF NOT RESPECTED
    "category": "",
    "location": "",
    "doc_url": "",
    "tracker_url": ""
}

module_loader = Alx_Module_Manager(__path__, globals())


def register():
    module_loader.developer_register_modules()
    module_loader.developer_process_module_keymaps()

    bpy.context.preferences.use_preferences_save = True


def unregister():
    module_loader.developer_unregister_modules()


if __name__ == "__main__":
    register()
