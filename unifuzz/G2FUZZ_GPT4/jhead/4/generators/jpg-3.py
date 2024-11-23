import os
import piexif
from PIL import Image, ImageDraw

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = (73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10,10), "Hello", fill=(255,255,0))

# Define EXIF data
exif_ifd = {
    piexif.ExifIFD.CameraOwnerName: u"John Doe",
    piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 10:00:00",
    piexif.ExifIFD.LensMake: u"LensCo",
    piexif.ExifIFD.ShutterSpeedValue: (1, 60),
    piexif.ExifIFD.ApertureValue: (8, 1),
}

gps_ifd = {
    piexif.GPSIFD.GPSLatitudeRef: u"N",
    piexif.GPSIFD.GPSLatitude: ((25, 1), (0, 1), (0, 1)),
    piexif.GPSIFD.GPSLongitudeRef: u"E",
    piexif.GPSIFD.GPSLongitude: ((121, 1), (0, 1), (0, 1)),
}

first_ifd = {
    piexif.ImageIFD.Make: u"MakeCo",
    piexif.ImageIFD.Model: u"Model123",
}

exif_dict = {"Exif": exif_ifd, "GPS": gps_ifd, "0th": first_ifd}
exif_bytes = piexif.dump(exif_dict)

# Save the image with EXIF data
img.save('./tmp/example_with_exif.jpg', exif=exif_bytes)

print("Image with EXIF data saved to ./tmp/example_with_exif.jpg")