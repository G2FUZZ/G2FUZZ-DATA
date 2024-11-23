from PIL import Image, GifImagePlugin

# Create or open a directory for saving the GIF
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image
image = Image.new("RGB", (200, 200), "blue")

# Prepare to save the image as a GIF
gif_path = './tmp/metadata_example.gif'

# Specify the comment metadata
comment = b"Copyright 2023, GIF Creator"

# Save the image as a GIF with the comment
image.save(gif_path, save_all=True, append_images=[image], comment=comment)

# Optionally, verify by reopening the GIF and checking the comment
with Image.open(gif_path) as img:
    print("Metadata comment in the GIF:", img.info.get("comment").decode())