from PIL import Image
from PIL.TiffTags import TAGS_V2 as TAGS

metadata = {
    TAGS.get("Artist", 315): "John Doe",
    TAGS.get("Copyright", 33432): "2022 John Doe",
    TAGS.get("DateTime", 306): "2022-09-01 12:00:00",
    TAGS.get("PlanarConfiguration", 284): 2  # 2 represents separate color planes
}

image = Image.new('RGB', (100, 100))
image.save('./tmp/metadata_with_planar_config.tiff', tiffinfo=metadata)