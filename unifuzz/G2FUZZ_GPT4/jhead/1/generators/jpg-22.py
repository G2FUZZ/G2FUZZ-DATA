from PIL import Image, ImageDraw, ImageFont, ExifTags
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image settings
image_width, image_height = 800, 200
background_color = (235, 235, 255)  # Slightly modified background color for a subtle difference
font_color = (0, 0, 0)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust the font path as needed
font_size = 20

# Initialize a new image with a modified background color
image = Image.new("RGB", (image_width, image_height), color=background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype(font_path, font_size) if os.path.exists(font_path) else None
except IOError:
    font = ImageFont.load_default()

# Text to be drawn
text = "8. Widespread Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers."

# Calculate text width and height to position it on the center
text_width, text_height = draw.textsize(text, font=font)
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2

# Draw the text onto the image
draw.text((x, y), text, fill=font_color, font=font)

# Create a watermark
watermark_text = "Watermarked"
watermark = Image.new('RGBA', image.size, (255,255,255,0))
watermark_draw = ImageDraw.Draw(watermark)
watermark_draw.text((image_width - 150, image_height - 30), watermark_text, fill=(0,0,0,128), font=font)
watermarked_img = Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')

# Create a rotated thumbnail of the base image
thumbnail_size = (128, 128)
thumbnail = watermarked_img.copy()
thumbnail.thumbnail(thumbnail_size)
thumbnail = thumbnail.rotate(45, expand=True)

# Embed EXIF data
# Note: The 'Pillow' library does not directly support editing EXIF data.
exif_data = {
    # Mock EXIF data; in practice, you would populate this with real details.
    ExifTags.TAGS[k]: v
    for k, v in {
        271: 'My Camera Brand',  # Make
        272: 'My Camera Model',  # Model
        306: '2023:01:01 00:00:00',  # DateTime
    }.items()
}
exif_bytes = b"Exif\x00\x00" + bytes(str(exif_data), 'utf-8')

# Save the image with watermark and mock EXIF data
output_path = os.path.join(output_dir, "widespread_compatibility_with_watermark.jpg")
watermarked_img.save(output_path, 'JPEG', exif=exif_bytes)

print(f"Image with watermark and EXIF data saved to {output_path}")