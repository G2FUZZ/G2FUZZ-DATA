from PIL import Image, ImageDraw, ImageFont
import os
import piexif

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a primary image (a simple blue square)
primary_image = Image.new('RGB', (800, 600), color='blue')

# Create a secondary image (a transparent red square) and place it over the primary image
secondary_image = Image.new('RGBA', (400, 300), color=(255,0,0,128))  # Half-transparent red
primary_image.paste(secondary_image, (200, 150), secondary_image)

# Add text annotation to the image
draw = ImageDraw.Draw(primary_image)
# Use a default font instead of specifying a file
font = ImageFont.load_default()
draw.text((10, 10), "Complex JPEG", fill="white", font=font)

# Save the primary image as a temp file to attach EXIF data later
primary_image_path = os.path.join(output_dir, "image_with_complex_structure.jpg")
primary_image.save(primary_image_path, "JPEG")

# Function to embed EXIF data into the image
def embed_exif_data(image_path, exif_data):
    # Convert the EXIF data to bytes
    exif_bytes = piexif.dump(exif_data)
    # Insert EXIF data into the image
    piexif.insert(exif_bytes, image_path)

# EXIF data to embed (using piexif)
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: u"Example Make",
        piexif.ImageIFD.Model: u"Example Model",
        piexif.ImageIFD.XResolution: (96, 1),
        piexif.ImageIFD.YResolution: (96, 1),
        piexif.ImageIFD.Software: u"Example Software"
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 00:00:00",
        piexif.ExifIFD.LensMake: u"Example Lens Make",
        piexif.ExifIFD.Sharpness: 1,
        piexif.ExifIFD.LensSpecification: ((24, 1), (70, 1), (28, 10), (28, 10)),
    }
}

# Embed the EXIF data into the primary image
embed_exif_data(primary_image_path, exif_dict)

print("The complex image with EXIF data, layers, and text annotation has been successfully generated.")