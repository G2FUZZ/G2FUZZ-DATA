from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image with ICC Profiles feature
icc_profile = b'Example ICC Profile Data'  # Example ICC profile data
image.save('./tmp/compressed_image_icc_profiles.tiff', compression='tiff_lzw', icc_profile=icc_profile)

print("TIFF file with ICC Profiles feature has been saved in ./tmp/")