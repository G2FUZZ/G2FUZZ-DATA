from PIL import Image, ImageCms, ImageDraw, ImageFont, PngImagePlugin
import os

def create_gradient_image(width, height, start_color, end_color):
    """
    Creates an image with a vertical gradient filling between `start_color` and `end_color`.
    """
    base = Image.new('RGB', (width, height), start_color)
    top_color = Image.new('RGB', (1, 1), end_color).getpixel((0, 0))

    for y in range(base.size[1]):
        # Calculate the intermediate color at this point
        intermediate_color = tuple(
            int(start_color[i] + (float(y) / (base.size[1] - 1)) * (top_color[i] - start_color[i]))
            for i in range(3)
        )
        base.putpixel((0, y), intermediate_color)

    base = base.resize((width, height), Image.BILINEAR)
    return base

def add_text_overlay(image, text, position, font, font_size, color):
    """
    Adds a text overlay to an existing image.
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font, font_size)
    draw.text(position, text, font=font, fill=color)
    return image

def add_metadata(image, metadata):
    """
    Adds custom metadata to an image.
    """
    meta = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        meta.add_text(key, value)
    image.info["pnginfo"] = meta
    return image

# Load a standard sRGB profile as both the input and output profile
srgb_profile = ImageCms.createProfile("sRGB")

# Create a more complex structure: a stacked image with gradient layers and text overlay
width, height = 400, 400
bottom_layer = create_gradient_image(width, height, (0, 0, 255), (0, 255, 0))  # Blue to Green
top_layer = create_gradient_image(width, height, (255, 255, 0), (255, 0, 0))  # Yellow to Red
composite_image = Image.blend(bottom_layer, top_layer, alpha=0.5)  # Blend images with 50% opacity

# Add a text overlay
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Example font path
composite_image_with_text = add_text_overlay(composite_image, "Complex Structure!", (50, 50), font_path, 20, 'white')

# Convert the image to include the ICC profile with higher quality
image_with_icc = ImageCms.profileToProfile(composite_image_with_text, srgb_profile, srgb_profile, outputMode='RGB')

# Add custom metadata
metadata = {"Description": "This is a complex image structure", "Author": "Your Name"}
image_with_metadata = add_metadata(image_with_icc, metadata)

# Ensure the './tmp/' directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image with ICC profile, custom DPI, and quality to a file
image_with_metadata.save(
    "./tmp/complex_image_with_icc_and_metadata.jpg",
    "JPEG",
    icc_profile=image_with_metadata.info.get('icc_profile'),
    dpi=(300, 300),  # Setting a custom DPI
    quality=95  # Higher quality (default is 75)
)

print("Complex image saved with ICC profile, custom DPI, metadata, and text overlay at './tmp/complex_image_with_icc_and_metadata.jpg'")