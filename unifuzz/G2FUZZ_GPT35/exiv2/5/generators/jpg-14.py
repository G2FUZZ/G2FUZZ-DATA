from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')

# Save the image with embedded color profiles
image.save('./tmp/quality_setting_color_profiles.jpg', quality=100, icc_profile=b'ICC_PROFILE_DATA_HERE')