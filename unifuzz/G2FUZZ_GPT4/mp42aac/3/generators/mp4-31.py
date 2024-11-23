import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output path for the mp4 file
output_file_path = os.path.join(output_dir, 'compatibility_with_BIFS.mp4')

# Define the video specifications
frame_width = 640
frame_height = 480
fps = 24
duration_seconds = 10  # Extended duration to accommodate both descriptions
total_frames = duration_seconds * fps

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
out = cv2.VideoWriter(output_file_path, fourcc, fps, (frame_width, frame_height))

# Generate frames and add text
for frame_num in range(total_frames):
    # Create a blank image
    img = np.zeros((frame_height, frame_width, 3), np.uint8)
    img.fill(255)  # make the frame white
    
    # Define text properties
    if frame_num < total_frames / 2:  # First half for the first feature
        text = "Compatibility: Designed to be compatible with a wide range of devices."
    else:  # Second half for the new feature
        text = "BIFS (Binary Format for Scenes): MP4 files can include BIFS, which allows for the description and synchronization of interactive and animated scenes alongside the audiovisual content."
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5  # Adjusted to fit longer text
    font_color = (0, 0, 0)  # black
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    
    # Calculate text position (to be at the center)
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = (img.shape[0] + text_size[1]) // 2
    
    # Break text into multiple lines if it's too long
    text_wrap = text.split(' ')
    line = ''
    y_offset = 0
    for word in text_wrap:
        test_line = f"{line} {word}".strip()
        size = cv2.getTextSize(test_line, font, font_scale, thickness)[0]
        if size[0] > frame_width - 20:  # Check if the line is too wide
            cv2.putText(img, line, (text_x, text_y + y_offset), font, font_scale, font_color, thickness)
            line = word  # Start a new line with the current word
            y_offset += text_size[1] + 10  # Move to the next line
        else:
            line = test_line
    cv2.putText(img, line, (text_x, text_y + y_offset), font, font_scale, font_color, thickness)  # Print the last line
    
    # Write the frame to the video
    out.write(img)

# Release the VideoWriter object
out.release()

print(f"Video saved to {output_file_path}")