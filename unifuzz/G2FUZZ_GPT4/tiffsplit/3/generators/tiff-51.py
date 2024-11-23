from PIL import Image, ImageDraw, TiffImagePlugin, TiffTags
import os

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def create_image_with_shape(color, shape, size=(100, 100)):
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    if shape == "circle":
        radius = min(size) // 3
        left_up_point = (size[0]//2 - radius, size[1]//2 - radius)
        right_down_point = (size[0]//2 + radius, size[1]//2 + radius)
        draw.ellipse([left_up_point, right_down_point], fill=color)
    elif shape == "square":
        edge_length = min(size) // 2
        left_up_point = (size[0]//2 - edge_length//2, size[1]//2 - edge_length//2)
        right_down_point = (size[0]//2 + edge_length//2, size[1]//2 + edge_length//2)
        draw.rectangle([left_up_point, right_down_point], fill=color)

    return image

shapes = [("red", "circle", (200, 200)), ("blue", "square", (150, 150))]
images = [create_image_with_shape(color, shape, size) for color, shape, size in shapes]

# Shared metadata for all layers
shared_metadata = {
    "software": "Pillow",
    "artist": "Example Layer Creator",
}

# Save the images as a multi-page TIFF with layers and metadata
with TiffImagePlugin.AppendingTiffWriter('./tmp/complex_multi_layer_with_metadata.tiff', True) as tf:
    for i, image in enumerate(images):
        # Custom metadata for each layer
        metadata = {
            **shared_metadata,  # Unpack shared metadata
            "image_description": f"Layer {i + 1} - A complex layered TIFF image.",
            "layer_number": (i, len(images)),  # Current layer number and total layers
        }

        # Prepare metadata for TIFF saving
        info = TiffImagePlugin.ImageFileDirectory_v2()
        for tag, value in metadata.items():
            tag_code = TiffTags.TAGS_V2.get(tag) or TiffTags.TAGS_V2.get(tag.lower())
            if tag_code:
                info[tag_code] = value
            else:
                # Handle custom metadata tags
                custom_tags = {
                    # Custom tag examples; replace with valid tag numbers for real applications
                }
                custom_tag_code = custom_tags.get(tag)
                if custom_tag_code:
                    info[custom_tag_code] = value

        # Save current layer to the TIFF file
        image.save(tf, format='TIFF', save_all=True, tiffinfo=info, compression="tiff_lzw")
        if i < len(images) - 1:  # Avoid adding a new frame after the last image
            tf.newFrame()

print("Complex TIFF with layers and metadata created at ./tmp/complex_multi_layer_with_metadata.tiff")