from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a simple image with different colors
def create_image(color, size=(800, 600)):
    return Image.new('RGB', size, color=color)

# Define a list of colors for each page
colors = [(73, 109, 137), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
images = [create_image(color) for color in colors]

# Define some metadata to be shared across all images
shared_metadata = {
    "software": "Pillow",
    "artist": "Example Creator",
}

# Save the images as a multi-page TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/multi_page_with_metadata.tiff', True) as tf:
    for i, image in enumerate(images):
        # Custom metadata for each page
        metadata = {
            **shared_metadata,  # Unpack shared metadata
            "image_description": f"Page {i + 1} - A sample multi-page TIFF image.",
            "page_number": (i, len(images)),  # Current page number and total pages
        }

        # Prepare metadata for TIFF saving
        info = TiffImagePlugin.ImageFileDirectory_v2()
        for tag, value in metadata.items():
            tag_code = TiffTags.TAGS_V2.get(tag) or TiffTags.TAGS_V2.get(tag.lower())
            if tag_code:
                info[tag_code] = value
            else:
                # Attempt to use custom metadata tags (requires knowing the appropriate tag number)
                custom_tags = {
                    "CustomTag1": 700,  # Example custom tag numbers
                    "CustomTag2": 701,  # These are fictitious and need to be replaced with valid tag numbers
                }
                custom_tag_code = custom_tags.get(tag)
                if custom_tag_code:
                    info[custom_tag_code] = value

        # Save current image to the TIFF file
        image.save(tf, format='TIFF', save_all=True, tiffinfo=info, compression="tiff_lzw")
        tf.newFrame()

print("Multi-page TIFF image with metadata saved successfully.")