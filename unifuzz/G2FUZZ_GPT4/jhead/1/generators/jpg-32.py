from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont, ExifTags
import os, io

# Ensure ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a more complex image using PIL
image_size = (400, 400)
image = Image.new("RGB", image_size, "skyblue")
draw = ImageDraw.Draw(image)

# Use a specific font if available
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this to a font path available on your system
font = ImageFont.truetype(font_path, 24) if os.path.exists(font_path) else None

# Draw multiple shapes and texts to make it more complex
draw.rectangle([10, 10, 150, 150], fill="yellow", outline="red", width=2)
draw.ellipse([250, 10, 390, 150], fill="green", outline="blue", width=2)
draw.text((10, 200), "Complex Example", fill="white", font=font)

# Apply an image filter for a visual effect
image = image.filter(ImageFilter.EDGE_ENHANCE)

# Enhance the contrast of the image
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# Create a watermark
watermark_text = "Watermarked"
watermark = Image.new('RGBA', image.size, (255,255,255,0))
watermark_draw = ImageDraw.Draw(watermark)
watermark_draw.text((300, 350), watermark_text, fill=(255,255,255,128), font=font)
watermarked_img = Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')

# Additional feature: Adding EXIF data with mock approach
exif_data = {
    ExifTags.TAGS[k]: v
    for k, v in {
        271: 'Brand',  # Make
        272: 'Model',  # Model
        306: '2023:01:01 00:00:00',  # DateTime
        305: 'Software',  # Software
    }.items()
}
exif_bytes = b"Exif\x00\x00" + bytes(str(exif_data), 'utf-8')

# Compression levels to use
compression_levels = [10, 50, 95]

# Save the watermarked image with different compression levels and EXIF data
for compression in compression_levels:
    filename = f"./tmp/complex_test_image_quality_{compression}.jpg"
    watermarked_img.save(filename, "JPEG", quality=compression, exif=exif_bytes)
    print(f"Saved {filename} with compression level {compression} and added EXIF data")

# Note: The EXIF data handling here is simplified and might not directly work as expected in all viewers.