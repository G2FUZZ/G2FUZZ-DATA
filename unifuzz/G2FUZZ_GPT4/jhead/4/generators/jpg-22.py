from PIL import Image, ImageCms
import os

# Create a more complex image using gradients
def create_gradient_image(width, height):
    image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = 128  # Constant value for simplification
            image.putpixel((x, y), (r, g, b))
    return image

# Load a standard sRGB profile as both the input and output profile
srgb_profile = ImageCms.createProfile("sRGB")

# Create a gradient image
image = create_gradient_image(200, 200)

# Convert the image to include the ICC profile with higher quality
image_with_icc = ImageCms.profileToProfile(image, srgb_profile, srgb_profile, outputMode='RGB')

# Ensure the './tmp/' directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image with ICC profile, custom DPI, and quality to a file
# Note: Removed the exif argument since we're not adding EXIF data in this simplified fix
image_with_icc.save(
    "./tmp/complex_image_with_icc.jpg",
    "JPEG",
    icc_profile=image_with_icc.info.get('icc_profile'),
    dpi=(300, 300),  # Setting a custom DPI
    quality=95  # Higher quality (default is 75)
)

print("Complex image saved with ICC profile, custom DPI at './tmp/complex_image_with_icc.jpg'")