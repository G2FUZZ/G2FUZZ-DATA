from PIL import Image, ImageCms
import os

# Define the path for saving the image
output_path = './tmp/colored_image_with_icc.jpg'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Create a new image with RGB mode
image = Image.new("RGB", (100, 100), "blue")

# Use a built-in sRGB profile for both input and output
input_profile = ImageCms.createProfile("sRGB")
output_profile = ImageCms.createProfile("sRGB")

# Convert the image using the sRGB profile for both input and output to embed it
image_converted = ImageCms.profileToProfile(image, input_profile, output_profile, outputMode='RGB')

# Save the image with the ICC profile embedded
image_converted.save(output_path, 'JPEG', icc_profile=image_converted.info.get('icc_profile'))

print(f"Image saved with ICC profile at {output_path}")