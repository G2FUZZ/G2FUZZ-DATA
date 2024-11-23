from PIL import Image
from PIL.TiffTags import TAGS_V2 as TAGS

metadata = {
    TAGS.get("Artist", 315): "John Doe",
    TAGS.get("Copyright", 33432): "2022 John Doe",
    TAGS.get("DateTime", 306): "2022-09-01 12:00:00"
}

image = Image.new('RGB', (100, 100))
image.save('./tmp/metadata_example.tiff', tiffinfo=metadata)