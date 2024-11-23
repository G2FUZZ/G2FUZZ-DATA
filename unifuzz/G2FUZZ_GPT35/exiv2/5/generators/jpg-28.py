from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')
image.save('./tmp/extended_jpg_file.jpg', quality=85, subsampling='4:2:0', dpi=(300, 300), icc_profile=b'sample_icc_profile_data', exif=b'sample_exif_data', quality_mode='keep', progressive=True, color_depth=8)  # Color depth: 8-bit per channel