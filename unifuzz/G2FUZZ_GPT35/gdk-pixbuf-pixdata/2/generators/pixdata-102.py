import os
import json
import time

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with complex file structures
features = [
    {"feature": "Color profile: Can include color profiles for accurate color representation across different devices."},
    {"feature": "Metadata: Contains information about the image such as resolution, camera settings, etc."},
    {"feature": "Timestamp: Includes the creation timestamp of the image file."}
]

for i, feature in enumerate(features):
    file_name = f'./tmp/pixdata{i}.txt'
    with open(file_name, 'w') as f:
        data = {
            "feature": feature["feature"],
            "metadata": {
                "resolution": "1920x1080",
                "camera": "Canon EOS 5D Mark IV",
                "aperture": "f/2.8"
            },
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        json.dump(data, f, indent=4)

print("pixdata files with complex file structures generated successfully!")