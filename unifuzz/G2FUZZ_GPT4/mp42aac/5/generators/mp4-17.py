import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the initial part of the video
width, height = 640, 480
fps_start = 10  # Starting with a lower FPS
fps_end = 60  # Ending with a higher FPS for smooth motion
duration = 5  # seconds
output_filename = os.path.join(output_dir, "example_vfr.mp4")

# Create a video writer object with a starting fps
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 files
# Initially setting to fps_start, but this will be adjusted for VFR.
video = cv2.VideoWriter(output_filename, fourcc, fps_start, (width, height))

# Calculate total frames and increment per frame for FPS change
total_frames = fps_start * duration
fps_increment = (fps_end - fps_start) / total_frames

current_fps = fps_start
for t in np.linspace(0, duration, int(total_frames)):
    # Frame generation
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    size = 50
    x = int((width - size) * (t / duration))
    y = height // 2 - size // 2
    frame[y:y+size, x:x+size] = (0, 255, 0)  # Green square
    video.write(frame)
    
    # VFR: Adjust FPS for the next frame
    current_fps += fps_increment
    # Re-initialize video writer with new FPS - This is a conceptual approach. 
    # OpenCV's VideoWriter does not support changing FPS on the fly. 
    # For actual VFR, a different approach or post-processing might be needed.
    video.set(cv2.CAP_PROP_FPS, int(current_fps))

# Release the video writer
video.release()

# Note: This code attempts to demonstrate how one might go about changing the FPS over time within the same video file,
# which is an interpretation of VFR. However, OpenCV's VideoWriter does not natively support changing the frame rate
# dynamically in this way. For true VFR support, additional processing or a different library that supports VFR natively
# would be required. This code serves more as a conceptual demonstration rather than a functional implementation of VFR.