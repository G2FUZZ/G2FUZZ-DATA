from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and colors for the gradient
width, height = 800, 600
start_color = (255, 105, 180)  # Pink
end_color = (135, 206, 235)  # Sky blue

# Create a new RGB image
image = Image.new("RGB", (width, height))

# Initialize the draw object
draw = ImageDraw.Draw(image)

# Generate a vertical gradient
for i in range(height):
    # Calculate the blend factor between start and end colors
    ratio = i / float(height - 1)
    # Calculate the intermediate color
    intermediate_color = tuple([
        int(start_color[j] * (1 - ratio) + end_color[j] * ratio)
        for j in range(3)
    ])
    # Draw a line with the intermediate color
    draw.line([(0, i), (width, i)], fill=intermediate_color)

# Save the image with lossy compression
file_path = './tmp/gradient_image.jpg'
image.save(file_path, 'JPEG', quality=85)  # Adjusting the quality parameter affects the compression

print(f"Image saved at {file_path}")