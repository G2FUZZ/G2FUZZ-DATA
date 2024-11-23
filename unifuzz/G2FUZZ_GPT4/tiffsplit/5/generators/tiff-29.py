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

# Function to create a thumbnail version of the provided image
def create_thumbnail(image, size=(50, 50)):
    thumbnail = image.copy()
    thumbnail.thumbnail(size)
    return thumbnail

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
images = [create_image_with_color(color) for color in colors]
thumbnails = [create_thumbnail(image) for image in images]  # Creating thumbnails for each image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the first image to initiate the multi-page TIFF with subsampling
images[0].save('./tmp/multi_page_with_subsampling_and_subfiles.tiff', compression="tiff_adobe_deflate")

# Now, append the rest of the images along with their thumbnails as subfiles
for img, thumb in zip(images[1:], thumbnails[1:]):
    img.save('./tmp/multi_page_with_subsampling_and_subfiles.tiff', save_all=True, append_images=[img, thumb], compression="tiff_adobe_defflate")

print("Multi-page TIFF with Subsampling and Multiple Subfiles has been saved in ./tmp/multi_page_with_subsampling_and_subfiles.tiff")