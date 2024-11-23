from PIL import Image, ImageDraw, ImageFont
import os

def generate_complex_jpeg(output_path, quality, text, font_path, source_images):
    """
    Generates a JPEG file with complex structures including text annotations and composite images.
    
    :param output_path: The file path to save the generated image.
    :param quality: The compression quality for the JPEG image.
    :param text: The text to annotate the image with.
    :param font_path: The file path to the .ttf font file for the text annotation.
    :param source_images: A list of file paths to source images for the composite.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a blank image for the composite
    composite_image = Image.new('RGB', (800, 600), color = (255, 255, 255))
    
    # Load source images, adjust their sizes, and paste them onto the composite image
    for idx, img_path in enumerate(source_images):
        if not os.path.exists(img_path):
            print(f"Source image not found: {img_path}. Skipping this image.")
            continue
        img = Image.open(img_path)
        # Resize image to 400x300 to fit two images side by side on the composite
        img = img.resize((400, 300))
        # Calculate position for each image (side by side)
        position = (idx % 2 * 400, (idx // 2) * 300)
        composite_image.paste(img, position)
    
    # Add text annotation
    if not os.path.exists(font_path):
        print(f"Font file not found: {font_path}. Using default font.")
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, 24)
    
    draw = ImageDraw.Draw(composite_image)
    text_position = (10, 10)  # Top-left corner
    draw.text(text_position, text, fill=(73, 109, 137), font=font)
    
    # Apply a rotation for demonstration (45 degrees)
    composite_image = composite_image.rotate(45, expand=1, fillcolor=(255,255,255))
    
    # Save the image with customizable compression level
    composite_image.save(output_path, 'JPEG', quality=quality)

# Example usage
generate_complex_jpeg(
    './tmp/complex_composite_quality_80.jpg',
    quality=80,
    text="Example Text",
    font_path="/path/to/your/font.ttf",  # Update this to the path of a valid font file
    source_images=["/path/to/image1.jpg", "/path/to/image2.jpg"]  # Update these paths to your source images
)