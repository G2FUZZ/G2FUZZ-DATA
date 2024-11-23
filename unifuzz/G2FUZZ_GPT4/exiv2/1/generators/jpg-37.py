import numpy as np
import cv2
import os
import piexif

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate an image using numpy
# Creating a simple gradient image for demonstration
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for the image - simple visualization
for i in range(height):
    color_value = 255 * (i / height)
    image[i, :, :] = [color_value, color_value, color_value]

def get_exif_data():
    zeroth_ifd = {piexif.ImageIFD.Make: u"Gradient Generator",
                  piexif.ImageIFD.Model: u"Model 1",
                  piexif.ImageIFD.Software: u"OpenCV with Numpy"}
    exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 00:00:00",
                piexif.ExifIFD.LensMake: u"Standard",
                piexif.ExifIFD.Sharpness: 65535,
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1))}
    gps_ifd = {piexif.GPSIFD.GPSLatitudeRef: u"N",
               piexif.GPSIFD.GPSLatitude: ((0, 1), (0, 1), (0, 1)),
               piexif.GPSIFD.GPSLongitudeRef: u"E",
               piexif.GPSIFD.GPSLongitude: ((0, 1), (0, 1), (0, 1))}
    first_ifd = {piexif.ImageIFD.Make: u"Gradient Generator",  # It's okay to duplicate data across IFDs
                 piexif.ImageIFD.Model: u"Model 1"}

    # Assemble the EXIF data
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    return exif_bytes

# Generate EXIF data
exif_data = get_exif_data()

# OpenCV does not directly support adding EXIF data during the save operation.
# Therefore, we need to save the image first, then load and re-save with EXIF data using piexif.
output_path = './tmp/gradient_image_with_exif.jpg'
temp_path = './tmp/temp_image.jpg'  # Temporary image file path
cv2.imwrite(temp_path, image, [int(cv2.IMWRITE_JPEG_PROGRESSIVE), 1, int(cv2.IMWRITE_JPEG_QUALITY), 95])

# Load the image with PIL to insert EXIF data
from PIL import Image
img = Image.open(temp_path)
img.save(output_path, "JPEG", exif=exif_data)

# Cleanup the temporary file
os.remove(temp_path)

print(f"Gradient JPEG image with EXIF data saved at: {output_path}")