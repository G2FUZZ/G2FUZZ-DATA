from PIL import Image, ImageDraw
import piexif
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using Pillow with added text
img = Image.new('RGB', (800, 600), color='lightblue')
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello, World!", fill=(255, 0, 0))

# Save the image temporarily without EXIF
temp_path = './tmp/temp_image.jpg'
img.save(temp_path)

# Define complex EXIF data
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: "Canon",  # Camera make
        piexif.ImageIFD.Model: "Canon EOS 80D",  # Camera model
        piexif.ImageIFD.XResolution: (300, 1),
        piexif.ImageIFD.YResolution: (300, 1),
        piexif.ImageIFD.Software: "Piexif",
        piexif.ImageIFD.DateTime: '2023:01:01 00:00:00'
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: '2023:01:01 00:00:00',
        piexif.ExifIFD.LensMake: "Canon",
        piexif.ExifIFD.ShutterSpeedValue: (491486, 65536),  # 1/30s
        piexif.ExifIFD.ApertureValue: (327680, 65536),  # f/5.0
        piexif.ExifIFD.ISOSpeedRatings: 400,
        piexif.ExifIFD.ExposureBiasValue: (0, 1),  # 0 EV
        piexif.ExifIFD.FocalLength: (50, 1),  # 50mm
    },
    "GPS": {
        piexif.GPSIFD.GPSLatitudeRef: 'N',
        piexif.GPSIFD.GPSLatitude: ((34, 1), (0, 1), (0, 1)),
        piexif.GPSIFD.GPSLongitudeRef: 'W',
        piexif.GPSIFD.GPSLongitude: ((118, 1), (0, 1), (0, 1)),
        piexif.GPSIFD.GPSAltitudeRef: 0,
        piexif.GPSIFD.GPSAltitude: (100, 1)  # 100m above sea level
    },
    "1st": {},
    "thumbnail": None,  # Will be filled with the thumbnail bytes
    "Interop": {},
}

# Generate a thumbnail
thumbnail = img.copy()
thumbnail.thumbnail((128, 128), Image.Resampling.LANCZOS)  # Ensure this line is correct
exif_dict['thumbnail'] = thumbnail.tobytes("jpeg", "RGB")

# Convert the dictionary to bytes
exif_bytes = piexif.dump(exif_dict)

# Now, let's save the image again, this time with EXIF data
final_path = './tmp/final_image_with_complex_exif.jpg'
img.save(final_path, exif=exif_bytes)

# Cleanup the temporary file
os.remove(temp_path)

print(f"Image with complex EXIF data saved to {final_path}")