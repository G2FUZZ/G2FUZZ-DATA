from PIL import Image, ImageDraw, ImageFont

# Create an image with a gradient effect and additional features
def create_complex_image(width, height):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Generate gradient effect
    for x in range(width):
        r = int(255 * x / width)
        g = int(255 * (width - x) / width)
        b = 128
        draw.line((x, 0, x, height), fill=(r, g, b))

    # Add text to the image using a system font
    font = ImageFont.load_default()
    draw.text((10, 10), "Complex Image", fill=(255, 255, 255), font=font)

    # Add shapes to the image
    draw.rectangle((50, 50, 150, 150), outline=(255, 0, 0))

    return img

# Generate and save the complex image
complex_img = create_complex_image(300, 300)
complex_img.save('./tmp/complex_image.jpg')