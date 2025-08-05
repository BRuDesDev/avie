# brutils/paths.py

import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

RAW_IMAGE_DIR = os.path.join(DATA_DIR, "raw_images")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed_images")
ANNOTATED_OUTPUT = os.path.join(PROCESSED_DIR, "yolo_output", "run")
DETECTIONS_LOG = os.path.join(LOG_DIR, "detections.jsonl")
