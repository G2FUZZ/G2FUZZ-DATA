from PIL import Image, ImageDraw, ImageFilter

# Create a new image with 24-bit true color support
image = Image.new('RGB', (200, 200), color='white')

# Draw text on the image
draw = ImageDraw.Draw(image)
draw.text((50, 50), "Hello, World!", fill='black')

# Apply image filters
image_blur = image.filter(ImageFilter.BLUR)
image_sharpen = image.filter(ImageFilter.SHARPEN)

# Save the images with different filters applied
image.save('./tmp/complex_image.png')
image_blur.save('./tmp/complex_image_blur.png')
image_sharpen.save('./tmp/complex_image_sharpen.png')