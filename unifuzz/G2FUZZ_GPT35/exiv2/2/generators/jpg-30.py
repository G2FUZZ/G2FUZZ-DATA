from PIL import Image

# Define the chroma subsampling ratio for color subsampling
color_subsampling = '4:2:2'

# Create an image object
image = Image.new('RGB', (100, 100), color='red')

# Save the image with JPEG format and apply both Chroma subsampling and Color subsampling
image.save('./tmp/compressed_image_color_subsampling.jpg', subsampling=color_subsampling)

print("JPEG file with Chroma subsampling and Color subsampling generated and saved successfully.")