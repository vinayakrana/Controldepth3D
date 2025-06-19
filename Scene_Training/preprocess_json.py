import json
import random
from pathlib import Path

def clean_and_split_transforms(json_path: str, seed=42):
    path = Path(json_path)
    with open(path, "r") as f:
        data = json.load(f)

    for frame in data["frames"]:
        name = Path(frame["file_path"]).name.split(".")[0]
        frame["file_path"] = f"./images/{name}.jpg"

    random.seed(seed)
    random.shuffle(data["frames"])

    n = len(data["frames"])
    splits = {
        "train": data["frames"][:int(0.8 * n)],
        "val": data["frames"][int(0.8 * n):int(0.9 * n)],
        "test": data["frames"][int(0.9 * n):]
    }

    for split, frames in splits.items():
        out_path = path.parent / f"transforms_{split}.json"
        with open(out_path, "w") as f:
            json.dump({**data, "frames": frames}, f, indent=4)
        print(f"Saved {split}: {out_path} with {len(frames)} frames")
