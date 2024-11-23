from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

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

# Create a list of images with different properties
images = []

# First page - RGB mode
width, height = 800, 600
image1 = Image.new("RGB", (width, height), "red")
images.append(image1)

# Second page - Grayscale mode
image2 = Image.new("L", (width, height), "gray")
images.append(image2)

# Third page - CMYK mode
image3 = Image.new("CMYK", (width, height), (0, 255, 255, 0))
images.append(image3)

# Append custom tags for individual pages
page_custom_tags = [
    {
        701: (TiffTags.FLOAT, 1, (1.0,), False),  # Custom tag for the first page
    },
    {
        702: (TiffTags.FLOAT, 1, (2.0,), False),  # Custom tag for the second page
    },
    {
        703: (TiffTags.FLOAT, 1, (3.0,), False),  # Custom tag for the third page
    },
]

# Save as a multipage TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/complex_multipage_tiff.tiff', True) as tf:
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
        tf.newFrame()

print("Complex multipage TIFF with various color modes and custom tags saved successfully.")