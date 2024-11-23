from PIL import Image, TiffImagePlugin
import os

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a simple image for demonstration (gradient)
width, height = 256, 256
image = Image.new("RGB", (width, height))
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (int(x / width * 255), int(y / height * 255), 112))

# Define compression types to demonstrate
compression_types = {
    "none": "tiff",
    "jpeg": "jpeg",
    "lzw": "tiff_lzw",
    "packbits": "tiff_packbits",
    "deflate": "tiff_deflate",
}

# Save the image using different compression schemes
for comp_type, tiff_compression in compression_types.items():
    filename = f"example_{comp_type}.tiff"
    filepath = os.path.join(output_dir, filename)
    
    # Save the image with the specified compression
    image.save(filepath, format="TIFF", compression=tiff_compression)
    
    print(f"Saved {filename} with {comp_type} compression")