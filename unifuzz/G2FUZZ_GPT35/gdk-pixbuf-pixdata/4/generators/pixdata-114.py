import os
import json
import datetime

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the content for the pixdata file with additional features
file_features = {
    "color_profile": "Information about the color characteristics of the image for accurate color reproduction.",
    "metadata": {
        "author": "John Doe",
        "created_at": str(datetime.datetime.now())
    }
}
content = json.dumps(file_features, indent=4)

# Save the content to a file
file_path = os.path.join(directory, 'pixdata_extended.txt')
with open(file_path, 'w') as file:
    file.write(content)

print(f"File 'pixdata_extended.txt' containing the extended features has been saved in the './tmp/' directory.")