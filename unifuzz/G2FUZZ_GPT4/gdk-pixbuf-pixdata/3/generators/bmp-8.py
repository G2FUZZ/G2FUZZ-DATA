from PIL import Image, ImageDraw

# Create an image with white background
width, height = 1920, 1080
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Settings for the grid
grid_color = (0, 0, 0)  # Black color for the grid lines
num_lines = 20  # Total number of lines horizontally and vertically

# Draw the grid
for i in range(num_lines + 1):
    # Horizontal lines
    draw.line((0, i * height / num_lines, width, i * height / num_lines), fill=grid_color)
    # Vertical lines
    draw.line((i * width / num_lines, 0, i * width / num_lines, height), fill=grid_color)

# Save the image
output_path = './tmp/scalability.bmp'
image.save(output_path)

print(f"Image saved to {output_path}")