import json
import os
import random

# Create a function to generate random data for the metadata
def generate_random_data():
    return {
        "author": "John Doe",
        "creation_date": "2022-09-10",
        "animation_properties": {
            "fps": random.randint(24, 60),
            "resolution": (random.randint(1280, 3840), random.randint(720, 2160))
        },
        "layers": [
            {"name": "Background", "opacity": 1.0},
            {"name": "Foreground", "opacity": 0.8}
        ]
    }

# Create a directory to store the 'ani' files
os.makedirs("./tmp/", exist_ok=True)

# Save the metadata to 'ani' files
for i in range(3):  # Generate 3 'ani' files
    metadata = generate_random_data()
    filename = f"./tmp/file_{i}.ani"
    with open(filename, "w") as file:
        json.dump(metadata, file, indent=4)

print("Generated 'ani' files with more complex metadata successfully.")