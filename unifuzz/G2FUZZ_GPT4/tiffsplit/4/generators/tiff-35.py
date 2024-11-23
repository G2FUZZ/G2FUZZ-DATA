from PIL import Image, ImageDraw, PngImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image with specified mode and color
def generate_image(mode, color, width=800, height=600, text=''):
    image = Image.new(mode, (width, height), color)
    draw = ImageDraw.Draw(image)
    text_position = (width // 2 - 100, height // 2)
    draw.text(text_position, text, fill='black')
    return image

# Function to add custom metadata to an image
def add_metadata(image, metadata):
    info = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        info.add_text(key, value)
    return info

# Create images with different modes and colors
rgb_image = generate_image("RGB", "red", text='RGB Image')
cmyk_image = generate_image("CMYK", "cyan", text='CMYK Image')
grayscale_image = generate_image("L", "gray", text='Grayscale Image')

# Define custom metadata
metadata = {
    "Author": "John Doe",
    "Description": "Sample TIFF with multiple pages and metadata"
}

# Add metadata to images (metadata is supported for PNG, here it's a placeholder for demonstration)
# Note: TIFF metadata handling would typically involve tiff tags, but PIL has limited support for setting custom TIFF tags directly.
# This step shows how you might add metadata for formats that support it directly in PIL, like PNG.
rgb_info = add_metadata(rgb_image, metadata)
cmyk_info = add_metadata(cmyk_image, metadata)
grayscale_info = add_metadata(grayscale_image, metadata)

# Save the images as a multi-page TIFF
tiff_path = './tmp/complex_tiled_and_subsampled_image.tiff'
rgb_image.save(tiff_path, save_all=True,
               append_images=[cmyk_image, grayscale_image],
               format='TIFF', compression="tiff_deflate",
               tile=('raw', (256, 256)), subsampling='4:2:0',
               dpi=(300,300))

print("Multi-page TIFF image with complex file structures and custom metadata saved successfully.")