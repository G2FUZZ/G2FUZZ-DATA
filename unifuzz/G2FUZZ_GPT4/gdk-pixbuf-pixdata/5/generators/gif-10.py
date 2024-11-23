from PIL import Image, ImageDraw

# Create a directory for storing the output if it doesn't exist
import os
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Since we can't directly specify aspect ratio in the GIF metadata,
# we have to create an image with the desired aspect ratio.
# Let's create an image with a 16:9 aspect ratio as an example.

# Define the dimensions
width = 320
height = int(width * 9 / 16)  # Calculate height to maintain 16:9 aspect ratio

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")

# Draw some simple content - a rectangle and some text
draw = ImageDraw.Draw(image)
draw.rectangle([width // 4, height // 4, 3 * width // 4, 3 * height // 4], outline="black", fill="lightgray")
draw.text((width // 2, height // 2), "16:9 Aspect Ratio", fill="black", anchor="mm")

# Save the image as a GIF
output_path = os.path.join(output_dir, "aspect_ratio_info.gif")
image.save(output_path)

print(f"Image saved to {output_path}")