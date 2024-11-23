import numpy as np
from PIL import Image

# Define resolution parameters
resolutions = [(1920, 1080), (1280, 720), (800, 600)]

# Define subsampling factors for chroma channels (YCbCr)
subsampling_factors = [(2, 2), (1, 1), (1, 1)]  # Y: 4:2:0, Y: 4:4:4, Y: 4:4:4

# Create and save jpg files with different resolutions and subsampling
for idx, (resolution, subsampling) in enumerate(zip(resolutions, subsampling_factors)):
    img = np.random.randint(0, 256, (resolution[1], resolution[0], 3), dtype=np.uint8)
    img = Image.fromarray(img)
    
    # Convert the image to YCbCr mode for subsampling
    img_ycbcr = img.convert("YCbCr")
    
    # Apply subsampling to chroma channels
    y, cb, cr = img_ycbcr.split()
    cb = cb.resize((resolution[0] // subsampling[0], resolution[1] // subsampling[1]), Image.BOX)
    cr = cr.resize((resolution[0] // subsampling[0], resolution[1] // subsampling[1]), Image.BOX)
    
    # Resize luma channel to match the dimensions of chroma channels
    y = y.resize((resolution[0] // subsampling[0], resolution[1] // subsampling[1]), Image.BOX)
    
    # Merge the subsampled YCbCr channels
    img_ycbcr = Image.merge("YCbCr", (y, cb, cr))
    
    # Convert back to RGB mode before saving
    img_subsampled = img_ycbcr.convert("RGB")
    
    # Save the image with subsampling
    img_subsampled.save(f"./tmp/image_{idx}_subsampling.jpg")