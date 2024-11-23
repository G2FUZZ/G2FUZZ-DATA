import json
import os

metadata = {
    "frame_rate": 30,
    "dimensions": {
        "width": 1920,
        "height": 1080
    },
    "other_info": "Additional information related to the animation"
}

# Create a directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Save metadata to ani file
with open(output_dir + 'animation.ani', 'w') as file:
    json.dump(metadata, file)

print("ANI files generated and saved successfully.")