from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists or create it
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create an image with a white background
image = Image.new('RGB', (400, 400), 'white')
draw = ImageDraw.Draw(image)

# Draw a rectangle (parameters are: top left corner and bottom right corner)
draw.rectangle(((50, 50), (350, 100)), fill="lightblue", outline="blue")

# Draw an ellipse (parameters are the bounding box as for the rectangle)
draw.ellipse(((50, 150), (150, 250)), fill="lightgreen", outline="green")

# Draw a polygon (triangle in this case)
draw.polygon([(200, 150), (300, 250), (100, 250)], fill="lightcoral", outline="red")

# Draw lines (a star in this case)
star_points = [ (250, 300), (275, 350), (325, 350), (290, 375),
                (305, 425), (250, 400), (195, 425), (210, 375),
                (175, 350), (225, 350), (250, 300) ]
draw.line(star_points, fill="gold", width=2)

# Load a font and draw text
try:
    # Attempt to load a specific font (adjust path as necessary)
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    # Fallback to the default PIL font if the preferred font is not found
    font = ImageFont.load_default()

draw.text((50, 300), "Hello, World!", fill="black", font=font)

# Optional: Draw more complex shapes or use additional PIL features

# Save the image as a progressive JPEG
image.save('./tmp/complex_image.jpg', 'JPEG', quality=90, progressive=True)