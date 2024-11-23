import json
import os

# Define the resolution information
resolution_info = {
    "width": 1920,
    "height": 1080,
    "dpi": 300
}

# Specify the directory to save the file
save_dir = './tmp/'
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Define the filename
filename = os.path.join(save_dir, 'pixdata_resolution.json')

# Write the resolution information to a file in JSON format
with open(filename, 'w') as file:
    json.dump(resolution_info, file)

print(f"Resolution information saved to {filename}")