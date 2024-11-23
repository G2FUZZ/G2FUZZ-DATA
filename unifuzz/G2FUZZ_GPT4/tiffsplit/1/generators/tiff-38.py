from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Helper function to generate resolution info
def generate_res_info(dpi):
    # Convert DPI to TIFF resolution unit (pixels per inch to pixels per centimeter)
    res = dpi * 2.54 / 10
    return (int(res), int(res))

# Generate an RGB image
rgb_image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square
rgb_res = generate_res_info(300)  # 300 DPI

# Generate a CMYK image
cmyk_color_space = np.zeros((200, 200, 4), dtype=np.uint8)
cmyk_color_space[:, :, 0] = 255  # High cyan
cmyk_color_space[:, :, 1] = 0    # Low magenta
cmyk_color_space[:, :, 2] = 0    # Low yellow
cmyk_color_space[:, :, 3] = 0    # Low key (black)
cmyk_image = Image.fromarray(cmyk_color_space, 'CMYK')
cmyk_res = generate_res_info(600)  # 600 DPI

# Generate a Grayscale image
gray_image = Image.new("L", (50, 50), 128)  # Medium gray square
gray_res = generate_res_info(150)  # 150 DPI

# Prepare metadata
metadata = {
    "Artist": "Python PIL",
    "Software": "Pillow",
    "Description": "Multi-page TIFF with varying color models and resolutions"
}

# Save TIFF with multiple pages, resolutions, and metadata
rgb_image.save(
    './tmp/complex_structure.tiff',
    compression="tiff_deflate",
    save_all=True,
    append_images=[cmyk_image, gray_image],
    dpi=[rgb_res, cmyk_res, gray_res],
    tiffinfo={270: metadata["Description"], 315: metadata["Artist"], 305: metadata["Software"]}
)