from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create an RGB image with Exif Data
rgb_image_with_exif = Image.new('RGB', (100, 100), color='red')
exif_data = {
    270: "Sample image description",
    271: "Photographer Name",
    272: "Camera Model",
    # Add more Exif data as needed
}
rgb_image_with_exif.save('./tmp/rgb_image_with_exif.tif', tiffinfo={34735: b'TIFF Geospatial Metadata', 34665: exif_data})