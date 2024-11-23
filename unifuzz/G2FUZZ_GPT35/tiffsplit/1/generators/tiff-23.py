import numpy as np
from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v2

# Create a simple black and white image
data = np.zeros((100, 100), dtype=np.float32)
data[25:75, 25:75] = 1.0  # Add a white square in the middle

# Set some example tags for the first image
tags_page1 = {
    256: 100,  # Image width
    257: 100,  # Image height
    258: 32,   # Bits per sample (32-bit float for HDR)
    259: 1,    # Compression (1 = no compression)
    262: 0,    # Photometric interpretation (0 = white is zero)
    274: 1,    # Orientation
    277: 1,    # Samples per pixel
    282: (72, 1),  # X resolution
    283: (72, 1),  # Y resolution
}

# Create a new image with the specified tags for the first image
img_page1 = Image.fromarray(data)

# Create a new image with the specified tags for the second image
img_page2 = Image.fromarray(np.flipud(data))  # Flip the image for demonstration

# Add text annotations
text_tags = ImageFileDirectory_v2()
text_tags.tagdata = {270: ("TextAnnotation", 2, "Example Text Annotation")}

# Add HDR feature tag
hdr_tags = ImageFileDirectory_v2()
hdr_tags.tagdata = {33432: ("HighDynamicRangeImaging", 7, "TIFF files support high bit depths and floating-point pixel values, making them suitable for storing HDR images with a wide dynamic range.")}

# Add Color Management feature tag
color_management_tags = ImageFileDirectory_v2()
color_management_tags.tagdata = {34675: ("ColorManagement", 2, "TIFF files support embedded color profiles for consistent color reproduction across different devices and platforms.")}

# Save all images as a multipage TIFF file with text annotations, HDR feature, and Color Management feature
img_page1.save("./tmp/example_multipage_with_text_annotations_and_hdr_and_color_management.tiff", tiffinfo=tags_page1, append_images=[img_page2], save_all=True, extratags={**text_tags.tagdata, **hdr_tags.tagdata, **color_management_tags.tagdata})