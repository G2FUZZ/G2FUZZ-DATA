from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Ensure the output directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a single page with a pattern
def create_page_with_pattern(width, height, pattern_data, font_path=None, font_size=20, fill_color="black"):
    # Convert numpy array pattern to PIL Image
    image = Image.fromarray(pattern_data)  # Corrected variable name here

    draw = ImageDraw.Draw(image)

    # Use a custom font if specified and available
    try:
        if font_path:
            font = ImageFont.truetype(font_path, size=font_size)
        else:
            # Fallback to default font if no custom font is specified
            font = ImageFont.load_default()
    except IOError:
        print(f"Warning: Could not load font from {font_path}. Using default font.")
        font = ImageFont.load_default()

    # Add some text to the image
    text = "Pattern Image"
    draw.text((10, 10), text, fill=fill_color, font=font)

    # Draw a simple border around the image
    draw.rectangle([0, 0, width - 1, height - 1], outline="blue", width=3)

    return image

# Create sample images using numpy and save them as a multi-page TIFF
width, height = 256, 256
pages = []

# Page 1 - A simple pattern
data1 = np.zeros((height, width, 3), dtype=np.uint8)
data1[64:192, 64:192] = [255, 0, 0]  # Red square
data1[128:160, 128:160] = [0, 255, 0]  # Green square
pages.append(create_page_with_pattern(width, height, data1))

# Page 2 - Another simple pattern
data2 = np.zeros((height, width, 3), dtype=np.uint8)
data2[32:224, 32:224] = [0, 0, 255]  # Blue square
data2[96:160, 96:160] = [255, 255, 0]  # Yellow square
pages.append(create_page_with_pattern(width, height, data2))

# Save the multi-page TIFF with document storage options
file_path = './tmp/multi_page_pattern_doc_options.tiff'
compression_options = 'tiff_deflate'
pages[0].save(file_path, format='TIFF', save_all=True, append_images=pages[1:], compression=compression_options, tiffinfo={317: 1, 269: 'Pattern Document'})

print(f"Multi-page TIFF file with document storage options saved at: {file_path}")