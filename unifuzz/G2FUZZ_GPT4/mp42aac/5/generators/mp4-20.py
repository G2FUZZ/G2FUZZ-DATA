import cv2
import numpy as np
import os
from lxml import etree as ET

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename
filename = './tmp/scalable_multiview_video_with_isobmff.mp4'
metadata_filename = './tmp/scalable_multiview_video_with_isobmff_metadata.xml'

# Define video properties
frame_width = 640
frame_height = 480
fps = 30
frame_count = 60  # 2 seconds of video at 30 fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

# Generate a simple video with colored frames
for i in range(frame_count):
    # Create a frame with a gradient and text
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.putText(frame, f'Frame {i+1}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_value = int((i / frame_count) * 255)
    frame[:] = [color_value, color_value, 255 - color_value]  # Blue to yellow gradient

    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()

# Create MPEG-7 Metadata with additional ISOBMFF Basis feature
root = ET.Element("MPEG7", xmlns="urn:mpeg:mpeg7:schema:2001", xsi="http://www.w3.org/2001/XMLSchema-instance")
description = ET.SubElement(root, "Description")
multimediaContent = ET.SubElement(description, "MultimediaContent", type="Video")
video = ET.SubElement(multimediaContent, "Video")

# ISO Base Media File Format (ISOBMFF) Basis
isobmffBasis = ET.SubElement(video, "ISOBMFFBasis")
isobmffBasisDescription = ET.SubElement(isobmffBasis, "Description")
isobmffBasisDescription.text = "MP4 files are based on the ISO Base Media File Format, providing a standardized structure for time-based media files. This foundation ensures interoperability across various devices and software."

textAnnotation = ET.SubElement(video, "TextAnnotation")
freeTextAnnotation = ET.SubElement(textAnnotation, "FreeTextAnnotation")
freeTextAnnotation.text = "A simple generated video with a gradient background and frame numbers. Includes ISO Base Media File Format (ISOBMFF) Basis feature."

# Add more detailed metadata as needed here

# Write MPEG-7 Metadata to file
tree = ET.ElementTree(root)
tree.write(metadata_filename, pretty_print=True, xml_declaration=True, encoding="UTF-8")

print(f'Video saved as {filename}')
print(f'MPEG-7 Metadata saved as {metadata_filename}')