from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new PNG image
img_size = (256, 256)
image = Image.new('RGBA', img_size, color=(255, 0, 0, 0))

# Optionally, draw something on the image
draw = ImageDraw.Draw(image)
draw.ellipse((img_size[0]//4, img_size[1]//4, 3*img_size[0]//4, 3*img_size[1]//4), fill=(0, 255, 0, 127), outline=(0, 0, 0))

# Save the image as ICO containing the PNG
ico_path = os.path.join(output_dir, 'sample_ico.ico')
image.save(ico_path, format='ICO', sizes=[(256, 256)])

print(f"ICO file saved at: {ico_path}")