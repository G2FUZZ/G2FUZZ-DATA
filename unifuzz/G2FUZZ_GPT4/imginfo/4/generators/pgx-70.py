import os
import json
from PIL import Image
import numpy as np

# Define the directory where the files will be saved
output_dir = "./tmp/"
# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the filename
filename = "features.pgx"
# Define the metadata filename
metadata_filename = "features_metadata.json"

# Path to the files
file_path = os.path.join(output_dir, filename)
metadata_path = os.path.join(output_dir, metadata_filename)

# Define image size and color depth for the simulated content
image_size = (100, 100)  # 100x100 pixels
color_depth = 16  # 16-bit grayscale image

# Generate a random image for demonstration (using numpy)
np.random.seed(0)  # For reproducibility
image_data = np.random.randint(0, 2**color_depth, image_size, dtype=np.uint16)

# Save the image data to a PGX file using PIL
try:
    # Create an image object from the numpy array
    image = Image.fromarray(image_data)
    # Save the image in the PGX format
    image.save(file_path, "JPEG2000", quality_mode='dB', quality_layers=[80])
    print(f"Image file saved to {file_path}")
except Exception as e:
    print(f"Failed to save the image file: {e}")

# Define metadata for the file
metadata = {
    "filename": filename,
    "image_size": image_size,
    "color_depth": color_depth,
    "description": "This is a simulated image file for demonstration purposes.",
    "features": [
        "Flexibility in Usage: Specialized fields where image integrity and raw data manipulation are crucial, such as medical imaging, digital archiving, and scientific research."
    ]
}

# Write the metadata to a JSON file
try:
    with open(metadata_path, "w") as json_file:
        json.dump(metadata, json_file, indent=4)
    print(f"Metadata saved to {metadata_path}")
except Exception as e:
    print(f"Failed to save the metadata file: {e}")