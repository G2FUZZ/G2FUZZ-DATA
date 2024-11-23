from PIL import Image, ImageDraw, ImageFont

# Create a new image with a solid color and add text overlay
def create_image_with_text(width, height, color, text):
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font)
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, text, font=font, fill='white')
    return image

# Save the image with different quality settings and text overlay
for quality in range(50, 100, 10):
    file_path = f'./tmp/image_quality_{quality}_with_text.jpg'
    image = create_image_with_text(100, 100, 'blue', f'Quality: {quality}')
    image.save(file_path, quality=quality)

print("JPG files with variable quality settings and text overlay saved successfully.")