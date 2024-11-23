from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an RGB image with Deflate Compression and Planar Configuration
rgb_image_planar = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square
rgb_image_planar.save('./tmp/rgb_image_deflate_planar.tiff', compression="tiff_deflate", tiffinfo={317: 2})

# Generate a CMYK image with Deflate Compression and Planar Configuration
cmyk_color_space_planar = np.zeros((100, 100, 4), dtype=np.uint8)
cmyk_color_space_planar[:, :, 0] = 255  # High cyan
cmyk_color_space_planar[:, :, 1] = 0    # Low magenta
cmyk_color_space_planar[:, :, 2] = 0    # Low yellow
cmyk_color_space_planar[:, :, 3] = 0    # Low key (black)
cmyk_image_planar = Image.fromarray(cmyk_color_space_planar, 'CMYK')
cmyk_image_planar.save('./tmp/cmyk_image_deflate_planar.tiff', compression="tiff_deflate", tiffinfo={317: 2})

# Generate a Grayscale image with Deflate Compression and Planar Configuration
gray_image_planar = Image.new("L", (100, 100), 128)  # Medium gray square
gray_image_planar.save('./tmp/gray_image_deflate_planar.tiff', compression="tiff_deflate", tiffinfo={317: 2})

# Generate an RGB image with Deflate Compression, Planar Configuration, and Geospatial Metadata
geospatial_metadata = {
    33550: (0.01, 0.01, 0.0),  # ModelPixelScaleTag
    33922: (0.0, 0.0, 0.0, 10.0, 20.0, 30.0),  # ModelTiepointTag
    34737: ("WGS84",),  # GeoKeyDirectoryTag (pseudo code for simplicity)
}
rgb_image_geo = Image.new("RGB", (100, 100), (255, 255, 255))  # White square for simplicity
rgb_image_geo.save('./tmp/rgb_image_geo.tiff', compression="tiff_deflate", tiffinfo={**{317: 2}, **geospatial_metadata})