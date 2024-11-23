from PIL import Image

# Create an image
image = Image.new('RGB', (100, 100), color='blue')

# Save the image with custom settings
image.save('./tmp/image_custom.jpg',
           quality=95,
           huffman_tables='custom',
           dct_mode='progressive'
           )