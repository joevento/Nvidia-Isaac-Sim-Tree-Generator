import random as r
import numpy as np

from pxr import Gf, Usd, UsdGeom

import omni.ext
import omni.ui as ui
from omni.isaac.ui.ui_utils import str_builder
from pxr.Usd import Stage
from omni.isaac.core.utils.stage import add_reference_to_stage, get_current_stage
import omni.isaac.core.utils.prims as prim_utils
from omni.isaac.core.prims import XFormPrim
import carb
from omni.physx import get_physx_scene_query_interface

trees = []
#change this
Birch_usd_path = "D:/temp_downloads/Birch_obj/Birch.usd"
Spruce_usd_path = "D:/temp_downloads/Spruce_obj/Spruce.usd"
Pine_usd_path = "D:/temp_downloads/Pine_obj/Pine.usd"
Maple_usd_path = "D:/temp_downloads/maple_obj/maple.usd"

def convert_rotation(roll, pitch, yaw):
    #converts degrees to radians first
    roll = roll * (np.pi/180)
    pitch = pitch * (np.pi/180)
    yaw = yaw * (np.pi/180)
    #radians to quarternions
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return qw, qx, qy, qz

def generate_trees(path_to_coords):
    stage = get_current_stage()
    over_all_scale = 100

    with open(path_to_coords) as coord_file:
        for line in coord_file:
            x, y, z, tree_type, sc_x, sc_y, sc_z = line.strip().split(";")
            x = float(x) * over_all_scale
            y = float(y) * over_all_scale
            z = float(z) * over_all_scale
            tree_type = int(tree_type)
            sc_x = float(sc_x) * over_all_scale
            sc_y = float(sc_y) * over_all_scale
            sc_z = float(sc_z) * over_all_scale
            print(f"Tree data: {x}, {y}, {z}, {tree_type}, {sc_x}, {sc_y}, {sc_z}")

            if tree_type == 0:
                #path to the tree
                tree_path = f'/World/Tree_parent/Tree_{str(len(trees)).rjust(4,"0")}'
                xform = prim_utils.create_prim(tree_path, "Xform")

                #load the model and place it in the world
                add_reference_to_stage(usd_path=Birch_usd_path, prim_path=tree_path)

                #randomize roatation
                qw, qx, qy, qz = convert_rotation(0, 0, r.randrange(-180, 180))

                #set rot, scale and pos
                prim_utils.set_prim_property(tree_path, "xformOp:orient", Gf.Quatd(qw, qx, qy, qz))
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x),
                                            float(y), 1000))
                prim_utils.set_prim_property(tree_path, "xformOp:scale", Gf.Vec3d(sc_x, sc_y, sc_z))

                #find where ground is and move the tree there
                distance_to_ground = 1000-check_raycast(stage, tree_path)
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x), float(y),
                                            distance_to_ground))

                trees.append(tree_path)

            elif tree_type == 1:
                #path to the tree
                tree_path = f'/World/Tree_parent/Tree_{str(len(trees)).rjust(4,"0")}'
                xform = prim_utils.create_prim(tree_path, "Xform")

                #load the model and place it in the world
                add_reference_to_stage(usd_path=Spruce_usd_path, prim_path=tree_path)

                #randomize roatation
                qw, qx, qy, qz = convert_rotation(0, 0, r.randrange(-180, 180))

                #set rot, scale and pos
                prim_utils.set_prim_property(tree_path, "xformOp:orient", Gf.Quatd(qw, qx, qy, qz))
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x),
                                            float(y), 1000))
                prim_utils.set_prim_property(tree_path, "xformOp:scale", Gf.Vec3d(sc_x, sc_y, sc_z))

                #find where ground is and move the tree there
                distance_to_ground = 1000-check_raycast(stage, tree_path)
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x), float(y),
                                            distance_to_ground))

                trees.append(tree_path)

            elif tree_type == 2:
                #path to the tree
                tree_path = f'/World/Tree_parent/Tree_{str(len(trees)).rjust(4,"0")}'
                xform = prim_utils.create_prim(tree_path, "Xform")

                #load the model and place it in the world
                add_reference_to_stage(usd_path=Pine_usd_path, prim_path=tree_path)

                #randomize roatation
                qw, qx, qy, qz = convert_rotation(0, 0, r.randrange(-180, 180))

                #set rot, scale and pos
                prim_utils.set_prim_property(tree_path, "xformOp:orient", Gf.Quatd(qw, qx, qy, qz))
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x),
                                            float(y), 1000))
                prim_utils.set_prim_property(tree_path, "xformOp:scale", Gf.Vec3d(sc_x, sc_y, sc_z))

                #find where ground is and move the tree there
                distance_to_ground = 1000-check_raycast(stage, tree_path)
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x), float(y),
                                            distance_to_ground))

                trees.append(tree_path)

            else:
                #path to the tree
                tree_path = f'/World/Tree_parent/Tree_{str(len(trees)).rjust(4,"0")}'
                xform = prim_utils.create_prim(tree_path, "Xform")

                #load the model and place it in the world
                add_reference_to_stage(usd_path=Maple_usd_path, prim_path=tree_path)

                #randomize roatation
                qw, qx, qy, qz = convert_rotation(0, 0, r.randrange(-180, 180))

                #set rot, scale and pos
                prim_utils.set_prim_property(tree_path, "xformOp:orient", Gf.Quatd(qw, qx, qy, qz))
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x),
                                            float(y), 1000))
                prim_utils.set_prim_property(tree_path, "xformOp:scale", Gf.Vec3d(sc_x, sc_y, sc_z))

                #find where ground is and move the tree there
                distance_to_ground = 1000-check_raycast(stage, tree_path)
                prim_utils.set_prim_property(tree_path, "xformOp:translate", Gf.Vec3d(float(x), float(y),
                                            distance_to_ground))

                trees.append(tree_path)

def check_raycast(stage, path_to_object):
    # Projects a raycast from 'origin', in the direction of 'rayDir', for a length of 'distance' cm
    # Parameters can be replaced with real-time position and orientation data  (e.g. of a camera)
    rayDir = carb.Float3(0.0, 0.0, -1.0)
    origin = carb.Float3(prim_utils.get_prim_property(path_to_object, "xformOp:translate"))
    distance = 100000.0
    # physX query to detect closest hit
    hit = get_physx_scene_query_interface().raycast_closest(origin, rayDir, distance)
    if(hit["hit"]):
        #record distance from origin
        usdGeom = UsdGeom.Mesh.Get(stage, hit["rigidBody"])
        distance = hit["distance"]
        return distance

def delete_forest(stage:Stage):
    for tree_path in trees:
        if stage.GetPrimAtPath(tree_path):
            stage.RemovePrim(tree_path)
    trees.clear()

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class PuutarhaTreeGeneratorExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[Puutarha-tree-generator] puutarha tree generator startup")

        self._window = ui.Window("Puutarha tree generator", width=350, height=150)
        with self._window.frame:
            with ui.VStack():
                stage = omni.usd.get_context().get_stage()

                def on_forest():
                    path_to_coords = tree_coord_file.get_value_as_string()
                    generate_trees(path_to_coords)
                def on_delete():
                    stage:Stage = omni.usd.get_context().get_stage()
                    delete_forest(stage)

                with ui.HStack(height=20):
                    tree_coord_file = str_builder(
                    label="Tree coordinate path",
                    tooltip="Directory where the tree coordinates is stored. The path must not end in a slash.",
                    use_folder_picker=True,
                    item_filter_fn=lambda item: item.is_folder or item.path.endswith('.txt'),
                    folder_dialog_title="Select Path",
                    folder_button_title="Select"
                )

                with ui.HStack():
                    ui.Button("Generate trees", clicked_fn=on_forest)
                    ui.Button("Delete trees", clicked_fn=on_delete)

    def on_shutdown(self):
        print("[Puutarha-tree-generator] puutarha tree generator shutdown")
