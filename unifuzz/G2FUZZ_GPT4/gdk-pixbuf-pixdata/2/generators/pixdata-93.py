import os
import zipfile
from datetime import datetime

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content to simulate embedding other data
content = """
Embedding Other Data:
This file simulates the process of embedding other data streams, 
such as thumbnails, preview images, or proprietary application-specific information.
"""

# Additional metadata for the file
metadata = {
    "Author": "Data Simulation",
    "Creation Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Description": "This file contains simulated embedded data streams."
}

# Generating a unique filename based on the current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
file_name = f"pixdata_{timestamp}.txt"
file_path = os.path.join('./tmp/', file_name)

# Writing the content and metadata to the file
with open(file_path, 'w') as file:
    file.write("Metadata:\n")
    for key, value in metadata.items():
        file.write(f"{key}: {value}\n")
    file.write("\n")
    file.write(content)

print(f"File saved at {file_path}")

# Compressing the file into a ZIP archive
zip_name = os.path.join('./tmp/', f"pixdata_{timestamp}.zip")
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(file_path, os.path.basename(file_path))

# Optionally, you can delete the original file after compression
# os.remove(file_path)

print(f"Compressed file saved at {zip_name}")