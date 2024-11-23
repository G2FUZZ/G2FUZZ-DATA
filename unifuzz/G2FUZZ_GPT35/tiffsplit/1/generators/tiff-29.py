import numpy as np
from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v2

# Create different images with varied resolutions and color modes
data1 = np.random.randint(0, 255, (200, 200), dtype=np.uint8)  # Random image data
data2 = np.random.randint(0, 255, (150, 150, 3), dtype=np.uint8)  # Random color image data

# Define tags for each image
tags_page1 = {
    256: 200,  # Image width
    257: 200,  # Image height
    258: 8,    # Bits per sample
    259: 1,    # Compression (1 = no compression)
    262: 0,    # Photometric interpretation (0 = white is zero)
    274: 1,    # Orientation
    277: 1,    # Samples per pixel
    282: (300, 1),  # X resolution (300 DPI)
    283: (300, 1),  # Y resolution (300 DPI)
}

tags_page2 = {
    256: 150,  # Image width
    257: 150,  # Image height
    258: 8,    # Bits per sample
    259: 1,    # Compression (1 = no compression)
    262: 2,    # Photometric interpretation (2 = RGB)
    274: 1,    # Orientation
    277: 3,    # Samples per pixel
    282: (150, 1),  # X resolution (150 DPI)
    283: (150, 1),  # Y resolution (150 DPI)
}

# Create images from the data arrays
img_page1 = Image.fromarray(data1)
img_page2 = Image.fromarray(data2)

# Add text annotations for each page
text_tags_page1 = ImageFileDirectory_v2()
text_tags_page1.tagdata = {270: ("TextAnnotation", 2, "Page 1 Text Annotation")}
text_tags_page2 = ImageFileDirectory_v2()
text_tags_page2.tagdata = {270: ("TextAnnotation", 2, "Page 2 Text Annotation")}

# Save both images as a multipage TIFF file with text annotations and custom tags
img_page1.save("./tmp/complex_multipage_with_text_annotations.tiff", tiffinfo=tags_page1, append_images=[img_page2], save_all=True, extratags=[text_tags_page1.tagdata, text_tags_page2.tagdata])