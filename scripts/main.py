# scripts/main.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from brutils.config import CENTER_LAT, CENTER_LON, RADIUS_MILES
from brutils.paths import RAW_IMAGE_DIR
from brutils.formatting import format_filename
from scripts.generate_coords import generate_random_coordinates
from scripts.download_image import download_satellite_image
from scripts.detect import run_detection
from scripts.flag_anomalies import log_detections


def main():
    lat, lon = generate_random_coordinates(CENTER_LAT, CENTER_LON, RADIUS_MILES)
    print(f"📍 Scanning: {lat}, {lon}")

    temp_path = download_satellite_image(lat, lon)
    if temp_path:
        filename = format_filename(lat, lon)
        final_path = os.path.join(RAW_IMAGE_DIR, filename)
        os.rename(temp_path, final_path)

        results = run_detection(final_path)

        log_detections(
            results=results,
            lat=lat,
            lon=lon,
            image_path=final_path,
            selected_filters={
                "wildlife": True,
                "structures": False,
                "agriculture": False,
                "ocean": False
            }
        )


if __name__ == "__main__":
    main()
