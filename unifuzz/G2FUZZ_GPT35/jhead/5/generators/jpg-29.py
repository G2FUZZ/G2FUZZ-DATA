from PIL import Image, ImageDraw, ImageFont

# Create an image with multiple text layers
image = Image.new('RGB', (400, 400), color='white')
draw = ImageDraw.Draw(image)

# Define fonts for different text layers
font1 = ImageFont.load_default()  # Using default font
font2 = ImageFont.load_default()  # Using default font
font3 = ImageFont.load_default()  # Using default font

# Add multiple text layers with different fonts and colors
draw.text((50, 50), "Text Layer 1", fill='black', font=font1)
draw.text((100, 100), "Text Layer 2", fill='blue', font=font2)
draw.text((150, 150), "Text Layer 3", fill='green', font=font3)

# Save the image with multiple text layers
image.save('./tmp/multi_text_layers.jpg')