from PIL import Image, ImageDraw, ImageFont
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to add text to an image
def add_text(img, text, position=(0,0), font_size=30):
    draw = ImageDraw.Draw(img)
    # Use a default font instead of "arial.ttf"
    font = ImageFont.load_default()
    draw.text(position, text, fill="white", font=font)
    return img

# Create base images in different color spaces
width, height = 800, 600
layer1_rgb = Image.new('RGB', (width, height), color='red')  # RGB layer
layer2_rgb = Image.new('RGB', (width, height), color='blue')  # RGB layer

# Convert layer2 to CMYK color space and rotate
layer2_cmyk = layer2_rgb.convert('CMYK').rotate(45)

# Create a new layer in YCbCr color space and add text
layer3_ycbcr = Image.new('YCbCr', (width, height), 'yellow')
layer3_ycbcr = add_text(layer3_ycbcr, "YCbCr Color Space", position=(200, 280), font_size=50)

# Create an L layer (grayscale) and manipulate it
layer4_l = Image.new('L', (width, height), color='black')
layer4_l = add_text(layer4_l, "Grayscale", position=(300, 250), font_size=40)

# Adding an RGBA layer with semi-transparent rectangles
layer5_rgba = Image.new('RGBA', (width, height), color='white')
draw = ImageDraw.Draw(layer5_rgba)
draw.rectangle([50, 50, width - 50, 150], fill=(255, 0, 0, 125))  # Semi-transparent red rectangle
draw.rectangle([50, 200, width - 50, 300], fill=(0, 255, 0, 125))  # Semi-transparent green rectangle

# Save the images as a multi-page TIFF with various properties
layer1_rgb.save('./tmp/complex_multicolor_spaces_image.tiff', save_all=True, append_images=[layer2_cmyk, layer3_ycbcr, layer4_l, layer5_rgba], compression="tiff_deflate")

print("Complex TIFF file with multiple color spaces and features created at './tmp/complex_multicolor_spaces_image.tiff'")