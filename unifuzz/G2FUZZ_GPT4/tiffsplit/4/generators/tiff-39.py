from PIL import Image, ImageDraw, ImageFont
import os

def create_page(width, height, text, font):
    # Create a single page image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black", font=font)
    return image

def save_multipage_tiff(images, file_path):
    # Save multiple images to a single multi-page TIFF file
    images[0].save(file_path, save_all=True, append_images=images[1:])

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Image dimensions
width, height = 800, 400

# Optionally add a font
# For simplicity, we'll use PIL's default font here. For custom fonts, use ImageFont.truetype("arial.ttf", size=15)
font = ImageFont.load_default()

# Define texts for multiple pages
texts = [
    "1. Lossless Compression: TIFF format supports lossless compression, ensuring that images are not degraded in quality over time.",
    "2. High Color Depth: TIFF images can support color depths from 1 to 24-bit and beyond, making it ideal for high-quality imaging needs.",
    "3. Flexibility: TIFF is a flexible format that can handle images and data within a single file, through the use of tags.",
    "4. Multipage Support: TIFF files can contain multiple images in a single file, which is great for scanning documents.",
    "5. Wide Compatibility: TIFF is supported by many image manipulation programs and is widely used in the imaging industry."
]

# Create image pages
pages = [create_page(width, height, text, font) for text in texts]

# Save the images as a multi-page TIFF
file_path = os.path.join(output_dir, "complex_features_tiff.tiff")
save_multipage_tiff(pages, file_path)

print(f"Multi-page TIFF file saved at: {file_path}")