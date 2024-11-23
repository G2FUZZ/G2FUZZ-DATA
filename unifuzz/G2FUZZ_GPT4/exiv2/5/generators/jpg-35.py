from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
img = Image.new('RGB', (400, 400), color='white')

# Initialize drawing context
d = ImageDraw.Draw(img)

# Draw a red rectangle
d.rectangle([50, 50, 150, 150], fill="red", outline="black")

# Draw a blue ellipse
d.ellipse([200, 50, 300, 150], fill="blue", outline="black")

# Draw a green circle
d.ellipse([75, 200, 125, 250], fill="green", outline="black")

# Draw lines of different colors
d.line([150, 200, 300, 200], fill="purple", width=5)
d.line([150, 250, 300, 250], fill="orange", width=3)

# Draw text
try:
    # Attempt to use a truetype font
    font = ImageFont.truetype("arial.ttf", size=20)
except IOError:
    # Fallback to default font if the preferred font is not available
    font = ImageFont.load_default()

d.text((50, 300), "Hello, PIL!", fill="darkblue", font=font)
d.text((50, 330), "More complex structures", fill="darkgreen", font=font)

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as a progressive JPEG
img.save('./tmp/complex_example.jpg', 'JPEG', quality=90, progressive=True)