from PIL import Image

# Create an image with a white background
image_data = Image.new('RGB', (64, 64), color='white')

# Save the image in different sizes and color depths
sizes = [(16, 16), (32, 32), (64, 64)]
color_depths = [8, 24, 32]

for size in sizes:
    for color_depth in color_depths:
        img = image_data.resize(size)
        img.save(f'./tmp/image_size_{size[0]}x{size[1]}_depth_{color_depth}.ico')