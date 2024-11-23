from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create an RGBA image with custom metadata
rgba_image = Image.new('RGBA', (200, 200), color='green')
metadata = {
    34735: b'TIFF Geospatial Metadata',
    33550: 1,  # ModelPixelScaleTag
    33922: (0.5, 0.5, 0.0),  # ModelTiepointTag
    33437: (1, 1, 1),  # GeotiffModelPixelScaleTag
    33438: (0, 0, 0),  # GeotiffModelTiepointTag
}
rgba_image.save('./tmp/rgba_image.tif', tiffinfo=metadata)