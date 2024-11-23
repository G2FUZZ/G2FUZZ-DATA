from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from PIL.ExifTags import TAGS

# Create a new image with RGB color mode and size 200x200
img = Image.new('RGB', (200, 200))

# Add JFIF format feature to the image
img.info["jfif"] = 1

# Add custom APP markers for application-specific information
app_marker_data1 = b'My Custom APP Marker 1 Data'
app_marker1 = b'\xff\xe1' + (len(app_marker_data1) + 2).to_bytes(2, 'big') + app_marker_data1
img.info["APP1"] = app_marker1

app_marker_data2 = b'My Custom APP Marker 2 Data'
app_marker2 = b'\xff\xe2' + (len(app_marker_data2) + 2).to_bytes(2, 'big') + app_marker_data2
img.info["APP2"] = app_marker2

# Add EXIF data to the image
exif_data = {
    TAGS.get(key, "Unknown Tag"): "Example Value" for key in range(270, 281) if TAGS.get(key)
}
img.info["exif"] = exif_data

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/complex_file_structure_example.jpg', quality=95)