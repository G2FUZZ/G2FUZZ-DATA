from PIL import Image

# Create a new image with RGBA color (Red, Green, Blue, Alpha)
image = Image.new('RGBA', (200, 200), (255, 0, 0, 128))  # Red with 50% transparency

# Save the image with compression level set to 9 (maximum compression)
image.save("./tmp/complex_file.png", compress_level=9)