import json
import os

# Define the path for saving the files
save_path = './tmp/'

# Ensure the directory exists
os.makedirs(save_path, exist_ok=True)

# Define the pixel data features
pixdata_features = {
    "Compression": {
        "Enabled": True,
        "Type": "lossless"
    }
}

# File name
file_name = 'pixdata_features.json'

# Full path for the file
full_path = os.path.join(save_path, file_name)

# Save the features to a JSON file
with open(full_path, 'w') as file:
    json.dump(pixdata_features, file, indent=4)

print(f"File saved at {full_path}")