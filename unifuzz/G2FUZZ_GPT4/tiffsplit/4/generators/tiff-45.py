from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image
def create_image(width, height, color):
    return Image.new("RGB", (width, height), color)

# Define custom tags for each image in a dictionary
# Example of custom tags: (tag_id, tag_type, length, value, writeonce)
# Adjust tag IDs and types according to real needs
custom_tags_images = [
    {
        700: (TiffTags.FLOAT, 1, (1.0,), False),  # Custom tag for first image
        701: (TiffTags.ASCII, 7, ("Tag701",), False)  # Another custom tag for demonstration
    },
    {
        702: (TiffTags.FLOAT, 1, (2.0,), False),  # Custom tag for second image
        703: (TiffTags.ASCII, 7, ("Tag703",), False)  # Another custom tag for demonstration
    }
]

# Image specifications for a multi-page TIFF
image_specs = [
    {"width": 800, "height": 600, "color": "red", "compression": "tiff_adobe_deflate"},
    {"width": 640, "height": 480, "color": "blue", "compression": "tiff_lzw"}
]

# Prepare and save each image with its custom tags and properties
images = []  # List to hold PIL Image objects
for idx, spec in enumerate(image_specs):
    image = create_image(spec["width"], spec["height"], spec["color"])
    info = {
        "compression": spec["compression"],
        "custom": [(tag, value[0], value[1], value[2], value[3]) for tag, value in custom_tags_images[idx].items()]
    }
    images.append(image)

# Save as a multi-page TIFF
images[0].save(
    './tmp/multi_page_tiled_image_with_custom_tags.tiff',
    save_all=True,
    append_images=images[1:],
    **info  # Applying the info of the last image for demonstration; adjust as needed
)

print("Multi-page TIFF image with tiles and custom tags saved successfully.")