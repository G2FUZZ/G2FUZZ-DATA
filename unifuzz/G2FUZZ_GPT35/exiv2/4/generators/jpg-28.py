from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100))

# Progressive encoding with DRI marker
exif_dict = {"progressive": True, "quality": 95, "optimize": True, "DRI": 100}  # Set DRI value as needed

# Convert the exif_dict to bytes
exif_bytes = bytes(str(exif_dict), 'utf-8')

# Save the image with exif data
img.save('./tmp/progressive_encoded_with_DRI.jpg', 'JPEG', exif=exif_bytes)