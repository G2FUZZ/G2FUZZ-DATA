from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Function to create a single page
def create_page(width, height, text, font_path=None, font_size=20, fill_color="black"):
    # Create a new image with white background
    image = Image.new("RGB", (width, height), "white")
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

    # Add the text to the image
    draw.text((10, 10), text, fill=fill_color, font=font)

    # Draw a simple rectangle
    draw.rectangle([50, height - 50, width - 50, height - 10], outline="red", width=3)

    return image

# Create multiple pages with different content
width, height = 800, 600
pages = []

# Page 1 - Default font and a simple message
text1 = "Page 1: This demonstrates a simple TIFF file with a single page."
pages.append(create_page(width, height, text1))

# Page 2 - Custom font, if available, and more complex text
text2 = "Page 2: Here's a more complex example, including a custom font (if available) and a rectangle."
# Provide the path to a .ttf font file if you have one, otherwise, this will fallback to the default font
custom_font_path = "arial.ttf"  # Update this path to a valid font file on your system
pages.append(create_page(width, height, text2, font_path=custom_font_path, font_size=24, fill_color="blue"))

# Save the multi-page TIFF
file_path = os.path.join(output_dir, "multi_page_tiff.tiff")
pages[0].save(file_path, format='TIFF', save_all=True, append_images=pages[1:], compression="tiff_deflate")

print(f"Multi-page TIFF file saved at: {file_path}")