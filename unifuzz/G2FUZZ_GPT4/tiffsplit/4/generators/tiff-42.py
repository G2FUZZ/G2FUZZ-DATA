from PIL import Image, ImageDraw, ImageFont, TiffTags, TiffImagePlugin
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to add text to an image
def add_text(img, text, position=(0,0), font_size=30):
    draw = ImageDraw.Draw(img)
    # Use a default font instead of "arial.ttf"
    font = ImageFont.load_default()
    draw.text(position, text, fill="white", font=font)
    return img

# Define a function to add custom tags for individual pages
def add_custom_tags(image, custom_tags):
    if hasattr(TiffImagePlugin, 'WRITE_LIBTIFF'):
        TiffImagePlugin.WRITE_LIBTIFF = True
    info = {
        'custom': [(tag, value[0], value[1], value[2], value[3]) for tag, value in custom_tags.items()]
    }
    return info

# Global custom tags for all pages
global_custom_tags = {
    700: (TiffTags.FLOAT, 1, (0.5,), False),  # Global custom tag for demonstration
}

# Create base images in different color spaces
width, height = 800, 600
images = []

# First page - RGB layer
layer1_rgb = Image.new('RGB', (width, height), color='red')  # RGB layer
images.append(layer1_rgb)

# Second page - CMYK color space and rotate
layer2_cmyk = Image.new('RGB', (width, height), color='blue').convert('CMYK').rotate(45)
images.append(layer2_cmyk)

# Third page - YCbCr color space and add text
layer3_ycbcr = Image.new('YCbCr', (width, height), 'yellow')
layer3_ycbcr = add_text(layer3_ycbcr, "YCbCr Color Space", position=(200, 280), font_size=50)
images.append(layer3_ycbcr)

# Fourth page - Grayscale and manipulate it
layer4_l = Image.new('L', (width, height), color='black')
layer4_l = add_text(layer4_l, "Grayscale", position=(300, 250), font_size=40)
images.append(layer4_l)

# Fifth page - RGBA layer with semi-transparent rectangles
layer5_rgba = Image.new('RGBA', (width, height), color='white')
draw = ImageDraw.Draw(layer5_rgba)
draw.rectangle([50, 50, width - 50, 150], fill=(255, 0, 0, 125))  # Semi-transparent red rectangle
draw.rectangle([50, 200, width - 50, 300], fill=(0, 255, 0, 125))  # Semi-transparent green rectangle
images.append(layer5_rgba)

# Append custom tags for individual pages
page_custom_tags = [
    {},  # No custom tags for the first page
    {},  # No custom tags for the second page
    {},  # No custom tags for the third page
    {},  # No custom tags for the fourth page
    {},  # No custom tags for the fifth page
]

# Save as a multipage TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/complex_multicolor_spaces_image.tiff', True) as tf:
    for i, image in enumerate(images):
        # Prepare the info dictionary to include global custom tags and compression
        info = {
            "compression": "tiff_deflate",  # Use deflate compression; adjust as needed
            'custom': [(tag, value[0], value[1], value[2], value[3]) for tag, value in global_custom_tags.items()]
        }
        # Merge page-specific custom tags
        info.update(add_custom_tags(image, page_custom_tags[i]))
        
        # Save the current image as a page within the TIFF
        image.save(tf, format='TIFF', save_all=True, **info)
        if i < len(images) - 1:  # Prevent adding a new frame after the last image
            tf.newFrame()

print("Complex TIFF file with multiple color spaces and features created at './tmp/complex_multicolor_spaces_image.tiff'")