import cv2
import numpy as np
import os
import textwrap

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
texts = [
    "Efficiency: MP4 files are designed to be highly efficient in terms of compression, enabling the storage and transmission of high-quality video and audio with relatively small file sizes.",
    "Rate Adaptation: MP4 supports dynamic rate adaptation, meaning the bitrate of the audio and video can change over time to adapt to varying network conditions or to optimize for different playback scenarios."
]

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 files
output_file = os.path.join(output_dir, 'features.mp4')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Prepare text overlay settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)
font_thickness = 2
start_x, start_y = 50, 50  # Text start position
line_spacing = 10  # Spacing between lines

# Calculate number of frames
total_frames = fps * duration

# Generate frames
for frame in range(total_frames):
    img = np.zeros((height, width, 3), np.uint8)  # Create a blank image
    y = start_y
    
    # Iterate through each text to add them to the frame
    for text in texts:
        wrapped_text = textwrap.wrap(text, width=100)  # Adjust wrapping according to your needs
        for line in wrapped_text:
            text_size, _ = cv2.getTextSize(line, font, font_scale, font_thickness)
            text_w, text_h = text_size
            
            # Add text line by line
            cv2.putText(img, line, (start_x, y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)
            y += text_h + line_spacing  # Move to the next line position
    
    out.write(img)  # Write the frame to the video file

# Release the VideoWriter object
out.release()

print(f"Video file saved: {output_file}")