from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')

# Save the image with embedded color profiles and lossless feature (JPEG 2000)
image.save('./tmp/quality_setting_color_profiles_lossless.jpg', quality=100, icc_profile=b'ICC_PROFILE_DATA_HERE', format='JPEG2000', quality_mode='dB')