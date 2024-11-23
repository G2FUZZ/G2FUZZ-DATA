from PIL import Image
from PIL.TiffTags import TAGS_V2 as TAGS

metadata = {
    TAGS.get("Artist", 315): "John Doe",
    TAGS.get("Copyright", 33432): "2022 John Doe",
    TAGS.get("DateTime", 306): "2022-09-01 12:00:00",
    TAGS.get("ICCProfile", 34675): b'Your_ICC_Profile_Data_Here',
    TAGS.get("Orientation", 274): 1  # 1 represents the default orientation (0th row is at the top, and 0th column is on the left)
}

image = Image.new('RGB', (100, 100))
image.save('./tmp/metadata_example_with_ICC_and_Orientation.tiff', tiffinfo=metadata)