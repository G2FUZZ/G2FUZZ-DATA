from PIL import Image

# Create a new image with a solid color
image = Image.new('RGB', (100, 100), color='blue')

# Save the image with different quality settings
for quality in range(50, 100, 10):
    file_path = f'./tmp/image_quality_{quality}.jpg'
    image.save(file_path, quality=quality)

print("JPG files with variable quality settings saved successfully.")