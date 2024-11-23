from PIL import Image, ImageDraw
from PIL.TiffTags import TAGS_V2 as TAGS

metadata = {
    TAGS.get("Artist", 315): "John Doe",
    TAGS.get("Copyright", 33432): "2022 John Doe",
    TAGS.get("DateTime", 306): "2022-09-01 12:00:00"
}

image = Image.new('RGB', (100, 100))
image.putpixel((50, 50), (255, 0, 0))  # Add a red pixel at the center

# Create a second layer with a green circle
layer2 = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(layer2)
draw.ellipse((25, 25, 75, 75), fill=(0, 255, 0))
image = Image.alpha_composite(image.convert('RGBA'), layer2.convert('RGBA'))

# Save the image with multiple layers and compression settings
image.save('./tmp/extended_metadata_example.tiff', tiffinfo=metadata, compression='tiff_adobe_deflate')