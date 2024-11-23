from PIL import Image, ImageCms

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image
img = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Path to your ICC profile
icc_profile_path = 'your_icc_profile_path.icc'

try:
    # Load an ICC profile
    with open(icc_profile_path, 'rb') as f:
        icc_profile = f.read()
    
    # Embed the ICC profile into the image
    img.save('./tmp/icc_profiled_image.jpg', 'JPEG', icc_profile=icc_profile)
    print("Image saved with ICC profile.")
except IOError:
    print(f"ICC profile at {icc_profile_path} not found. Saving image without ICC profile.")
    img.save('./tmp/simple_image.jpg', 'JPEG')
    print("Image saved without ICC profile.")