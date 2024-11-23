from PIL import Image, ImageDraw, ImageFont

# Create an image with a solid color and add text to it
def add_text_to_image(image, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Use a built-in font
    draw.text((10, 10), text, fill='white', font=font)

# Save the image with different quality settings and text added
quality_settings = [50, 75, 90]
texts = ['Hello', 'World', 'Python']

for idx, quality in enumerate(quality_settings, start=1):
    image = Image.new('RGB', (100, 100), color='blue')
    add_text_to_image(image, texts[idx-1])
    image.save(f'./tmp/image_{idx}_with_text.jpg', quality=quality)