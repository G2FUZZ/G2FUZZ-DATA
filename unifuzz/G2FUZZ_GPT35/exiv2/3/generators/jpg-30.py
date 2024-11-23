import numpy as np
from PIL import Image, ExifTags

# Define resolution parameters
resolutions = [(1920, 1080), (1280, 720), (800, 600)]

# Create and save jpg files with different resolutions and lossless transformations
for idx, resolution in enumerate(resolutions):
    img = np.random.randint(0, 256, (resolution[1], resolution[0], 3), dtype=np.uint8)
    img = Image.fromarray(img)
    
    # Lossless transformation: Rotate image
    rotated_img = img.transpose(Image.ROTATE_90)
    
    # Lossless transformation: Flip image
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Lossless transformation: Crop image
    width, height = img.size
    crop_img = img.crop((width // 4, height // 4, width * 3 // 4, height * 3 // 4))
    
    # Save images with lossless transformations
    rotated_img.save(f"./tmp/rotated_image_{idx}.jpg")
    flipped_img.save(f"./tmp/flipped_image_{idx}.jpg")
    crop_img.save(f"./tmp/cropped_image_{idx}.jpg")