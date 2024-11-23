from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the animation
width, height = 200, 200
frames = 10

# Create frames
images = []
for i in range(frames):
    # Create an image with a different color
    img = Image.new("RGB", (width, height), (i*25 % 255, i*5 % 255, i*15 % 255))
    draw = ImageDraw.Draw(img)
    # Optional: Draw something on your frame
    draw.text((10, 10), f"Frame {i+1}", fill=(255,255,255))
    images.append(img)

# Save the frames as an animated GIF
output_path = os.path.join(output_dir, "animated.gif")
images[0].save(output_path, save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)

print(f"Animated GIF saved to {output_path}")