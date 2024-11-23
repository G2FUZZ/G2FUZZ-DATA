import os
import json

# Create the `./tmp/` directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define a dictionary to represent the pixdata with the Compression feature
pixdata_info = {
    "Compression": {
        "Type": "Lossless",
        "Description": "Reduces file size without losing any data"
    }
}

# Convert the dictionary to a string in JSON format
pixdata_json = json.dumps(pixdata_info, indent=4)

# Save the generated JSON string into a file in the `./tmp/` directory
with open('./tmp/pixdata_compression.json', 'w') as file:
    file.write(pixdata_json)