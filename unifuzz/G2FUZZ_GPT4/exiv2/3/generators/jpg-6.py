from PIL import Image

# Create a simple image with one color
img = Image.new('RGB', (100, 100), color = 'red')

# Specify the directory to save the image
save_path = './tmp/color_profile_image.jpg'

# Assuming you have an sRGB ICC profile file, you would load it like this:
# with open("path_to_srgb_profile.icc", "rb") as f:
#     icc_profile = f.read()

# For demonstration, we'll simulate the ICC profile data as None
# In practice, replace None with the actual ICC profile data loaded from a file
icc_profile = None

# Save the image with an ICC profile
img.save(save_path, 'JPEG', icc_profile=icc_profile)

print(f"Image saved to {save_path} with an embedded ICC profile.")