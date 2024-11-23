from PIL import Image, ImageDraw
import os

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a new PNG image with transparency
size = (256, 256)  # Common ICO size that supports PNG compression
image = Image.new("RGBA", size, (0, 0, 0, 0))

# Draw a simple shape, for example, a red circle
draw = ImageDraw.Draw(image)
draw.ellipse((56, 56, 200, 200), fill=(255, 0, 0, 255))

# Save the image as a PNG to a temporary file (ICO supports embedded PNG)
temp_png_path = os.path.join(output_dir, "temp_icon.png")
image.save(temp_png_path, format="PNG")

# Use the same PIL Image instance to save as an ICO file, including the PNG image
ico_path = os.path.join(output_dir, "icon.ico")
image.save(ico_path, format="ICO", sizes=[(256, 256)])

# Optionally, remove the temporary PNG file
os.remove(temp_png_path)

print(f"ICO file with PNG compression saved to: {ico_path}")