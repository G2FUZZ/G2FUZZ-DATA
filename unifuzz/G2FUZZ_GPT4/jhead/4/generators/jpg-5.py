from PIL import Image, ImageCms

# Create a simple image using PIL
image = Image.new("RGB", (100, 100), "red")

# Load a standard sRGB profile as both the input and output profile
srgb_profile = ImageCms.createProfile("sRGB")

# Convert the image to include the ICC profile
image_with_icc = ImageCms.profileToProfile(image, srgb_profile, srgb_profile)

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image with ICC profile to a file
image_with_icc.save("./tmp/image_with_icc.jpg", "JPEG", icc_profile=image_with_icc.info.get('icc_profile'))

print("Image saved with ICC profile at './tmp/image_with_icc.jpg'")