from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 256, 256
image = Image.new("RGB", (width, height))

# Generate a gradient
for x in range(width):
    for y in range(height):
        # Gradient from black to white
        gray = int((x / width) * 255)
        image.putpixel((x, y), (gray, gray, gray))

# Apply gamma correction
# Gamma value < 1 will brighten the image, > 1 will darken it
gamma = 2.2
gamma_correction = [int((i / 255.0) ** (1.0 / gamma) * 255) for i in range(256)]
image = image.point(gamma_correction * 3)

# Save the image with gamma information
output_path = './tmp/gamma_corrected_image.png'
image.save(output_path, "PNG", gamma=1.0/gamma)

print(f"Image with gamma correction saved to {output_path}")