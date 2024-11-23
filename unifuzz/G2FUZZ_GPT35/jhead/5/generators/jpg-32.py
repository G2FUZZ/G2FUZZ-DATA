from PIL import Image, ImageDraw, ImageFont

# Create a new image with a solid color
image = Image.new('RGB', (200, 200), color='blue')

# Draw text and shapes on the image
draw = ImageDraw.Draw(image)
text = "Hello, JPG!"

# Use a built-in font
font = ImageFont.load_default()
draw.text((50, 50), text, fill='white', font=font)
draw.rectangle([20, 20, 100, 100], outline='red', width=2)

# Save the image with different compression ratios
for quality in range(10, 100, 10):
    image.save(f'./tmp/complex_image_{quality}.jpg', quality=quality)

print("JPG files with text and shapes added have been saved in the './tmp/' directory.")