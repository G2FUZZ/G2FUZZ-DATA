from PIL import Image

# Create a new image (100x100 pixels) with RGB color
image = Image.new('RGB', (100, 100), color='white')

# Save the image as an interlaced PNG file
image.save("./tmp/interlaced_image.png", interlace=True)

print("Interlaced PNG file created successfully!")