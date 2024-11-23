from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Create a sample image with a gradient background
image = Image.new('RGB', (400, 300))
draw = ImageDraw.Draw(image)
for y in range(image.height):
    draw.line((0, y, image.width, y), fill=(y, 0, 0))

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)

# Add text overlay to the image using a default font
font = ImageFont.load_default()
draw = ImageDraw.Draw(blurred_image)
draw.text((50, 50), "Generated Image", fill=(255, 255, 255), font=font)

# Save the final image with complex features
blurred_image.save('./tmp/complex_sample.jpg')