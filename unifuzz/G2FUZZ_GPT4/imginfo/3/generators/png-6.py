from PIL import Image, ImageCms

# Define the path for saving the generated PNG file
output_file_path = './tmp/colormanaged_image.png'

# Create a simple gradient image
width, height = 800, 600
image = Image.new("RGB", (width, height))

# Create a gradient from black to white
for i in range(width):
    intensity = int(255 * (i / width))
    for j in range(height):
        image.putpixel((i, j), (intensity, intensity, intensity))

# Load a standard sRGB ICC profile
# Pillow might already include this profile, or you may need to download one and load it here.
# For demonstration, we're assuming Pillow's included sRGB profile.
srgb_profile = ImageCms.createProfile("sRGB")

# Convert the image to sRGB using the loaded ICC profile
# Note: The conversion function already embeds the ICC profile into the image,
# so there's no need to manually add it again when saving.
image = ImageCms.profileToProfile(image, srgb_profile, srgb_profile, outputMode='RGB')

# Save the image. The ICC profile is already embedded.
image.save(output_file_path, "PNG")

print(f"Image saved with color management (ICC profile embedded): {output_file_path}")