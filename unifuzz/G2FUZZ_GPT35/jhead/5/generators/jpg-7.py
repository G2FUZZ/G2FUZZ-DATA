from PIL import Image

# Create a new image with a solid color
image = Image.new('RGB', (100, 100), color='blue')

# Save the image with different compression ratios
for quality in range(10, 100, 10):
    image.save(f'./tmp/compressed_image_{quality}.jpg', quality=quality)

print("JPG files with different compression ratios have been saved in the './tmp/' directory.")