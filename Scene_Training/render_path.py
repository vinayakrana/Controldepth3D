import json
import numpy as np

def create_spiral_camera_path(transforms_path: str, output_path: str, radius=1.5, num_frames=90):
    with open(transforms_path) as f:
        transforms = json.load(f)

    camera_positions = [np.array(f["transform_matrix"])[:3, 3] for f in transforms["frames"]]
    look_at = np.mean(camera_positions, axis=0)
    fixed_z = look_at[2] + 0.5
    up = np.array([0, 0, 1])
    fov = 60

    def normalize(v): return v / np.linalg.norm(v)

    def create_c2w(pos):
        forward = normalize(look_at - pos)
        right = normalize(np.cross(forward, up))
        up_corr = np.cross(right, forward)
        mat = np.eye(4)
        mat[:3, 0] = right
        mat[:3, 1] = up_corr
        mat[:3, 2] = -forward
        mat[:3, 3] = pos
        return mat

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        pos = np.array([
            look_at[0] + radius * np.cos(angle),
            look_at[1] + radius * np.sin(angle),
            fixed_z
        ])
        c2w = create_c2w(pos)
        frames.append({"camera_to_world": c2w.tolist(), "fov": fov})

    spiral = {
        "version": "1.0",
        "seconds": 6,
        "render_height": 800,
        "render_width": 800,
        "frames": frames
    }

    with open(output_path, "w") as f:
        json.dump(spiral, f, indent=4)
    print(f"Spiral camera path saved to {output_path}")
