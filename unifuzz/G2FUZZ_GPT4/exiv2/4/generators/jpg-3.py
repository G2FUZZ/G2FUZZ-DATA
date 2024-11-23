from PIL import Image, ExifTags
import piexif
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image
img = Image.new('RGB', (100, 100), color = 'red')

# Save the image temporarily to insert EXIF data
temp_file_path = './tmp/temp_image.jpg'
img.save(temp_file_path)

# Define EXIF data
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: "Python",
        piexif.ImageIFD.Model: "PIL",
        piexif.ImageIFD.Software: "Pillow",
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: "2023:01:01 00:00:00",
        piexif.ExifIFD.LensMake: "Python Lens",
        piexif.ExifIFD.ShutterSpeedValue: (500, 100),
        piexif.ExifIFD.ApertureValue: (8, 1),
        piexif.ExifIFD.ISOSpeedRatings: 100,
    },
}

# Convert dict to bytes
exif_bytes = piexif.dump(exif_dict)

# Save image with EXIF data
final_file_path = './tmp/generated_with_exif.jpg'
img.save(final_file_path, exif=exif_bytes)

# Clean up temporary file
os.remove(temp_file_path)

print("JPEG with EXIF created at: " + final_file_path)