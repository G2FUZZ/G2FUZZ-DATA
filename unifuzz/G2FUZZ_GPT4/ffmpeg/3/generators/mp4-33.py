import cv2
import numpy as np
import os

def add_subtitles(frame, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, 
                  font_scale=1, font_color=(255, 255, 255), thickness=2, background_color=(0,0,0)):
    """
    Add subtitles to a frame.
    """
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_w, text_h = text_size
    x, y = position
    
    # Add background for text for better readability
    cv2.rectangle(frame, (x, y - text_h - 10), (x + text_w, y + 10), background_color, -1)
    cv2.putText(frame, text, (x, y), font, font_scale, font_color, thickness)

    return frame

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define output file path
output_file = output_dir + 'example_avc_with_subtitles.mp4'

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # AVC codec

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate synthetic frames with subtitles
for t in range(fps * duration):
    # Create a frame with changing colors
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:, :, 0] = (t * 5) % 256  # Red channel
    frame[:, :, 1] = (t * 3) % 256  # Green channel
    frame[:, :, 2] = (t * 1) % 256  # Blue channel
    
    # Add subtitles to the frame
    subtitle_text = "Time: {:02d}s".format(t // fps)
    frame = add_subtitles(frame, subtitle_text, (10, height - 30))
    
    # Write the frame to the video file
    out.write(frame)

# Release the VideoWriter object
out.release()

print(f"Video file with subtitles has been saved to {output_file}")