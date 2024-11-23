from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def create_page(width, height, text, image_path=None, font_path=None, font_size=20):
    """
    Create a single page for the TIFF document.
    If an image_path is provided, it will embed the image along with the text.
    """
    # Create a new image with white background
    page = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(page)
    
    # Load a custom font or PIL's default
    if font_path:
        font = ImageFont.truetype(font_path, size=font_size)
    else:
        font = ImageFont.load_default()
    
    # Optionally embed an image
    if image_path:
        # Load the image
        img = Image.open(image_path)
        # resize image
        img = img.resize((width // 2, height // 3))
        # Place the image at the bottom center of the page
        page.paste(img, (width // 4, 2 * height // 3))
    
    # Add text to the page
    draw.text((10, 10), text, fill="black", font=font)
    
    return page

def save_multipage_tiff(pages, output_path):
    """
    Save multiple images (pages) as a single multi-page TIFF file.
    """
    # Ensure the first page is saved and subsequent pages are appended
    first_page, *other_pages = pages
    first_page.save(
        output_path,
        save_all=True,
        append_images=other_pages,
        format="TIFF"
    )

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the size of each page
width, height = 800, 600

# Text for each page
texts = [
    "Page 1: TIFF files can contain multiple pages within a single file, making it suitable for document scanning, faxing, and other applications.",
    "Page 2: Each page in a TIFF file can be of different sizes, and can contain both raster and vector images.",
    "Page 3: TIFF files support various compression schemes, such as LZW, JPEG, and PackBits, which can significantly reduce file sizes without losing quality."
]

# Paths to images you might want to include in the TIFF (optional)
image_paths = [None, None, None]  # Assuming you have images to include

# Create each page
pages = [
    create_page(width, height, text, image_path)
    for text, image_path in zip(texts, image_paths)
]

# Apply a simple effect to the first page as an example
pages[0] = pages[0].filter(ImageFilter.CONTOUR)

# Save the multi-page TIFF
file_path = os.path.join(output_dir, "complex_features_tiff.tiff")
save_multipage_tiff(pages, file_path)

print(f"Multi-page TIFF file saved at: {file_path}")