import json
import os

# Generate sample Exif data
exif_data = {
    "camera_model": "Canon EOS 80D",
    "date_time_original": "2022-10-15 14:30:00",
    "location": "New York City"
}

# Create directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save Exif data to a file
filename = 'pixdata_exif.json'
filepath = os.path.join(directory, filename)
with open(filepath, 'w') as file:
    json.dump(exif_data, file, indent=4)

print(f"Generated 'pixdata' file: {filepath}")