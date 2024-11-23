from PIL import Image
from PIL.TiffTags import TAGS_V2 as TAGS

metadata = {
    TAGS.get("Artist", 315): "Jane Smith",
    TAGS.get("Copyright", 33432): "2023 Jane Smith",
    TAGS.get("DateTime", 306): "2023-03-15 09:30:00",
    TAGS.get("ICCProfile", 34675): b'Your_ICC_Profile_Data_Here',
    TAGS.get("Orientation", 274): 1,
    TAGS.get("Software", 305): "PIL",  # Adding software information
    TAGS.get("ResolutionUnit", 296): 2,  # Resolution unit in inches
    TAGS.get("XResolution", 282): (300, 1),  # X resolution 300 pixels per inch
    TAGS.get("YResolution", 283): (300, 1),  # Y resolution 300 pixels per inch
    TAGS.get("Compression", 259): 7,  # Compression type LZW
    TAGS.get("Predictor", 317): 2,  # Predictor type for LZW compression
    TAGS.get("TileWidth", 322): 128,  # Tile width for tiled TIFF
    TAGS.get("TileLength", 323): 128,  # Tile length for tiled TIFF
}

# Create a new image with RGBA mode
image = Image.new('RGBA', (200, 200), color=(255, 0, 0, 255))

# Create a second layer with a different color
second_layer = Image.new('RGBA', (200, 200), color=(0, 255, 0, 255))
image.paste(second_layer, (50, 50), mask=second_layer)

# Save the image with complex metadata and multiple layers
image.save('./tmp/metadata_example_complex.tiff', tiffinfo=metadata)