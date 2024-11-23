import json
from PIL import Image

# Create a sample metadata dictionary
metadata = {
    "camera_settings": {
        "aperture": "f/2.8",
        "shutter_speed": "1/500",
        "iso": 200
    },
    "location": {
        "latitude": 37.7749,
        "longitude": -122.4194
    }
}

# Convert metadata to JSON string
metadata_json = json.dumps(metadata)

# Convert metadata_json to bytes
metadata_bytes = metadata_json.encode('utf-8')

# Create a new JPG image with metadata
image = Image.new('RGB', (100, 100), color='red')
image.save('./tmp/metadata_example.jpg', exif=metadata_bytes)

print("JPG file with metadata created successfully.")