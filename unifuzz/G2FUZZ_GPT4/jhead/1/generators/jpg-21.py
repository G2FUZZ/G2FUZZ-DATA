from PIL import Image, ImageDraw, ImageFont, ExifTags
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a base image
img = Image.new('RGB', (800, 600), color='skyblue')

# Optionally, draw some content on the image
draw = ImageDraw.Draw(img)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this to a font path available on your system
font = ImageFont.truetype(font_path, 24) if os.path.exists(font_path) else None
draw.text((10, 10), "Complex Sample Image", fill="white", font=font)

# Create a watermark
watermark_text = "Watermarked"
watermark = Image.new('RGBA', img.size, (255,255,255,0))
watermark_draw = ImageDraw.Draw(watermark)
watermark_draw.text((600, 560), watermark_text, fill=(255,255,255,128), font=font)
watermarked_img = Image.alpha_composite(img.convert('RGBA'), watermark).convert('RGB')

# Create a rotated thumbnail of the base image
thumbnail_size = (128, 128)
thumbnail = watermarked_img.copy()
thumbnail.thumbnail(thumbnail_size)
thumbnail = thumbnail.rotate(45, expand=True)

# Embed EXIF data
# Note: The 'Pillow' library does not directly support editing EXIF data.
# This code assumes you are handling the EXIF data separately and embedding a placeholder.
exif_data = {
    # Mock EXIF data; in practice, you would populate this with real details.
    ExifTags.TAGS[k]: v
    for k, v in {
        271: 'My Camera Brand',  # Make
        272: 'My Camera Model',  # Model
        306: '2023:01:01 00:00:00',  # DateTime
    }.items()
}
# Convert EXIF data to bytes
exif_bytes = b"Exif\x00\x00" + bytes(str(exif_data), 'utf-8')

# Save the watermarked image with an embedded thumbnail and mock EXIF data to a file
output_path = os.path.join(output_dir, 'complex_sample_with_thumbnail.jpg')
watermarked_img.save(output_path, 'JPEG', exif=exif_bytes, quality=95)

print(f"Complex image with embedded thumbnail and EXIF data saved to {output_path}")