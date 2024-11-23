from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create an image and save it with different compression levels
def create_jpg_with_compression_levels(filename_prefix, compression_levels, bit_depth=8):
    # Create a simple 100x100 pixel image with a single rectangle
    # Adjust color mode based on bit depth
    color_mode = 'RGB' if bit_depth == 8 else 'I;16'
    image = Image.new(color_mode, (100, 100), color='blue')
    draw = ImageDraw.Draw(image)
    draw.rectangle([25, 25, 75, 75], fill="red")
    
    # Iterate over the requested compression levels
    for level in compression_levels:
        # The 'quality' parameter controls the compression level in PIL
        # Quality goes from 1 (worst) to 95 (best), 0 and 100 are system values
        filename = f'./tmp/{filename_prefix}_quality_{level}_bit_{bit_depth}.jpg'
        # When saving, always save as RGB, since JPEG does not support 16-bit directly
        if bit_depth == 12:
            # Convert the 16-bit image (PIL mode 'I;16') to 8-bit 'RGB' for saving
            image_to_save = image.convert('RGB')
            image_to_save.save(filename, 'JPEG', quality=level)
        else:
            image.save(filename, 'JPEG', quality=level)
        print(f'Saved {filename} with quality level {level} and bit depth {bit_depth}')

# Define a list of desired compression levels
compression_levels = [10, 30, 50, 70, 90]

# Call the function with a filename prefix and the list of compression levels for 8-bit depth
create_jpg_with_compression_levels('test_image', compression_levels, 8)

# Extend the function call for 12-bit color depth
# Note: JPEG standard doesn't natively support 12-bit color depth, 
# but this example demonstrates how you might handle higher bit depths before converting to JPEG.
create_jpg_with_compression_levels('test_image', compression_levels, 12)