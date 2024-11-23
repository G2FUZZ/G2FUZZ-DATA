from PIL import Image, ImageDraw, ImageFont

# Create a new image with a solid color and add text
image = Image.new('RGB', (200, 200), color='green')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((50, 50), "Hello, World!", fill='white', font=font)

# Save the image with different quality settings and file names
for quality in range(50, 100, 10):
    file_path = f'./tmp/complex_image_quality_{quality}.jpg'
    image.save(file_path, quality=quality)

print("JPG files with variable quality settings and text added saved successfully.")