import os
from PIL import Image, PngImagePlugin

# Create the directory for storing the output if it doesn't already exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new png file
file_path = os.path.join(output_dir, 'with_metadata.png')

# Create a new image
image = Image.new(mode="RGB", size=(200, 200), color=(255, 100, 100))

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Title", "Test Image")
metadata.add_text("Author", "John Doe")
metadata.add_text("Description", "This is an example PNG with metadata")
metadata.add_text("Copyright", "Copyright 2023 John Doe")
metadata.add_itxt("Creation Time", "2023-01-01T12:00:00Z", lang="en", tkey="Creation Time")

# Save the image with metadata
image.save(file_path, "PNG", pnginfo=metadata)

print(f"Image saved with metadata at {file_path}")