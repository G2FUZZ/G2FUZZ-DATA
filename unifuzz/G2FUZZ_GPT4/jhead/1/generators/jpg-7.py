from PIL import Image, ImageDraw
import os

# Ensure ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a simple image using PIL
image_size = (100, 100)
image = Image.new("RGB", image_size, "blue")
draw = ImageDraw.Draw(image)
draw.text((10, 40), "Test", fill="white")

# Compression levels to use
compression_levels = [10, 50, 95]

# Save the image with different compression levels
for compression in compression_levels:
    filename = f"./tmp/test_image_quality_{compression}.jpg"
    image.save(filename, "JPEG", quality=compression)
    print(f"Saved {filename} with compression level {compression}")