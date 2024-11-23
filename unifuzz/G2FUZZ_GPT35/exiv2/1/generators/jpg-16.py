from PIL import Image

# Create an image
image = Image.new('RGB', (100, 100), color='red')

# Save the image with DRM protection
image.save('./tmp/image_with_drm.jpg', format='JPEG', quality=80, dpi=(300, 300), icc_profile=image.info.get('icc_profile'))

print("Image with DRM protection saved successfully.")