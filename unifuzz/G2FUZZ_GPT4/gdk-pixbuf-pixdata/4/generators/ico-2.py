from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an icon with specified color depth
def generate_icon(color_depth, file_name):
    # Create an image 64x64 pixels
    if color_depth in ['1', 'P']:  # Monochrome or 256 colors
        mode = 'P'  # Using 'P' mode for both to utilize palette-based images
        size = (64, 64)
        image = Image.new(mode, size, "white")
        draw = ImageDraw.Draw(image)

        # Draw a simple shape
        draw.rectangle([16, 16, 48, 48], fill="black")

        if color_depth == '1':  # Convert to 1-bit for monochrome
            image = image.convert('1')
    else:
        size = (64, 64)
        image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent background for 32-bit
        draw = ImageDraw.Draw(image)

        # Draw a simple shape with different colors based on color depth
        if color_depth == '16':
            draw.rectangle([16, 16, 48, 48], fill=(0, 0, 255))  # Simple blue for demonstration
        elif color_depth == '256':
            draw.rectangle([16, 16, 48, 48], fill=(0, 255, 0))  # Simple green for demonstration
        elif color_depth == '24-bit':
            draw.rectangle([16, 16, 48, 48], fill=(255, 165, 0))  # Orange
        else:  # 32-bit
            draw.rectangle([16, 16, 48, 48], fill=(255, 20, 147, 128))  # Semi-transparent pink

    # Save the image
    image.save(f'./tmp/{file_name}.ico', format='ICO', sizes=[(64, 64)])

# Generate icons with various color depths
generate_icon('1', 'monochrome_icon')        # Monochrome
generate_icon('16', '16_color_icon')         # 16 colors
generate_icon('256', '256_color_icon')       # 256 colors
generate_icon('24-bit', '24_bit_color_icon') # 24-bit color
generate_icon('32-bit', '32_bit_color_icon') # 32-bit color (with transparency)