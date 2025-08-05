# scripts/flag_anomalies.py

import os
import json
from datetime import datetime

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from brutils.paths import DETECTIONS_LOG

def log_detections(results, lat, lon, image_path, selected_filters=None, output_path=DETECTIONS_LOG):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    detections = []
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = result.names.get(cls_id, "unknown")

            detections.append({
                "class_id": cls_id,
                "class_name": class_name,
                "confidence": confidence
            })

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "coordinates": {
            "latitude": lat,
            "longitude": lon
        },
        "image_path": image_path,
        "detections": detections,
        "filters": selected_filters or {}
    }

    with open(output_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"🧠 Logged {len(detections)} detections at {lat}, {lon}")
