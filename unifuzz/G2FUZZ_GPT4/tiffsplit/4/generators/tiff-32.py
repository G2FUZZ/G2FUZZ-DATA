from PIL import Image, ImageDraw, ImageFont, ImageSequence
import os

def create_page(width, height, text, font):
    """
    Create a single page for the TIFF file.
    """
    # Create a new image with white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Add text to the image
    draw.text((10, 10), text, fill="black", font=font)
    
    return image

def save_multipage_tiff(images, file_path):
    """
    Save multiple images to a single multi-page TIFF file.
    """
    # Ensure the first image is saved with the save_all=True and append_images=other_images
    images[0].save(file_path, save_all=True, append_images=images[1:], format='TIFF')

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a new TIFF image
width, height = 800, 600

# Optionally add a font
# For simplicity, we'll use PIL's default font here. For custom fonts, use ImageFont.truetype()
# font = ImageFont.truetype("arial.ttf", size=15)
font = ImageFont.load_default()

# Define texts for each page
texts = [
    "Page 1: Interoperability is key in multi-platform environments.",
    "Page 2: TIFF supports various compression schemes, making it versatile.",
    "Page 3: Metadata in TIFF files can include copyright information, timestamps, and more.",
]

# Create pages
pages = [create_page(width, height, text, font) for text in texts]

# Save the multi-page TIFF
file_path = os.path.join(output_dir, "multi_page_tiff.tiff")
save_multipage_tiff(pages, file_path)

print(f"Multi-page TIFF file saved at: {file_path}")