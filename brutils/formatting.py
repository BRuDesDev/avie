# brutils/formatting.py
# utils/formatting.py

from datetime import datetime, timezone


def format_filename(lat, lon, prefix="bes", extension=".jpg"):
    lat_str = f"{lat:.5f}"
    lon_str = f"{lon:.5f}"
    current_time = datetime.now(timezone.utc)
    timestamp = current_time.strftime("%Y-%m-%dT%H-%M-%S")
    return f"{prefix}-{lat_str}--{lon_str}--{timestamp}{extension}"
