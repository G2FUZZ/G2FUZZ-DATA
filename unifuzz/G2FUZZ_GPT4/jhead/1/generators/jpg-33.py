from PIL import Image, ImageDraw, ImageFont, ExifTags
import os

def create_complex_jpg_with_extras(filename):
    # Create a new image with RGB mode and a modified background color
    width, height = 800, 600
    image = Image.new("RGB", (width, height), "skyblue")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Generate a radial gradient
    center_x, center_y = width / 2, height / 2
    for y in range(height):
        for x in range(width):
            # Calculate distance to the center
            distance = ((center_x - x) ** 2 + (center_y - y) ** 2) ** 0.5
            # Normalize distance and calculate color
            distance = min(1, distance / (width / 2))
            color = int(255 * (1 - distance))
            draw.point((x, y), fill=(color, color, color))

    # Add a text overlay with custom font path
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    try:
        font = ImageFont.truetype(font_path, 40) if os.path.exists(font_path) else ImageFont.load_default()
    except IOError:
        font = ImageFont.load_default()
    text = "Complex JPG with Extras"
    textwidth, textheight = draw.textsize(text, font=font)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2
    draw.text((x, y), text, font=font, fill="white")

    # Create a watermark
    watermark_text = "Watermarked"
    watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text((600, 560), watermark_text, fill=(255, 255, 255, 128), font=font)
    watermarked_img = Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')

    # Embed EXIF data
    exif_data = {
        ExifTags.TAGS[k]: v
        for k, v in {
            271: 'My Camera Brand',
            272: 'My Camera Model',
            306: '2023:01:01 00:00:00',
        }.items()
    }
    exif_bytes = b"Exif\x00\x00" + bytes(str(exif_data), 'utf-8')

    # Add more compression options and save with EXIF data
    watermarked_img.save(filename, "JPEG", exif=exif_bytes, quality=95, optimize=True, progressive=True)

# Ensure the ./tmp/ directory exists or create it
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Filepath to save the image
filepath = './tmp/complex_image_with_extras.jpg'

# Create and save a complex JPEG with extras
create_complex_jpg_with_extras(filepath)
print(f"Complex JPEG with extras saved to {filepath}")