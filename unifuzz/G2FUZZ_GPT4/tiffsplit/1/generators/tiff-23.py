from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an RGB image
rgb_image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square
# Save with strip storage
rgb_image.save('./tmp/rgb_image_strip.tiff', compression="tiff_deflate", save_all=True, append_images=[rgb_image], tiffinfo={259: 1})

# Generate a CMYK image
cmyk_color_space = np.zeros((100, 100, 4), dtype=np.uint8)
cmyk_color_space[:, :, 0] = 255  # High cyan
cmyk_color_space[:, :, 1] = 0    # Low magenta
cmyk_color_space[:, :, 2] = 0    # Low yellow
cmyk_color_space[:, :, 3] = 0    # Low key (black)
cmyk_image = Image.fromarray(cmyk_color_space, 'CMYK')
# Save with strip storage
cmyk_image.save('./tmp/cmyk_image_strip.tiff', compression="tiff_deflate", save_all=True, append_images=[cmyk_image], tiffinfo={259: 1})

# Generate a Grayscale image
gray_image = Image.new("L", (100, 100), 128)  # Medium gray square
# Save with strip storage
gray_image.save('./tmp/gray_image_strip.tiff', compression="tiff_deflate", save_all=True, append_images=[gray_image], tiffinfo={259: 1})