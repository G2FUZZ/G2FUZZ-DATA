import json
import os

# Create a dictionary for metadata
metadata = {
    "author": "John Doe",
    "creation_date": "2022-09-10",
    "animation_properties": {
        "fps": 30,
        "resolution": (1920, 1080)
    }
}

# Create a directory to store the 'ani' files
os.makedirs("./tmp/", exist_ok=True)

# Save the metadata to 'ani' files
for i in range(3):  # Generate 3 'ani' files
    filename = f"./tmp/file_{i}.ani"
    with open(filename, "w") as file:
        json.dump(metadata, file)

print("Generated 'ani' files with metadata successfully.")