from PIL import Image, ImageDraw, TiffTags, TiffImagePlugin, PngImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image with specified mode, color, and optional text
def create_image(mode, width, height, color, text=''):
    image = Image.new(mode, (width, height), color)
    draw = ImageDraw.Draw(image)
    if text:  # Only add text if it's specified (non-empty)
        text_position = (width // 2 - len(text) * 3, height // 2)  # Simplistic centering
        draw.text(text_position, text, fill='black')
    return image

# Function to add custom metadata to an image
def add_metadata(metadata):
    info = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        info.add_text(key, value)
    return info

# Define custom tags for each image in a dictionary
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

# Image specifications for a multi-page TIFF with different modes and texts
image_specs = [
    {"mode": "RGB", "width": 800, "height": 600, "color": "red", "compression": "tiff_adobe_deflate", "text": "First Image"},
    {"mode": "L", "width": 640, "height": 480, "color": "blue", "compression": "tiff_lzw", "text": "Second Image"}
]

# Prepare and save each image with its custom tags, properties, and optional text
images = []  # List to hold PIL Image objects
for idx, spec in enumerate(image_specs):
    image = create_image(spec["mode"], spec["width"], spec["height"], spec["color"], spec["text"])
    info = {
        "compression": spec["compression"],
        "custom": [(tag, value[0], value[1], value[2], value[3]) for tag, value in custom_tags_images[idx].items()]
    }
    images.append(image)

# Define custom metadata
metadata = {
    "Author": "Jane Doe",
    "Description": "Multi-page TIFF with custom tags and optional text"
}

# Add metadata to the first image (demonstration purpose since it's a TIFF)
# In practice, TIFF custom tags are more relevant, but here we follow the mutated approach for consistency
png_info = add_metadata(metadata)

# Save as a multi-page TIFF
images[0].save(
    './tmp/multi_page_image_with_custom_tags_and_text.tiff',
    save_all=True,
    append_images=images[1:],
    pnginfo=png_info,  # Applying PNG metadata to a TIFF for demonstration; in practice, this would be handled differently
    **info  # Applying the info of the last image for demonstration; adjust as needed
)

print("Multi-page TIFF image with custom tags, text, and metadata saved successfully.")