from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create multiple images to store in a single TIFF file
images = []

# Define image size and background colors
image_size = (100, 100)
background_colors = ['red', 'green', 'blue']

# Generate images with different background colors
for color in background_colors:
    img = Image.new('RGB', image_size, color=color)
    # Optionally, add some text or draw on the image
    d = ImageDraw.Draw(img)
    d.text((10, 10), color, fill='white')
    images.append(img)

# Save the images as a multi-page TIFF
images[0].save('./tmp/multi_page.tiff', save_all=True, append_images=images[1:])

print("TIFF file with multiple images has been saved to ./tmp/multi_page.tiff")