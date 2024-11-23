import os
from PIL import Image, ImageDraw, ImageFont, TiffTags, TiffImagePlugin

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

# Create a list of images with different properties and texts
images = []
texts = [
    """
    6. Flexibility through Tags: The format uses a flexible, tag-based structure,
    enabling TIFF to support a wide range of image types, resolutions, and color depths,
    making it highly adaptable to various imaging needs.
    """,
    """
    9. Spot Colors Support: TIFF files can support spot colors, used in printing to ensure accurate reproduction of specific colors that cannot be achieved through the standard CMYK color process alone.
    """,
    """
    6. Security Tags: TIFF allows for the inclusion of security tags which can store encryption keys or digital signatures, adding a layer of security to protect sensitive  information contained within the image file.
    """
]

# Load a font
font = ImageFont.load_default()

for text in texts:
    # Create a new image with white background for each text entry
    img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, fill="black", font=font)
    images.append(img)

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
with TiffImagePlugin.AppendingTiffWriter('./tmp/flexibility_spot_colors_security_tags_support.tiff', True) as tf:
    for i, image in enumerate(images):
        # Prepare the info dictionary to include global custom tags and compression
        info = {
            'custom': [(tag, value[0], value[1], value[2], value[3]) for tag, value in global_custom_tags.items()]
        }
        # Merge page-specific custom tags
        info.update(add_custom_tags(image, page_custom_tags[i]))
        
        # Save the current image as a page within the TIFF
        image.save(tf, format='TIFF', **info)
        tf.newFrame()

print("Multipage TIFF with various texts and custom tags saved successfully.")