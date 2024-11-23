from PIL import Image

# Create a 32-bit CMYK image with multiple layers
image_cmyk = Image.new('CMYK', (200, 200))
pixels = image_cmyk.load()

# Define colors for each layer
colors = [(255, 0, 0, 0),  # Cyan
          (0, 255, 0, 0),  # Magenta
          (0, 0, 255, 0),  # Yellow
          (0, 0, 0, 255)]  # Black

# Assign colors to different quadrants of the image
for i in range(image_cmyk.size[0]):
    for j in range(image_cmyk.size[1]):
        if i < image_cmyk.size[0] // 2 and j < image_cmyk.size[1] // 2:
            pixels[i, j] = colors[0]  # Cyan
        elif i >= image_cmyk.size[0] // 2 and j < image_cmyk.size[1] // 2:
            pixels[i, j] = colors[1]  # Magenta
        elif i < image_cmyk.size[0] // 2 and j >= image_cmyk.size[1] // 2:
            pixels[i, j] = colors[2]  # Yellow
        else:
            pixels[i, j] = colors[3]  # Black

# Convert CMYK image to RGB mode before saving as PNG
image_rgb = image_cmyk.convert('RGB')
image_rgb.save('./tmp/32bit_cmyk.png')