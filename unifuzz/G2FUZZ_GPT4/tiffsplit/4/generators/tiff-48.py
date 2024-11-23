from PIL import Image, ImageDraw, ImageFont, PngImagePlugin
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to add text to an image
def add_text(img, text, position=(0,0), font_size=30):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text(position, text, fill="white", font=font)
    return img

# Create base images in different color spaces
width, height = 800, 600
layer1_rgb = Image.new('RGB', (width, height), color='red')  # RGB layer
layer2_rgb = Image.new('RGB', (width, height), color='blue')  # RGB layer

# Prepare DRM metadata
drm_info = {
    "Copyright": "Copyright 2023 by the Creator",
    "UsageRights": "Viewing permitted, but no modifications or distribution allowed.",
    "DRMProtected": "True"
}

# Function to embed DRM metadata into an image
def embed_drm_metadata(image, metadata):
    if image.format == 'TIFF':
        for key, value in metadata.items():
            image.tag_v2[PngImagePlugin.PngInfo()][key] = value
    else:
        # For non-TIFF images, if needed, other metadata embedding approaches can be used.
        pass

# Embed DRM metadata into both layers
embed_drm_metadata(layer1_rgb, drm_info)
embed_drm_metadata(layer2_rgb, drm_info)

# Convert layer2 to CMYK color space, rotate, and add text with DRM notice
layer2_cmyk = layer2_rgb.convert('CMYK').rotate(45)
layer2_cmyk = add_text(layer2_cmyk, "DRM Protected", position=(200, 280), font_size=50)

# Create an L layer (grayscale), add text, and apply DRM metadata
layer3_l = Image.new('L', (width, height), color='black')
layer3_l = add_text(layer3_l, "Grayscale DRM", position=(300, 250), font_size=40)
embed_drm_metadata(layer3_l, drm_info)

# Adding an RGBA layer with semi-transparent rectangles and DRM metadata
layer4_rgba = Image.new('RGBA', (width, height), color='white')
draw = ImageDraw.Draw(layer4_rgba)
draw.rectangle([50, 50, width - 50, 150], fill=(255, 0, 0, 125))  # Semi-transparent red rectangle
draw.rectangle([50, 200, width - 50, 300], fill=(0, 255, 0, 125))  # Semi-transparent green rectangle
embed_drm_metadata(layer4_rgba, drm_info)

# Save the images as a multi-page TIFF with various properties and DRM metadata
layer1_rgb.save('./tmp/complex_multilayer_drm_image.tiff', save_all=True, append_images=[layer2_cmyk, layer3_l, layer4_rgba], compression="tiff_deflate")

print("Complex TIFF file with multiple layers, DRM, and additional features created at './tmp/complex_multilayer_drm_image.tiff'")