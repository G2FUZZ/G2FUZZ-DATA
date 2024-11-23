import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to create a PNM file demonstrating the lack of metadata support
def create_pnm_lack_of_metadata():
    # Create a simple image
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), "No Metadata", fill=(255, 0, 0))

    # Save the image as PNM
    img.save('./tmp/lack_of_metadata.pnm')

# Execute the function
create_pnm_lack_of_metadata()