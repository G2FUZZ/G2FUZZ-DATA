from PIL import Image
import piexif
from datetime import datetime
import os
import subprocess  # To use external tools for lossless JPEG conversion

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color='blue')

# Prepare Exif data (using piexif)
exif_ifd = {
    piexif.ExifIFD.CameraOwnerName: u"John Doe",
    piexif.ExifIFD.DateTimeOriginal: datetime.now().strftime('%Y:%m:%d %H:%M:%S'),
    piexif.ExifIFD.LensMake: u"Sample Lens",
}

exif_dict = {"Exif": exif_ifd}
exif_bytes = piexif.dump(exif_dict)

# Save the image temporarily without Exif to convert it to lossless JPEG later
temp_image_path = './tmp/temp_image.jpg'
img.save(temp_image_path)

# Instead of saving the image directly with Exif data, we first need to convert 
# the image to a Lossless JPEG format. This feature is not directly supported 
# by PIL or piexif, so we would typically need to use external tools like ImageMagick 
# or a similar tool that supports Lossless JPEG. However, Python itself does not 
# support creating Lossless JPEGs directly through PIL or other common libraries.

# The code snippet below is a placeholder for where you would call such an external tool.
# For example, using ImageMagick's 'convert' tool might look like this:
# subprocess.run(['convert', temp_image_path, '-compress', 'Lossless', './tmp/sample_image_with_exif.jpg'])

# Since we can't perform the actual conversion in this example, we'll mimic the process
# by saving the image with Exif data as we would normally.
final_image_path = './tmp/sample_image_with_exif.jpg'
img.save(final_image_path, exif=exif_bytes)

print("Image (intended to be Lossless JPEG) with Exif data saved.")

# Note: This code snippet assumes the use of an external tool for the conversion to Lossless JPEG.
# You will need to replace the placeholder subprocess call with an actual call to a tool that supports this.