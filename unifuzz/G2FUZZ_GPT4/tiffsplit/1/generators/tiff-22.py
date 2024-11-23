from PIL import Image, TiffImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an RGB image with Deflate Compression and additional IFDs
rgb_image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square
# Prepare additional IFDs
ifd = TiffImagePlugin.ImageFileDirectory_v2()
ifd[256] = 100  # Image width
ifd[257] = 100  # Image height
ifd[258] = (8, 8, 8)  # Bits per sample for RGB
ifd[259] = 8  # Compression, 8 for Deflate
ifd[262] = 2  # Photometric interpretation, 2 means RGB
# Save with additional IFDs
rgb_image.save('./tmp/rgb_image_deflate.tiff', compression="tiff_deflate", tiffinfo=ifd)

# Generate a CMYK image with Deflate Compression and additional IFDs
cmyk_color_space = np.zeros((100, 100, 4), dtype=np.uint8)
cmyk_color_space[:, :, 0] = 255  # High cyan
cmyk_color_space[:, :, 1] = 0    # Low magenta
cmyk_color_space[:, :, 2] = 0    # Low yellow
cmyk_color_space[:, :, 3] = 0    # Low key (black)
cmyk_image = Image.fromarray(cmyk_color_space, 'CMYK')
# Prepare additional IFDs for CMYK
ifd_cmyk = TiffImagePlugin.ImageFileDirectory_v2()
ifd_cmyk[256] = 100  # Image width
ifd_cmyk[257] = 100  # Image height
ifd_cmyk[258] = (8, 8, 8, 8)  # Bits per sample for CMYK
ifd_cmyk[259] = 8  # Compression, 8 for Deflate
ifd_cmyk[262] = 5  # Photometric interpretation, 5 means CMYK
# Save with additional IFDs
cmyk_image.save('./tmp/cmyk_image_deflate.tiff', compression="tiff_deflate", tiffinfo=ifd_cmyk)

# Generate a Grayscale image with Deflate Compression and additional IFDs
gray_image = Image.new("L", (100, 100), 128)  # Medium gray square
# Prepare additional IFDs for Grayscale
ifd_gray = TiffImagePlugin.ImageFileDirectory_v2()
ifd_gray[256] = 100  # Image width
ifd_gray[257] = 100  # Image height
ifd_gray[258] = (8,)  # Bits per sample for grayscale
ifd_gray[259] = 8  # Compression, 8 for Deflate
ifd_gray[262] = 1  # Photometric interpretation, 1 means black is zero
# Save with additional IFDs
gray_image.save('./tmp/gray_image_deflate.tiff', compression="tiff_deflate", tiffinfo=ifd_gray)