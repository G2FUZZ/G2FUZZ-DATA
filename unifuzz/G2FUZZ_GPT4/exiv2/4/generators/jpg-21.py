from PIL import Image
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a blank image
image = Image.new('RGB', (100, 100), color = (73, 109, 137))

# For demonstration, we'll skip directly assigning an ICC profile and just save the image.
# This image will be in sRGB color space because that's the default for new RGB images in Pillow.

# To implement the "Variable Resolution Levels" feature, you can adjust the quality parameter
# when saving the JPEG. The quality parameter allows you to choose a balance between image quality and file size.
# A higher quality level results in better image quality and larger file size, and vice versa.

# Save the image with a high quality level
high_quality_path = './tmp/icc_profiled_image_high_quality.jpg'
image.save(high_quality_path, 'JPEG', quality=95)
print(f"High-quality image saved to {high_quality_path}")

# Save the image with a medium quality level
medium_quality_path = './tmp/icc_profiled_image_medium_quality.jpg'
image.save(medium_quality_path, 'JPEG', quality=50)
print(f"Medium-quality image saved to {medium_quality_path}")

# Save the image with a low quality level
low_quality_path = './tmp/icc_profiled_image_low_quality.jpg'
image.save(low_quality_path, 'JPEG', quality=10)
print(f"Low-quality image saved to {low_quality_path}")

# This demonstrates generating JPEG files with variable resolution levels by adjusting the quality parameter.