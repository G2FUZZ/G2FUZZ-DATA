from PIL import Image, ImageDraw, ImageFont

# Create a new image with a solid color and add text
image = Image.new('RGB', (200, 200), color='yellow')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((80, 80), "Complex Structure", fill='black', font=font)

# Save the image with different compression ratios
for quality in range(10, 100, 10):
    image.save(f'./tmp/complex_image_{quality}.jpg', quality=quality)

print("JPG files with different compression ratios and text overlay have been saved in the './tmp/' directory.")