from PIL import Image, ImageDraw, ImageSequence
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a simple image for demonstration purposes
def generate_image(mode, size, color, text):
    image = Image.new(mode, size, color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill='black')
    return image

# Generate different images for the TIFF pages
page_1 = generate_image("RGB", (100, 100), "red", "Page 1: RGB")
page_2 = generate_image("L", (100, 100), "gray", "Page 2: Grayscale")
page_3 = generate_image("RGB", (100, 100), "blue", "Page 3: RGB")

# Path for the output TIFF
tiff_output_path = './tmp/complex_structure.tiff'

# Save as multi-page TIFF
page_1.save(
    tiff_output_path,
    save_all=True,
    append_images=[page_2, page_3],
    compression="tiff_deflate",
    dpi=(300.0, 300.0),
    tiffinfo={
        317: 2,
        270: "Multi-page TIFF with different color spaces and custom metadata."
    }
)

# If needed, here's how to read and inspect the generated TIFF file
with Image.open(tiff_output_path) as img:
    for i, page in enumerate(ImageSequence.Iterator(img)):
        print(f"Page {i}: Mode={page.mode}, Size={page.size}")
        # Perform operations per page here
        # page.show()  # Uncomment to display each page