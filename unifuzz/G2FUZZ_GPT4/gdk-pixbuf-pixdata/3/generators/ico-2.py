import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size and color depth for the icons
sizes_and_modes = [
    (16, '1'),  # Monochrome
    (32, 'P'),  # 256 Colors
    (48, 'RGBA')  # 24-bit True Color with Alpha Channel
]

# Function to create an icon with specified size and color depth
def create_icon(size, mode):
    # Create a new image with the specified size and color depth
    image = Image.new(mode, (size, size))
    
    # Create a draw object to draw shapes or text on the image
    draw = ImageDraw.Draw(image)
    
    # Depending on the mode, draw different shapes or patterns
    if mode == '1':
        # For monochrome, draw a simple black and white pattern
        draw.rectangle([0, 0, size // 2, size // 2], fill=1)
    elif mode == 'P':
        # For 256 colors, use a gradient
        for i in range(size):
            gray = int(255 * (i / size))
            draw.line([(i, 0), (i, size)], fill=gray)
    elif mode == 'RGBA':
        # For true color with alpha, draw a semi-transparent circle
        for i in range(size):
            for j in range(size):
                distance = ((i - size / 2) ** 2 + (j - size / 2) ** 2) ** 0.5
                if distance < size / 3:
                    draw.point((i, j), fill=(255, 0, 0, 127))
                else:
                    draw.point((i, j), fill=(0, 255, 0, 127))
    
    # Return the created image
    return image

# Iterate over each size and mode, create an icon, and save it
for size, mode in sizes_and_modes:
    icon = create_icon(size, mode)
    filename = f'./tmp/icon_{size}x{size}_{mode}.ico'
    icon.save(filename, format='ICO', sizes=[(size, size)])

print('Icons have been generated and saved into ./tmp/')