from PIL import Image
import os
import datetime
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image - for example, 100x100 pixels, blue
image = Image.new("RGB", (100, 100), "blue")

# Save the image temporarily without metadata
temp_image_path = './tmp/temp_image.jpg'  # Changed to .jpg
image.save(temp_image_path)

# Metadata to add
metadata = {
    "0th": {
        piexif.ImageIFD.Artist: u"Copyright Owner",
        piexif.ImageIFD.ImageDescription: u"A blue square with metadata.",
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S"),
        piexif.ExifIFD.UserComment: b"This is a comment within the metadata.",  # Converted to bytes
    }
}

# Convert metadata dictionary to bytes
exif_bytes = piexif.dump(metadata)

# Re-save the image with metadata
final_image_path = './tmp/blue_square_with_metadata.jpg'  # Changed to .jpg
image.save(final_image_path, "JPEG", exif=exif_bytes)  # Changed format to JPEG

# Clean up the temporary image
os.remove(temp_image_path)

print(f"Image saved with metadata at {final_image_path}")