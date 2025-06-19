import os
import shutil

def setup_scene_directory(dataset_path: str, scene_dir: str):
    os.makedirs(scene_dir, exist_ok=True)
    os.makedirs(f"{scene_dir}/images", exist_ok=True)

    shutil.copy(os.path.join(dataset_path, "transforms.json"), scene_dir)

    shutil.copytree(
        os.path.join(dataset_path, "images", "images"),
        os.path.join(scene_dir, "images"),
        dirs_exist_ok=True
    )
    print("Scene directory setup complete.")
    return scene_dir