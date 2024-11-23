from PIL import Image, ImageDraw, ImageFont
import os
import piexif

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create an image with white background
img = Image.new('RGB', (800, 400), color=(255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to write for both features
text1 = "9. Standardization: The JPEG format (from which JPG files come) is standardized by the Joint Photographic Experts Group, ensuring consistent implementation across different platforms and devices."
text2 = "4. Arithmetic Coding Option: While less common due to patent restrictions (which have now expired), arithmetic coding is an alternative to the standard Huffman coding used in JPG compression, offering potentially more efficient compression."

# Set the font and size
# For simplicity, using default font. For custom fonts, load them with ImageFont.truetype
font = ImageFont.load_default()

# Position for the first text
text_x1, text_y1 = 10, 50

# Apply the first text to the image
draw.text((text_x1, text_y1), text1, fill=(0, 0, 0), font=font)

# Position for the second text (adjusted for spacing)
text_x2, text_y2 = 10, 150

# Apply the second text to the image
draw.text((text_x2, text_y2), text2, fill=(0, 0, 0), font=font)

def get_exif_data():
    zeroth_ifd = {piexif.ImageIFD.Make: u"Custom Text Generator",
                  piexif.ImageIFD.Model: u"Python PIL Model",
                  piexif.ImageIFD.Software: u"Pillow with piexif"}
    exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 00:00:00",
                piexif.ExifIFD.LensMake: u"Custom Lens",
                piexif.ExifIFD.Sharpness: 65535,
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1))}
    gps_ifd = {piexif.GPSIFD.GPSLatitudeRef: u"N",
               piexif.GPSIFD.GPSLatitude: ((30, 1), (15, 1), (0, 1)),
               piexif.GPSIFD.GPSLongitudeRef: u"E",
               piexif.GPSIFD.GPSLongitude: ((115, 1), (30, 1), (0, 1))}
    first_ifd = {piexif.ImageIFD.Make: u"Custom Text Generator",  # It's okay to duplicate data across IFDs
                 piexif.ImageIFD.Model: u"Python PIL Model"}

    # Assemble the EXIF data
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    return exif_bytes

# Generate EXIF data
exif_data = get_exif_data()

# Save the image with EXIF data
img_path = './tmp/jpeg_features_with_exif.jpg'
img.save(img_path, exif=exif_data)

print(f'Image with detailed EXIF data saved to {img_path}')