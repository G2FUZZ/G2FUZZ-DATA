from PIL import Image

# Create a new RGB image
image = Image.new('RGB', (100, 100))

# Add Chroma Subsampling feature (4:2:0) to reduce file size
image.save('./tmp/rgb_image_subsampling.jpg', subsampling=0)

print("RGB image with Chroma Subsampling saved successfully.")