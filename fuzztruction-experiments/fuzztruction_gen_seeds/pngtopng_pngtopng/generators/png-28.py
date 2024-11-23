import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin, ImageCms
import io

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image to demonstrate PNG's robustness to file corruption,
# robust file structure, and the inclusion of Embedded ICC Profiles Version 4
# Using a basic plot for simplicity

# Creating a simple plot
plt.figure(figsize=(6, 4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sin(x)')
plt.title('PNG Features: Robustness, File Structure, and ICC Profiles')
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
text_to_add += "\nEmbedded ICC Profiles Version 4: While PNG inherently supports color management through ICC profiles, newer versions of these profiles offer improved accuracy and compatibility across different devices."

# Use PIL to add text as metadata to the PNG
buf.seek(0)  # Go to the start of the in-memory file
img = Image.open(buf)

# Create a PngInfo object and add the text information
pnginfo = PngImagePlugin.PngInfo()
pnginfo.add_text("Comment", text_to_add)

# To add an ICC profile, we first need to create or load an ICC profile
# For demonstration, we'll convert the image to sRGB, which is a common use case
# Note: This assumes the image is not already in sRGB and does not embed an actual ICC v4 profile
# To use a specific ICC v4 profile, you would load it from disk instead
srgb_profile = ImageCms.createProfile("sRGB")
img = ImageCms.profileToProfile(img, srgb_profile, srgb_profile, outputMode='RGB')

# Save the modified image with text information and an ICC profile as metadata
output_path = os.path.join(output_dir, 'png_features_robustness_file_structure_icc_v4.png')
img.save(output_path, pnginfo=pnginfo)

print(f"Image saved at: {output_path}")