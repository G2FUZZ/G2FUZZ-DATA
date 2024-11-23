from PIL import Image
import piexif
from datetime import datetime
import os
import subprocess  # To use external tools for lossless JPEG conversion and color space modification

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

# Here, we could use an external tool like ImageMagick to convert the image
# to Lossless JPEG and also to apply the sRGB or Adobe RGB color space.
# The exact commands depend on the tool and the desired outcome.
# Example (not executable in this context):
# subprocess.run(['convert', temp_image_path, '-compress', 'Lossless', '-colorspace', 'sRGB', './tmp/sample_image_with_exif_sRGB.jpg'])
# subprocess.run(['convert', temp_image_path, '-compress', 'Lossless', '-colorspace', 'AdobeRGB', './tmp/sample_image_with_exif_AdobeRGB.jpg'])

# Since the actual conversion and color space manipulation cannot be performed
# in this example due to the limitations of executing external tools here,
# we will proceed to save the image with Exif data as we would normally.
# This step is to mimic the process of saving the image after conversion and applying the color space.
final_image_path = './tmp/sample_image_with_exif.jpg'
img.save(final_image_path, exif=exif_bytes)

print("Image (intended to be Lossless JPEG with sRGB and Adobe RGB support) with Exif data saved.")

# Note: This code snippet is a template for integrating sRGB and Adobe RGB support
# into a workflow using external tools for image conversion and color space manipulation.
# The actual implementation of these features would require executing the external commands
# as commented out above and possibly managing multiple output files for different color spaces.