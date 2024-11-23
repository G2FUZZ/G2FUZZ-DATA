from PIL import Image, ImageDraw, ImageFont

# Create an image with text
def create_image_with_text(text, text_color, background_color, font_size, file_path):
    image = Image.new('RGB', (200, 200), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((50, 50), text, fill=text_color, font=font)
    image.save(file_path)

create_image_with_text('Hello World!', 'black', 'white', 20, './tmp/text_image.jpg')

print('JPG file with text added has been generated and saved in ./tmp/')