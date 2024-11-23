from PIL import Image

# Create an image
image = Image.new('RGB', (100, 100), color='red')

# Save the image at different quality levels and subsampling formats
quality_levels = [10, 50, 80, 100]
subsampling_formats = ['4:4:4', '4:2:2', '4:2:0']

for quality in quality_levels:
    for subsampling_format in subsampling_formats:
        subsampling_format_code = {
            '4:4:4': 444,
            '4:2:2': 422,
            '4:2:0': 420
        }

        image.save(f'./tmp/image_quality_{quality}_subsampling_{subsampling_format}.jpg', quality=quality, subsampling=subsampling_format_code[subsampling_format])