from PIL import Image, TiffImagePlugin
import os

# Make sure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using PIL
image = Image.new('RGB', (1024, 1024), color='blue')  # Starting with a larger image

# Define metadata using TIFF tag numbers
metadata = {
    270: "A blue square",  # ImageDescription
    282: (96, 1),  # XResolution
    283: (96, 1),  # YResolution
    296: 2,  # ResolutionUnit, 2 signifies inches
    305: "Python PIL",  # Software
    33432: "Copyright 2023",  # Copyright
    315: "Generated by PIL"  # Artist
}

# Prepare the TIFF tags for Pyramid TIFF
tif_info = TiffImagePlugin.ImageFileDirectory_v2()

for tag, value in metadata.items():
    tif_info[tag] = value

# Prepare a list to hold each level of the pyramid
images = [image]

# Generate the pyramid levels by downscaling the image by half each time
# Stop when we reach a minimum size, to avoid too many levels for very small images
min_size = 64
current_size = image.width

while current_size > min_size:
    current_size //= 2
    # Use Image.Resampling.LANCZOS for high-quality downsampling
    images.append(images[-1].resize((current_size, current_size), resample=Image.Resampling.LANCZOS))

# Save the pyramid
image.save('./tmp/generated_image_with_pyramid.tif', save_all=True, append_images=images[1:], tiffinfo=tif_info)

print("Pyramid TIFF image with metadata saved successfully.")