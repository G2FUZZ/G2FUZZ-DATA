from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create an image with a specified color depth
def create_image_with_color_depth(filename, color_depth):
    # Create an RGBA image (red, green, blue, alpha)
    if color_depth in [8, 16]:
        # For 8-bit or 16-bit color depth per channel, we use the 'I' mode for grayscale as a demonstration
        # 'L' mode could also represent 8-bit images, but to showcase variety, we're using 'I' for demonstration.
        mode = 'I;16' if color_depth == 16 else 'L'
        image = Image.new(mode, (100, 100), 'black')
        
        # Modify the image to have some variety in colors/pixels
        for x in range(100):
            for y in range(100):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    # For 16-bit, we can use a higher value since the range is 0-65535. For 8-bit, the range is 0-255.
                    value = 65535 if color_depth == 16 else 255
                    image.putpixel((x, y), value)
    else:
        print(f"Unsupported color depth: {color_depth}. Skipping.")
        return

    # Save the image
    image.save(os.path.join(output_dir, filename))

# Create images with different color depths
create_image_with_color_depth('8bit_image.png', 8)
create_image_with_color_depth('16bit_image.png', 16)

print("Images have been created in ./tmp/ directory.")