import numpy as np
from PIL import Image

# Create a numpy array with shape (100, 100, 4) for RGBA image
rgba_image = np.zeros((100, 100, 4), dtype=np.uint8)

# Fill the image with some color (e.g., white) in RGB channels
rgba_image[:, :, :3] = 255

# Add alpha channel with transparency values
alpha_channel = np.linspace(0, 255, 100).astype(np.uint8)
rgba_image[:, :, 3] = alpha_channel[:, np.newaxis]

# Create CMYK Color Space data (for demonstration purposes)
cmyk_image = np.zeros((100, 100, 4), dtype=np.uint8)
# Assume a simple transformation from RGB to CMYK
cmyk_image[:, :, 0] = 255 - rgba_image[:, :, 0]  # Cyan
cmyk_image[:, :, 1] = 255 - rgba_image[:, :, 1]  # Magenta
cmyk_image[:, :, 2] = 255 - rgba_image[:, :, 2]  # Yellow
cmyk_image[:, :, 3] = np.min(rgba_image[:, :, :3], axis=2)  # Key (Black)

# Create PIL Image from CMYK numpy array
cmyk_image_pil = Image.fromarray(cmyk_image, mode='CMYK')

# Define the resolution in DPI (dots per inch)
resolution = (300, 300)  # Set the resolution to 300 DPI

# Set the resolution information in the tiff image
cmyk_image_pil.info["dpi"] = resolution

# Save CMYK image with resolution as a TIFF file
cmyk_image_pil.save("./tmp/cmyk_image_with_resolution.tiff")