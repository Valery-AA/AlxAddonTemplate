from pathlib import Path  # type definition
import bpy

# AlxModuleAutoloader
import importlib
from .AlxModuleAutoloader import (
    developer_gather_addon_folders,
    developer_gather_addon_files,
    developer_execute_locals_update,
    developer_gather_classes_from_files,
    developer_register_addon_classes,
    developer_unregister_addon_classes
)


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


addon_path = __path__[0]
addon_folders: set[Path] = set()
addon_files: dict[str, Path] = dict()
addon_classes: set[str] = set()

folder_blacklist: set[str] = {"__pycache__"}
file_blacklist: set[str] = {"__init__.py"}


def register():
    addon_folders = developer_gather_addon_folders(addon_path, folder_blacklist)
    addon_files = developer_gather_addon_files(addon_folders, file_blacklist)
    developer_execute_locals_update(addon_path, globals(), addon_files)

    addon_classes = developer_gather_classes_from_files(globals(), addon_files)
    developer_register_addon_classes(addon_classes)

    bpy.context.preferences.use_preferences_save = True


def unregister():
    developer_unregister_addon_classes(addon_classes)


if __name__ == "__main__":
    register()
