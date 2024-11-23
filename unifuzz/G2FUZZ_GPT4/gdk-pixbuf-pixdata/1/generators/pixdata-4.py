import os
import json

# Create the directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the pixel data feature for compression
pixdata_feature_compression = {
    "Compression": {
        "Description": "Details whether the pixel data is stored in a compressed format to save space.",
        "Type": ["Lossy", "Lossless"]
    }
}

# Define the filename for storing the feature
filename = os.path.join(output_dir, 'pixdata_compression.json')

# Save the feature to a file in JSON format
with open(filename, 'w') as file:
    json.dump(pixdata_feature_compression, file, indent=4)

print(f'File saved: {filename}')