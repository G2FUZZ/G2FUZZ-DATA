from PIL import Image, ImageCms

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple gradient image
width, height = 800, 600
image = Image.new("RGB", (width, height))

# Generate gradient
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (int(255 * (x / width)), int(255 * (y / height)), 112))

# Embed an sRGB profile to ensure color consistency across different displays
srgb_profile = ImageCms.createProfile("sRGB")
ImageCms.profileToProfile(image, srgb_profile, srgb_profile, outputMode='RGB').save('./tmp/gradient_with_srgb.png')

print("PNG file with sRGB profile has been saved to ./tmp/gradient_with_srgb.png")