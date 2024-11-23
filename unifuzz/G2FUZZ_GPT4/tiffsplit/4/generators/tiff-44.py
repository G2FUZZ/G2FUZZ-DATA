import os
from PIL import Image, ImageDraw, ImageFont, TiffTags, TiffImagePlugin

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create an image page
def create_image_page(width, height, text, font):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color='white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(img)

    # Position for the text
    text_x, text_y = 10, 10

    # Apply text onto the image
    draw.text((text_x, text_y), text, fill="black", font=font)

    return img

# Define texts for each page
texts = [
    "Page 1: Flexibility through Tags",
    "Page 2: Spot Colors Support"
]

# Load a font
font = ImageFont.load_default()

# Page dimensions
width, height = 800, 400

# Create a list of image pages
pages = [create_image_page(width, height, text, font) for text in texts]

# Define custom metadata
custom_metadata = {
    270: "Multi-page TIFF example with custom metadata"  # 270 is the tag number for ImageDescription
}

# Save the images as a multi-page TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/multi_page_custom_metadata.tiff', True) as tf:
    for page in pages:
        # Adding custom metadata to each page
        info = TiffImagePlugin.ImageFileDirectory_v2()
        for tag, value in custom_metadata.items():
            info[tag] = value
        page.save(tf, tiffinfo=info)
        tf.newFrame()

print("TIFF file with multiple pages and custom metadata has been created.")