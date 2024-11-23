from PIL import Image

# Define resolution in pixels
resolutions = [(640, 480), (1920, 1080), (3840, 2160)]

# Create and save jpg files with different resolutions
for i, resolution in enumerate(resolutions):
    img = Image.new('RGB', resolution)
    img.save(f'./tmp/image_{i+1}.jpg', 'JPEG')