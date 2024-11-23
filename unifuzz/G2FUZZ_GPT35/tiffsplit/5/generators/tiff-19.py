from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create an RGB image with Exif Data and ICC Profiles
rgb_image_with_exif_icc = Image.new('RGB', (100, 100), color='red')
exif_data = {
    270: "Sample image description",
    271: "Photographer Name",
    272: "Camera Model",
    # Add more Exif data as needed
}
icc_profile_data = b'Example ICC Profile Data'
rgb_image_with_exif_icc.save('./tmp/rgb_image_with_exif_icc.tif', tiffinfo={34735: b'TIFF Geospatial Metadata', 34665: exif_data, 34675: icc_profile_data})