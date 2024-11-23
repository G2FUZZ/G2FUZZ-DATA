from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with a white background
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple red rectangle
draw.rectangle([50, 50, 150, 150], fill="red")

# Save the image with JPEG compression and Restart Markers to ./tmp/
image_path = './tmp/test_image_with_restart_markers.jpg'

# Specify the restart interval (for example, after every 10 MCU rows)
restart_interval = 10  # This value could be adjusted based on your needs or testing

# Save the image with additional option for restart markers
image.save(image_path, 'JPEG', quality=95, restart_interval=restart_interval)

print(f"Image saved to {image_path} with Restart Markers")