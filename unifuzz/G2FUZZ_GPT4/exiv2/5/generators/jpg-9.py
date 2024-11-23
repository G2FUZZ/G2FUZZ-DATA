from PIL import Image, ImageDraw

# Create an image with white background
width, height = 500, 500
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Parameters for the grid
line_color = (0, 0, 0)
line_width = 1
block_size = 50  # This will create a high contrast grid pattern

# Draw vertical lines
for x in range(0, width, block_size):
    draw.line((x, 0, x, height), fill=line_color, width=line_width)

# Draw horizontal lines
for y in range(0, height, block_size):
    draw.line((0, y, width, y), fill=line_color, width=line_width)

# Save the image with visible block encoding artifact
# Adjust the quality to see different levels of block encoding artifacts
output_path = './tmp/high_contrast_grid.jpg'
image.save(output_path, 'JPEG', quality=25)  # Lower quality = more pronounced artifacts