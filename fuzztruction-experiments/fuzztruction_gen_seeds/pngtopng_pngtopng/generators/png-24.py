import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin
import io

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image to demonstrate PNG's robustness to file corruption,
# robust file structure, and tile-based image viewing
# Using a basic plot for simplicity

# Creating a simple plot
plt.figure(figsize=(6, 4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sin(x)')
plt.title('PNG Features: Robustness, File Structure, and Tile-based Image Viewing')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

# Save the plot as a PNG file in memory (not directly to disk)
buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close()

# Textual information to add as metadata in PNG for features
text_to_add = "Text Compression: Textual information within PNG files, like comments and metadata, can be added, reducing the overall file size without affecting the image data."
text_to_add += "\nRobust File Structure: The PNG file structure is designed to be easily recoverable in case of transmission errors, enhancing its reliability for storage and transmission."
text_to_add += "\nTile-based Image Viewing: Specialized extensions or modifications of PNG support tile-based viewing, enabling efficient viewing and manipulation of very large images by loading only the visible portions."

# Use PIL to add text as metadata to the PNG
buf.seek(0)  # Go to the start of the in-memory file
img = Image.open(buf)

# Create a PngInfo object and add the text information
pnginfo = PngImagePlugin.PngInfo()
pnginfo.add_text("Comment", text_to_add)

# Save the modified image with text information as metadata
output_path = os.path.join(output_dir, 'png_features_with_tile_based_viewing.png')
img.save(output_path, pnginfo=pnginfo)

print(f"Image saved at: {output_path}")