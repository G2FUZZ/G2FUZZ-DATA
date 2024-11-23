from PIL import Image, ImageOps
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a sample image with a specific color mode and pattern
def create_sample_image(width, height, color=(255, 0, 0), color_mode='RGB'):
    data = np.zeros((height, width, 3), dtype=np.uint8)
    if color_mode == 'L':  # Grayscale
        data[:] = 255  # make the image white
        # Add a grayscale pattern
        for i in range(0, height, 10):
            for j in range(0, width, 10):
                data[i:i+5, j:j+5] = 0  # make part of the squares black
        data = np.dot(data[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)  # Convert to grayscale
    elif color_mode == 'RGB':
        # Add a colored pattern
        data[64:192, 64:192] = color  # Square of specified color
    image = Image.fromarray(data, mode=color_mode)
    return image

# Create sample images
width, height = 256, 256
image1 = create_sample_image(width, height, color=(255, 0, 0), color_mode='RGB')
image2 = create_sample_image(width, height, color=(0, 255, 0), color_mode='L')

# List of images to save
images = [image1, image2]

# Define compression options for each page
compression_options = ['tiff_adobe_deflate', 'tiff_lzw']

# Save the images as a multi-page TIFF with different compression schemes and custom tags
filename = './tmp/sample_multi_page_complex_features.tiff'
# Save the first image with additional options, subsequent images are appended
images[0].save(
    filename,
    save_all=True,
    append_images=images[1:],
    compression=compression_options[0],
    tiffinfo={315: b"Artist Name", 270: b"Multi-page TIFF with custom tags and different color modes"},
    resolution=(300.0, 300.0)  # DPI
)

# Update compression for subsequent pages by reopening the TIFF and appending the rest of the images
with Image.open(filename) as img:
    for i, page in enumerate(images[1:], start=1):
        page.save(
            filename,
            save_all=True,
            append_images=[],
            compression=compression_options[i % len(compression_options)],
            tiffinfo={315: b"Artist Name", 270: b"Page with different compression"},
        )

print(f'Saved {filename} with multiple pages, different compression schemes, and custom tags.')