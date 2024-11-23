import json
import os
import random

# Create a list of possible tags
tags = ["nature", "animals", "art", "technology", "music"]

# Function to generate random tags
def generate_tags():
    num_tags = random.randint(1, len(tags))
    return random.sample(tags, num_tags)

# Create a dictionary with more complex metadata
metadata = {
    "author": "Jane Smith",
    "creation_date": "2022-09-15",
    "animation_properties": {
        "fps": 60,
        "resolution": (2560, 1440)
    },
    "tags": generate_tags(),
    "description": "A beautiful animation showcasing various elements.",
    "layers": [
        {"name": "Background", "opacity": 1.0},
        {"name": "Foreground", "opacity": 0.8}
    ]
}

# Create a directory to store the 'ani' files
os.makedirs("./tmp/", exist_ok=True)

# Save the metadata to 'ani' files
for i in range(3):  # Generate 3 'ani' files
    filename = f"./tmp/file_{i}.ani"
    with open(filename, "w") as file:
        json.dump(metadata, file, indent=4)

print("Generated 'ani' files with more complex metadata successfully.")