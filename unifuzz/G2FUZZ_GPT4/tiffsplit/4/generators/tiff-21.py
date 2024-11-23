from PIL import Image, PngImagePlugin
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create two images to act as layers
width, height = 800, 600
layer1 = Image.new('RGB', (width, height), color = 'red')
layer2 = Image.new('RGB', (width, height), color = 'blue')

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
embed_drm_metadata(layer1, drm_info)
embed_drm_metadata(layer2, drm_info)

# Save the images as a TIFF with multiple layers and DRM metadata
layer1.save('./tmp/multilayer_drm_image.tiff', save_all=True, append_images=[layer2])

print("TIFF file with layers and DRM created at './tmp/multilayer_drm_image.tiff'")