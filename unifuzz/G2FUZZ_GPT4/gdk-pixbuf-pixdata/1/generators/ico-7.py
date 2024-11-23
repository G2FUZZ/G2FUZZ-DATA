from PIL import Image

# Define the sizes for the icon images
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Create a list to hold the images
images = []

# Generate an image for each size
for size in sizes:
    # Create a new image with RGBA mode (to support different color depths)
    img = Image.new("RGBA", size, (255, 0, 0, 0))

    # You can customize the image content here. For simplicity, we're filling it with a solid color.
    # For a real application, you would draw your icon's graphics here.

    # Add the generated image to the list
    images.append(img)

# Define the output path
output_path = './tmp/icon.ico'

# Save the images as a single ICO file
images[0].save(output_path, format='ICO', sizes=[img.size for img in images])