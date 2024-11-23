import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin
import io

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image to demonstrate PNG's robustness to file corruption
# Using a basic plot for simplicity

# Creating a simple plot
plt.figure(figsize=(6, 4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sin(x)')
plt.title('Robustness to File Corruption: PNG Format')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

# Save the plot as a PNG file in memory (not directly to disk)
buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close()

# Textual information to add as metadata in PNG
text_to_add = "Text Compression: Textual information within PNG files, like comments and metadata, can be added, reducing the overall file size without affecting the image data."

# Use PIL to add text as metadata to the PNG
buf.seek(0)  # Go to the start of the in-memory file
img = Image.open(buf)

# Create a PngInfo object and add the text information
pnginfo = PngImagePlugin.PngInfo()
pnginfo.add_text("Comment", text_to_add)

# Save the modified image with text information as metadata
output_path = os.path.join(output_dir, 'robustness_to_file_corruption_with_compression.png')
img.save(output_path, pnginfo=pnginfo)

print(f"Image saved at: {output_path}")