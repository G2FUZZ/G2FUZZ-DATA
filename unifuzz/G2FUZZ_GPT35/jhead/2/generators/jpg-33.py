from PIL import Image, ImageDraw, ImageFont

# Create a blank image in RGB mode with size 200x200
baseline_image = Image.new('RGB', (200, 200))

# Add text to the baseline image
draw = ImageDraw.Draw(baseline_image)
font = ImageFont.load_default()  # Use the default system font
draw.text((50, 50), "Baseline Image", fill="black", font=font)

# Save the baseline image with text
baseline_image.save('./tmp/baseline_text.jpg')

# Create a blank image in RGB mode with size 200x200
progressive_image = Image.new('RGB', (200, 200))

# Add text to the progressive image
draw = ImageDraw.Draw(progressive_image)
progressive_font = ImageFont.load_default()  # Use the default system font
draw.text((50, 50), "Progressive Image", fill="black", font=progressive_font)

# Save the progressive image with text in progressive format
progressive_image.save('./tmp/progressive_text.jpg', format='JPEG', progressive=True)