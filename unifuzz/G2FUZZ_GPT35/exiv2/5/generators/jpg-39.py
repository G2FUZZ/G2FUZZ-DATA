from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')

# Save the image with specified subsampling mode
image.save('./tmp/quality_setting_subsampling.jpg', quality=95, subsampling=0)  # Use no subsampling for higher quality
image.save('./tmp/quality_setting_subsampling_high.jpg', quality=95, subsampling=1)  # Use horizontal subsampling for better compression efficiency
image.save('./tmp/quality_setting_subsampling_low.jpg', quality=95, subsampling=2)  # Use full chroma subsampling for maximum compression efficiency