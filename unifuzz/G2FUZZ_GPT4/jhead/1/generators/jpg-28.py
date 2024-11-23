from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import os, io
from PIL.ExifTags import TAGS

# Ensure ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a more complex image using PIL
image_size = (400, 400)
image = Image.new("RGB", image_size, "skyblue")
draw = ImageDraw.Draw(image)

# Draw multiple shapes and texts to make it more complex
draw.rectangle([10, 10, 150, 150], fill="yellow", outline="red")
draw.ellipse([250, 10, 390, 150], fill="green", outline="blue")
draw.text((10, 200), "Complex Example", fill="white")

# Apply an image filter for a visual effect
image = image.filter(ImageFilter.EDGE_ENHANCE)

# Enhance the contrast of the image
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# Compression levels to use
compression_levels = [10, 50, 95]

# Additional feature: Adding EXIF data
exif_data = {
    271: "Brand",  # Make
    272: "Model",  # Model
    305: "Software",  # Software
    306: '2023:01:01 00:00:00',  # DateTime
}
exif_bytes = {TAGS.get(key, key): value for key, value in exif_data.items()}
exif_bytes = {k: str(v).encode() for k, v in exif_bytes.items()}  # Simplified EXIF bytes creation
exif_io = io.BytesIO()
exif_io.write(b"Exif\x00\x00")
for tag, value in exif_bytes.items():
    exif_io.write(tag.encode() + b"\x00" + value + b"\x00")
exif_final = exif_io.getvalue()

# Save the image with different compression levels and EXIF data
for compression in compression_levels:
    filename = f"./tmp/complex_test_image_quality_{compression}.jpg"
    image.save(filename, "JPEG", quality=compression, exif=exif_final)
    print(f"Saved {filename} with compression level {compression} and added EXIF data")

# Note: The EXIF data handling here is simplified and might not directly work as expected in all viewers.