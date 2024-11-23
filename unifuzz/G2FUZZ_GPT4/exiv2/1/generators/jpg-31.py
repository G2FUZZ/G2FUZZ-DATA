from PIL import Image
import os
import piexif

# Create the 'tmp' directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create a blank image
img = Image.new('RGB', (100, 100), color='red')

# Exif data is a bit more complex and requires a structured dictionary
# Let's prepare some fake GPS data and camera details as an example
# Note: In real applications, ensure the GPS values are correctly formatted and valid.

def get_exif_data():
    zeroth_ifd = {piexif.ImageIFD.Make: u"Fake Camera Make",
                  piexif.ImageIFD.Model: u"Fake Camera Model",
                  piexif.ImageIFD.Software: u"Piexif"}
    exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 00:00:00",
                piexif.ExifIFD.LensMake: u"Fake Lens Make",
                piexif.ExifIFD.Sharpness: 65535,
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1))}
    gps_ifd = {piexif.GPSIFD.GPSLatitudeRef: u"N",
               piexif.GPSIFD.GPSLatitude: ((30, 1), (15, 1), (0, 1)),
               piexif.GPSIFD.GPSLongitudeRef: u"E",
               piexif.GPSIFD.GPSLongitude: ((115, 1), (30, 1), (0, 1))}
    first_ifd = {piexif.ImageIFD.Make: u"Fake Camera Make",  # It's okay to duplicate data across IFDs
                 piexif.ImageIFD.Model: u"Fake Camera Model"}

    # Assemble the EXIF data
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    return exif_bytes

# Generate EXIF data
exif_data = get_exif_data()

# Saving the image with EXIF data
img.save('./tmp/exif_detailed_example.jpg', exif=exif_data)

print("Image with detailed EXIF data saved.")