from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont, ExifTags
import os, io

# Ensure ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a more complex image using PIL
image_size = (400, 400)
image = Image.new("RGB", image_size, "skyblue")
draw = ImageDraw.Draw(image)

# Optionally, use a specified font if available
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this to a font path available on your system
font = ImageFont.truetype(font_path, 20) if os.path.exists(font_path) else None

# Draw multiple shapes and texts to make it more complex, using the specified font
draw.rectangle([10, 10, 150, 150], fill="yellow", outline="red")
draw.ellipse([250, 10, 390, 150], fill="green", outline="blue")
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
watermark_draw.text((10, 350), watermark_text, fill=(255,255,255,128), font=font)
watermarked_img = Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')

# Compression levels to use
compression_levels = [10, 50, 95]

# Additional feature: Adding EXIF data
exif_data = {
    ExifTags.TAGS[k]: v
    for k, v in {
        271: "Brand",  # Make
        272: "Model",  # Model
        305: "Software",  # Software
        306: '2023:01:01 00:00:00',  # DateTime
    }.items()
}
# Convert EXIF data to bytes
exif_bytes = b"Exif\x00\x00" + bytes(str(exif_data), 'utf-8')

# Save the watermarked image with different compression levels and EXIF data
for compression in compression_levels:
    filename = f"./tmp/complex_test_image_quality_{compression}_watermarked.jpg"
    watermarked_img.save(filename, "JPEG", quality=compression, exif=exif_bytes)
    print(f"Saved {filename} with compression level {compression}, added watermark, and EXIF data")