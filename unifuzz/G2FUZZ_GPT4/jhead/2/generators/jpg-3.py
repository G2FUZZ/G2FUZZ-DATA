from PIL import Image
import piexif
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using Pillow
img = Image.new('RGB', (100, 100), color = 'blue')

# Save the image temporarily without EXIF
temp_path = './tmp/temp_image.jpg'
img.save(temp_path)

# Define some EXIF data, for instance, a simple GPS information and a timestamp
exif_dict = {
    "GPS": {
        piexif.GPSIFD.GPSLatitudeRef: 'N',
        piexif.GPSIFD.GPSLatitude: ((34, 1), (0, 1), (0, 1)),
        piexif.GPSIFD.GPSLongitudeRef: 'W',
        piexif.GPSIFD.GPSLongitude: ((118, 1), (0, 1), (0, 1)),
    },
    "0th": {
        piexif.ImageIFD.DateTime: '2023:01:01 00:00:00'  # Corrected from piexib to piexif
    }
}

# Convert the dictionary to bytes
exif_bytes = piexif.dump(exif_dict)

# Now, let's save the image again, this time with EXIF data
final_path = './tmp/final_image_with_exif.jpg'
img.save(final_path, exif=exif_bytes)

# Cleanup the temporary file
os.remove(temp_path)

print(f"Image with EXIF data saved to {final_path}")