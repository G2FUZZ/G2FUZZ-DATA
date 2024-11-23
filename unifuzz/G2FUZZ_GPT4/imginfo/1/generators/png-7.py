from PIL import Image, PngImagePlugin

# Create an image
image = Image.new("RGB", (100, 100), "blue")

# Metadata to be included
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Author", "John Doe")
metadata.add_text("Copyright", "Copyright © 2023 John Doe")
metadata.add_text("Description", "This is an example image with metadata.")

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with metadata
image.save("./tmp/example_with_metadata.png", "PNG", pnginfo=metadata)