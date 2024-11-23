from PIL import Image, ImageDraw
import os

# Function to create a simple image with a specified color
def create_image_with_color(color, size=(100, 100), text_color="white"):
    # Convert the color to YCbCr for subsampling
    image = Image.new("RGB", size, color).convert("YCbCr")
    draw = ImageDraw.Draw(image)
    # Adding some text to differentiate between the layers
    draw.text((10, 40), f"Layer {color}", fill=text_color)
    return image

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
images = [create_image_with_color(color) for color in colors]

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the first image to initiate the multi-page TIFF with subsampling
# Note: TIFF format does not directly support chroma subsampling upon saving in PIL.
#       This example keeps the images in YCbCr color space, which is suitable for subsampling,
#       but the actual subsampling would need to be done before this step if required.
images[0].save('./tmp/multi_page_with_subsampling_support.tiff', compression="tiff_adobe_deflate")

# Now, append the rest of the images
for img in images[1:]:
    img.save('./tmp/multi_page_with_subsampling_support.tiff', save_all=True, append_images=[img], compression="tiff_adobe_deflate")

print("Multi-page TIFF with Subsampling Support has been saved in ./tmp/multi_page_with_subsampling_support.tiff")