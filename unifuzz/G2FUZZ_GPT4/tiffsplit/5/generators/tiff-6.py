from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image (gradient)
width, height = 256, 256
gradient = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))

# Convert the numpy array to PIL Image
image = Image.fromarray(gradient)

# Configure tiff tags for tile-based storage
# Define the tile dimensions (e.g., 128x128 pixels)
tile_width, tile_height = 128, 128
tiff_tags = {
    256: width,                # ImageWidth
    257: height,               # ImageLength
    258: (8,),                 # BitsPerSample
    259: 1,                    # Compression (none)
    262: 1,                    # PhotometricInterpretation (black is zero)
    273: (8,),                 # StripOffsets, dummy value, Pillow will overwrite
    277: 1,                    # SamplesPerPixel
    278: tile_height,          # RowsPerStrip
    279: (tile_width*tile_height,),  # StripByteCounts, dummy value, Pillow will overwrite
    282: (1, 1),               # XResolution (1 pixel per resolution unit)
    283: (1, 1),               # YResolution (1 pixel per resolution unit)
    284: 1,                    # PlanarConfiguration (chunky format)
    322: tile_width,           # TileWidth
    323: tile_height,          # TileLength
    339: 1,                    # SampleFormat (unsigned integer data)
}

# Save the image as TIFF with tile-based storage
image.save('./tmp/tiled_image.tiff', format='TIFF', tiffinfo=tiff_tags, compression="tiff_deflate", tile=(tile_width, tile_height))