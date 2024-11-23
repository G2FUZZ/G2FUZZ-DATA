from PIL import Image, ExifTags
import piexif
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using PIL
img = Image.new('RGB', (100, 100), color = 'blue')

# Save the image temporarily to insert EXIF data
temp_img_path = './tmp/temp_image.jpg'
img.save(temp_img_path)

# Define EXIF data to add
exif_ifd = {
    piexif.ExifIFD.DateTimeOriginal: u"2023:09:24 10:10:10",
    piexif.ExifIFD.LensMake: u"Sample Lens",
    piexif.ExifIFD.Sharpness: 65535,
    piexif.ExifIFD.LensSpecification: ((24, 1), (70, 1), (35, 1), (35, 1)),
}

exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {}, "thumbnail": None, "GPS": {}}
exif_bytes = piexif.dump(exif_dict)

# Insert EXIF data into the image
piexif.insert(exif_bytes, temp_img_path)

# Move the updated image to the final path (overwriting the temp file)
final_img_path = './tmp/final_image_with_exif.jpg'
os.rename(temp_img_path, final_img_path)

print(f'Image with EXIF data saved to {final_img_path}')