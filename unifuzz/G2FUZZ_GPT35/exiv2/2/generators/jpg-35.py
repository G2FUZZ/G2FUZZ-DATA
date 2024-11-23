from PIL import Image

# Create a new image with RGB color mode and size 200x200
img = Image.new('RGB', (200, 200))

# Add JFIF format feature to the image
img.info["jfif"] = 1

# Add custom APP markers for application-specific information
app_marker_data_1 = b'My Custom APP Marker Data 1'
app_marker_1 = b'\xff\xe1' + (len(app_marker_data_1) + 2).to_bytes(2, 'big') + app_marker_data_1
img.info["APP1"] = app_marker_1

app_marker_data_2 = b'My Custom APP Marker Data 2'
app_marker_2 = b'\xff\xe2' + (len(app_marker_data_2) + 2).to_bytes(2, 'big') + app_marker_data_2
img.info["APP2"] = app_marker_2

# Add EXIF data for image metadata
exif_data = {
    270: 'My Image Description',
    274: 1,  # Orientation
    282: (300, 1),  # XResolution
    283: (300, 1),  # YResolution
    296: 2  # ResolutionUnit
}
img.info["exif"] = exif_data

# Add Color management feature
color_management_data = b'Color management information'
color_management_marker = b'\xff\xed' + (len(color_management_data) + 2).to_bytes(2, 'big') + color_management_data
img.info["Color management"] = color_management_marker

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/complex_jpg_file_with_APP_and_EXIF_and_color_management.jpg', quality=95)