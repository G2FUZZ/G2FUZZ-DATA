from PIL import Image, ImageCms
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image using RGB mode
image = Image.new("RGB", (100, 100), (255, 0, 0))

# Path to the sRGB profile (Adjust this path to the actual location of your sRGB profile)
srgb_profile_path = 'path_to_your_srgb_profile.icc'

# Load the sRGB color profile
try:
    srgb_profile = ImageCms.ImageCmsProfile(srgb_profile_path)
except OSError as e:
    print(f"Error opening sRGB profile: {e}")
    # Optionally, handle the error (e.g., use a default profile, exit the program, etc.)
else:
    # Apply the sRGB color profile to the image
    # Specify Chroma Subsampling using the subsampling='4:2:0' argument in save()
    # 4:2:0 chroma subsampling is common and significantly reduces file size with minimal visual quality loss
    image.save('./tmp/colored_image_with_profile_and_subsampling.jpg', 'JPEG', icc_profile=srgb_profile.tobytes(), subsampling='4:2:0', quality=95)