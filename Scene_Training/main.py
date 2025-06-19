import yaml
import argparse
from setup_scene import setup_scene_directory
from preprocess_json import clean_and_split_transforms
from train_model import run_training
from render_path import create_spiral_camera_path

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Run NeRF pipeline from config.")
    parser.add_argument("--config", type=str, required=True, help="Path to the config.yaml file.")
    args = parser.parse_args()

    config = load_config(args.config)
    dataset_path = config["dataset_path"]
    
    scene_path = setup_scene_directory(dataset_path, scene_path)
    transforms_json = f"{scene_path}/transforms.json"
    spiral_output = f"{scene_path}/spiral_camera_path.json"

    clean_and_split_transforms(transforms_json)
    run_training(scene_path)
    create_spiral_camera_path(transforms_json, spiral_output)

if __name__ == "__main__":
    main()
