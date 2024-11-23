from PIL import Image

# Define the chroma subsampling ratio for color subsampling
color_subsampling = '4:2:2'

# Create an image object with a more complex file structure
image = Image.new('CMYK', (200, 200), color='blue')

# Save the image with JPEG format and apply both Chroma subsampling and Color subsampling with a higher quality
image.save('./tmp/complex_image.jpg', format='JPEG', subsampling=color_subsampling, quality=90)

print("JPEG file with a more complex file structure generated and saved successfully.")