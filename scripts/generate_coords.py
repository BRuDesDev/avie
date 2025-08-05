# scripts/generate_coords.py

import random
from geopy.distance import distance
from geopy.point import Point


def generate_random_coordinates(center_lat, center_lon, radius_miles):
    """
    Generate random coordinates within a circle of given radius around a center point.
    """
    center = Point(center_lat, center_lon)
    angle = random.uniform(0, 360)
    dist = random.uniform(0, radius_miles)
    destination = distance(miles=dist).destination(center, angle)
    return destination.latitude, destination.longitude


# Example usage
if __name__ == "__main__":
    lat, lon = generate_random_coordinates(40.7128, -74.0060, 5)  # Around NYC
    print(f"Generated coordinates: {lat}, {lon}")
