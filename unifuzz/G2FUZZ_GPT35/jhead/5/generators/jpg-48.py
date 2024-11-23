from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

# Create a sample image with custom gradient background
def create_custom_gradient(width, height):
    custom_gradient = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = 255 - int(((x + y) / (width + height)) * 255)
            custom_gradient.putpixel((x, y), (r, g, b))
    return custom_gradient

custom_gradient = create_custom_gradient(400, 300)
custom_gradient.save('./tmp/custom_gradient.jpg')

# Apply a blur filter on the custom gradient image
custom_gradient_blurred = custom_gradient.filter(ImageFilter.GaussianBlur(5))
custom_gradient_blurred.save('./tmp/custom_gradient_blurred.jpg')

# Add text overlays to the blurred image
draw = ImageDraw.Draw(custom_gradient_blurred)
font = ImageFont.load_default()

draw.text((50, 50), "Text Overlay 1", fill='white', font=font)
draw.text((200, 150), "Text Overlay 2", fill='yellow', font=font)

# Add geometric shapes
draw.rectangle([100, 100, 200, 200], outline='red')
draw.ellipse([250, 50, 350, 150], outline='blue')

custom_gradient_blurred.save('./tmp/custom_gradient_final.jpg')