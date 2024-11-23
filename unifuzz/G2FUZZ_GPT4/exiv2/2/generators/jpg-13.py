from PIL import Image
import os
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Define EXIF data
# The correct approach is to separate the data into the different IFDs (0th, Exif, GPS, etc.)
# and use the correct tags from piexif.
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: u"Canon",  # Correctly placed under the "0th" IFD
        piexif.ImageIFD.Model: u"Canon EOS 80D",  # Correctly placed under the "0th" IFD
    },
    "Exif": {
        piexif.ExifIFD.LensModel: u"EF-S 18-135mm f/3.5-5.6 IS",
    }
}

# Generate EXIF bytes
exif_bytes = piexif.dump(exif_dict)

# Save the image with EXIF data
temp_path = './tmp/simple_image_no_exif.jpg'
final_path = './tmp/simple_image_with_exif.jpg'
image.save(temp_path, 'JPEG', exif=exif_bytes)

# Since we've already included the EXIF data during the save, there's no need to insert it again with piexif.insert
# Move the file to the final path (with EXIF data)
os.rename(temp_path, final_path)

print("Image was saved with embedding JFIF (by default in JPEG) and custom EXIF metadata.")