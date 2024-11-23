import os
from PIL import Image, PngImagePlugin

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Author", "John Doe")
metadata.add_text("Copyright", "2023 John Doe")
metadata.add_text("Description", "This is a sample TGA image with metadata.")
metadata.add_text("Tags", "sample;example;demo")

# Save the image with metadata
# Note: The standard PIL does not directly support saving metadata in TGA format.
# As a workaround, we'll save it as PNG first, then convert it to TGA.
png_path = "./tmp/sample_with_metadata.png"
tga_path = "./tmp/sample_with_metadata.tga"
img.save(png_path, "PNG", pnginfo=metadata)

# Convert PNG to TGA
img_with_metadata = Image.open(png_path)
img_with_metadata.save(tga_path, "TGA")

# Cleanup the intermediate PNG file
os.remove(png_path)

print("TGA file with metadata has been saved.")