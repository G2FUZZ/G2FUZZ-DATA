from PIL import Image, ImageDraw

# Create an image with a gradient effect
def create_gradient_image(width, height):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for x in range(width):
        r = int(255 * x / width)
        g = int(255 * (width - x) / width)
        b = 128
        draw.line((x, 0, x, height), fill=(r, g, b))

    return img

# Generate and save the gradient image
gradient_img = create_gradient_image(200, 200)
gradient_img.save('./tmp/gradient.jpg')