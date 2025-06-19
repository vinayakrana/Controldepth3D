import subprocess

def run_training(scene_path: str):
    subprocess.run([
        "ns-train", "nerfacto",
        "--data", scene_path,
        "--viewer.quit-on-train-completion", "True"
    ], check=True)
