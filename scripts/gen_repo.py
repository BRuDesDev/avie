import os

# Create folder structure for the base repo
base_path = "/mnt/data/cryptid_detector"
# Folders for base repo
folders = [
    "data/raw_images",
    "data/processed_images",
    "data/labels",
    "models",
    "notebooks",
    "scripts",
    "utils"
]

for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create basic README and placeholder Python files
readme_content = """# Cryptid Detector AI

An AI-powered pipeline to scan satellite imagery for wildlife and anomalies using YOLO and Computer Vision.

## Features

- Random coordinate generation within radius
- Satellite image downloading via Google Static Maps API
- Object detection using YOLOv8
- Flagging and saving anomalies
- (Future) Integration with K230 Vision Module for real-world testing
"""

with open(os.path.join(base_path, "README.md"), "w") as f:
    f.write(readme_content)

# Placeholder scripts
placeholder_files = {
    "scripts/main.py": "# Entry point for the cryptid detection pipeline\n",
    "scripts/detect.py": "# Object detection logic using YOLOv8\n",
    "scripts/download_image.py": "# Download images using Google Static Maps API\n",
    "scripts/generate_coords.py": "# Random coordinate generation logic\n",
    "scripts/flag_anomalies.py": "# Logic to flag unusual detections\n",
    "utils/config.py": "# Configuration variables\n"
}

for path, content in placeholder_files.items():
    with open(os.path.join(base_path, path), "w") as f:
        f.write(content)

import shutil
shutil.make_archive("/mnt/data/cryptid_detector_repo", 'zip', base_path)