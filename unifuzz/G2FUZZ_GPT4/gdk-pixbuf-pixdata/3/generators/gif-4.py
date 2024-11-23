from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a simple image with text
def generate_image(text, size=(200, 100), background_color='white', text_color='black'):
    image = Image.new('RGB', size, color=background_color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 40), text, fill=text_color)
    return image

# Generate a series of images with different texts
images = [generate_image(f"Frame {i+1}") for i in range(5)]

# Save the images as a GIF
gif_path = os.path.join(output_dir, 'lossless_compression_example.gif')
images[0].save(gif_path,
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=200,
               loop=0)

print(f"GIF saved to {gif_path}")