from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), color='white')

# Draw a red square on the image
draw = ImageDraw.Draw(image)
draw.rectangle([100, 100, 300, 300], fill='red')

# Save the original image
image.save('./tmp/original.jpg')

# Add Quantization tables feature
quantization_table = {
    'luminance': [
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ],
    'chrominance': [
        [17, 18, 24, 47, 99, 99, 99, 99],
        [18, 21, 26, 66, 99, 99, 99, 99],
        [24, 26, 56, 99, 99, 99, 99, 99],
        [47, 66, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99]
    ]
}

# Save the image with quantization tables
image.save('./tmp/quantization.jpg', quality=95)

# Add Embedded thumbnails feature
thumbnail_image = image.copy()
thumbnail_image.thumbnail((100, 100))
thumbnail_image.save('./tmp/thumbnail.jpg')