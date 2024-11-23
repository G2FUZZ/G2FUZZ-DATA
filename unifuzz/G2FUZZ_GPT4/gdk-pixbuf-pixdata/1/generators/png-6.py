from PIL import Image, PngImagePlugin
from datetime import datetime
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode and white background
image = Image.new("RGB", (100, 100), "white")

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Comment", "This is a sample PNG file with metadata.")
metadata.add_text("Creation Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
metadata.add_text("Modification Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Save the image with metadata to ./tmp/
image.save("./tmp/sample_with_metadata.png", "PNG", pnginfo=metadata)