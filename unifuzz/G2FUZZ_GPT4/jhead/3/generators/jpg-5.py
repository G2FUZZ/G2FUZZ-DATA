from PIL import Image, ExifTags
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a primary image (a simple red square)
primary_image = Image.new('RGB', (800, 600), color = 'red')

# Create a thumbnail image from the primary image
thumbnail_size = (128, 128)
thumbnail_image = primary_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Save the thumbnail in a temp location to embed later
temp_thumbnail_path = os.path.join(output_dir, "temp_thumbnail.jpg")
thumbnail_image.save(temp_thumbnail_path, "JPEG")

# Embed the thumbnail in the primary image's Exif data
with open(temp_thumbnail_path, "rb") as thumb:
    primary_image.info["thumbnail"] = thumb.read()

# Define the function to embed thumbnail into the Exif data of the main image
def embed_thumbnail(image_path, thumbnail_bytes):
    # Load the image
    with Image.open(image_path) as img:
        # Check if the image has Exif data. If not, create an empty dict
        if not hasattr(img, "_getexif"):
            exif = {}
        else:
            exif = img._getexif() or {}
        
        # Convert the Exif tags to their corresponding IDs
        exif_tags = {ExifTags.TAGS[k]: k for k in ExifTags.TAGS.keys() if k in ExifTags.TAGS}
        
        # Embed the thumbnail
        if "JPEGThumbnail" in exif_tags:
            exif[exif_tags["JPEGThumbnail"]] = thumbnail_bytes
        else:
            print("Unable to find the tag for embedding the thumbnail.")
            return False
        
        # Save the image with the embedded thumbnail
        exif_bytes = img.info.get('exif')
        img.save(image_path, "JPEG", exif=exif_bytes)
        return True

# Save the primary image with a placeholder for the Exif data
primary_image_path = os.path.join(output_dir, "image_with_thumbnail.jpg")
primary_image.save(primary_image_path, "JPEG", exif=b"")

# Embed the thumbnail into the primary image's Exif
success = embed_thumbnail(primary_image_path, primary_image.info['thumbnail'])

# Cleanup the temporary thumbnail file
os.remove(temp_thumbnail_path)

if success:
    print("The thumbnail has been successfully embedded.")
else:
    print("Failed to embed the thumbnail.")