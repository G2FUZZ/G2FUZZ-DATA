import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")

# Apply gamma correction
gamma = 2.2
# Directly adjust the pixels for gamma correction
pixels = image.load()  # Load pixel data
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (int((r / 255.0) ** gamma * 255),
                        int((g / 255.0) ** gamma * 255),
                        int((b / 255.0) ** gamma * 255))

# Save the image with gamma correction
file_path = './tmp/gamma_corrected_image.png'
image.save(file_path, 'PNG')

print(f"Gamma corrected image saved to {file_path}")