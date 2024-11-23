from PIL import Image

# Create a new RGB image
image = Image.new('RGB', (100, 100))

# Add Chroma Subsampling feature (4:2:0) to reduce file size
image.save('./tmp/rgb_image_subsampling.jpg', subsampling=0)

# Add Resolution information (dpi)
resolution = (300, 300)
image.save('./tmp/rgb_image_with_resolution.jpg', dpi=resolution)

# Add Baseline and Progressive Modes feature
image.save('./tmp/rgb_image_baseline_progressive.jpg', quality=95, progressive=True)

print("RGB image with Chroma Subsampling, Resolution, and Baseline/Progressive Modes saved successfully.")