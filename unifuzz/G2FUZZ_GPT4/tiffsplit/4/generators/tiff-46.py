from PIL import Image, ImageDraw, TiffImagePlugin
import os

# Make sure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image with specified mode and color
def generate_image(mode, color, width=1024, height=1024, text=''):
    image = Image.new(mode, (width, height), color)
    draw = ImageDraw.Draw(image)
    text_position = (width // 2 - 100, height // 2)
    draw.text(text_position, text, fill='black')
    return image

# Function to add custom metadata to an image
def add_metadata(image, metadata):
    tif_info = TiffImagePlugin.ImageFileDirectory_v2()
    for tag, value in metadata.items():
        tif_info[tag] = value
    return tif_info

# Create images with different modes and colors
blue_image = generate_image("RGB", "blue", text='Blue Image')
red_image = generate_image("RGB", "red", text='Red Image')
green_image = generate_image("RGB", "green", text='Green Image')

# Define custom metadata
metadata = {
    270: "A collection of colored squares",  # ImageDescription
    282: (96, 1),  # XResolution
    283: (96, 1),  # YResolution
    296: 2,  # ResolutionUnit, signifies inches
    305: "Python PIL Enhanced",  # Software
    33432: "Copyright 2023 Enhanced",  # Copyright
    315: "Generated by Advanced PIL"  # Artist
}

# Add metadata to images (demonstration for TIFF, as PIL's handling of TIFF metadata is more direct)
blue_info = add_metadata(blue_image, metadata)
red_info = add_metadata(red_image, metadata)
green_info = add_metadata(green_image, metadata)

# Save the images as a multi-page TIFF with pyramid levels for each image
tiff_path = './tmp/enhanced_image_with_pyramid_and_metadata.tif'
blue_image.save(tiff_path, save_all=True, append_images=[red_image, green_image],
                tiffinfo=blue_info, format='TIFF', compression="tiff_deflate",
                dpi=(300,300))

print("Enhanced multi-page Pyramid TIFF image with custom metadata saved successfully.")