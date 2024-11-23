from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image with ICC Profiles and Color Profiles features
icc_profile = b'Example ICC Profile Data'  # Example ICC profile data
color_profile = b'Example Color Profile Data'  # Example Color profile data
image.save('./tmp/compressed_image_icc_color_profiles.tiff', compression='tiff_lzw', icc_profile=icc_profile, extra_params=[(34675, 'Color Profiles', color_profile)])

print("TIFF file with ICC Profiles and Color Profiles features has been saved in ./tmp/")