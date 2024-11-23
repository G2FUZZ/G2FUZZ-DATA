from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), 'white')

# Save the image with quality setting
quality_levels = [10, 50, 80, 100]
for level in quality_levels:
    file_path = f'./tmp/quality_{level}.jpg'
    white_image.save(file_path, quality=level)

print('Images with different quality levels saved successfully.')