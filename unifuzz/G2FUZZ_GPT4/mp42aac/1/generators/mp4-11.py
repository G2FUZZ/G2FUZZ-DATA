import numpy as np
import cv2
import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications for HEVC (H.265) Support
output_filename_hevc = output_dir + "example_streaming_hevc.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Codec definition for H.265
duration_sec = 5  # Duration of the video in seconds

# Create a VideoWriter object for HEVC (H.265)
out_hevc = cv2.VideoWriter(output_filename_hevc, fourcc_hevc, fps, frame_size)

# Generate frames
for i in range(fps * duration_sec):
    # Create a black image
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Define a moving rectangle parameters
    start_point = (i * 5 % frame_size[0], 50)  # Moving along the x-axis
    end_point = (start_point[0] + 100, 150)  # Fixed size
    color = (255, 255, 255)  # White
    thickness = -1  # Solid
    
    # Draw the rectangle on the frame
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Write the frame into the HEVC file
    out_hevc.write(frame)

# Release everything when the job is finished for HEVC
out_hevc.release()
print(f"Video with HEVC (H.265) support successfully saved to {output_filename_hevc}")

# MPEG-7 Metadata Creation
mpeg7_metadata_filename = output_dir + "mpeg7_metadata.xml"
root = ET.Element("Mpeg7", nsmap={'mpeg7': 'http://www.mpeg7.org'})
description = ET.SubElement(root, "Description")
description.set("type", "ContentEntityType")

# Here you can add more specific MPEG-7 metadata details as needed
descriptionText = ET.SubElement(description, "Text")
descriptionText.text = "Example content description for an MP4 file generated with Python."

tree = ET.ElementTree(root)
tree.write(mpeg7_metadata_filename, pretty_print=True, xml_declaration=True, encoding="UTF-8")

print(f"MPEG-7 Metadata successfully saved to {mpeg7_metadata_filename}")