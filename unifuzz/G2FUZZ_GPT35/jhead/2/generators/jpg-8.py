from PIL import Image

# Create a blank image in RGB mode with size 100x100
baseline_image = Image.new('RGB', (100, 100))

# Save the image in baseline format
baseline_image.save('./tmp/baseline.jpg')

# Create a blank image in RGB mode with size 100x100
progressive_image = Image.new('RGB', (100, 100))

# Save the image in progressive format
progressive_image.save('./tmp/progressive.jpg', format='JPEG', progressive=True)