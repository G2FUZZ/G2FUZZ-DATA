from PIL import Image

# Create a new GIF image
gif_image = Image.new('RGB', (100, 100), color = 'red')

# Save the GIF image to a file
gif_image.save('./tmp/test.gif')

print("GIF file created successfully.")