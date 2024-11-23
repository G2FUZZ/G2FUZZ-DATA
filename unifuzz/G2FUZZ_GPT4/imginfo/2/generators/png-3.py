from PIL import Image, ImageDraw

# Ensure the tmp directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# 1-bit black and white image
img_1bit = Image.new('1', (100, 100), color=1)  # 1 for white background, 0 for black
draw = ImageDraw.Draw(img_1bit)
draw.line((0, 0) + img_1bit.size, fill=0)  # Draw a black diagonal line
draw.line((0, img_1bit.size[1], img_1bit.size[0], 0), fill=0)  # Another diagonal line
img_1bit.save('./tmp/1bit_black_white.png')

# 8-bit per channel image (24-bit color depth)
img_8bit = Image.new('RGB', (100, 100), color='skyblue')  # Skyblue background
draw = ImageDraw.Draw(img_8bit)
draw.rectangle([25, 25, 75, 75], fill='yellow', outline='red')  # Yellow square with red outline
img_8bit.save('./tmp/8bit_color.png')

# 16-bit per channel image (48-bit color depth)
# PIL/Pillow might save 16-bit images in a way that not all viewers can render correctly
img_16bit = Image.new('I;16', (100, 100), color='white')  # 'I;16' for 16-bit grayscale, white background
draw = ImageDraw.Draw(img_16bit)
# Drawing a gradient rectangle for demonstration, though it's grayscale
for i in range(100):
    draw.line([(i, 0), (i, 99)], fill=i*655)  # Drawing lines with increasing darkness
img_16bit.save('./tmp/16bit_grayscale.png')