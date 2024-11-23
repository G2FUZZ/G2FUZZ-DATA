from PIL import Image, ImageDraw

# Create a simple image
img = Image.new('RGB', (800, 600), color=(73, 109, 137))

# Optionally, draw some elements on it
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255, 255, 0))

# Create a thumbnail
thumbnail_size = (128, 128)
thumbnail = img.copy()
thumbnail.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image as metadata (EXIF, XMP, etc. isn't directly supported for this by Pillow)
# This just demonstrates the thumbnail creation and assignment, but saving it directly within the JPEG in a way
# that image viewers recognize as the official thumbnail might not be straightforward without external libraries.
# For demonstration, we'll save the thumbnail separately, because embedding it in a recognized format is beyond Pillow's scope.

# Ensure the target directory exists
import os
target_directory = "./tmp/"
os.makedirs(target_directory, exist_ok=True)

# Save the original image
img_save_path = os.path.join(target_directory, "image_with_thumbnail.jpg")
img.save(img_save_path)

# Save the thumbnail next to it (for demonstration)
thumbnail_save_path = os.path.join(target_directory, "thumbnail.jpg")
thumbnail.save(thumbnail_save_path)

print(f"Image saved to {img_save_path}")
print(f"Thumbnail saved to {thumbnail_save_path}")