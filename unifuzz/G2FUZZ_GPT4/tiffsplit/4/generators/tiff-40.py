import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a function to create a single image page
def create_image_page(text, font_size=30, img_size=(800, 400), bg_color='white', text_color='black'):
    img = Image.new('RGB', img_size, color=bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Using PIL's default font
    text_x, text_y = 10, 10
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    return img

# Define the text for different pages
texts = [
    "Page 1: Flexibility through Tags - TIFF supports a wide range of image types, resolutions, and color depths.",
    "Page 2: Embedded Thumbnails - TIFF files can contain embedded thumbnail images for quick previews.",
]

# Create multiple pages
pages = [create_image_page(text) for text in texts]

# Save the images as a multi-page TIFF
output_path = './tmp/complex_features.tiff'
pages[0].save(output_path, save_all=True, append_images=pages[1:], compression="tiff_deflate")

print("Multi-page TIFF with custom metadata created.")