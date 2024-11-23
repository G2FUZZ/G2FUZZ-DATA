from PIL import Image

# Create a new RGB image
img = Image.new('RGB', (100, 100))

# Save the image in progressive mode
img.save('./tmp/progressive_rendering.png', 'PNG', optimize=True, progressive=True)