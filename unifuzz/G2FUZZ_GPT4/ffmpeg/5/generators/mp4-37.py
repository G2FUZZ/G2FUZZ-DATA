import cv2
import numpy as np
import os
from moviepy.editor import *

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define video specifications
width, height = 1920, 1080
fps = 30
duration_sec = 5
total_frames = fps * duration_sec

# Function to generate a frame
def generate_frame(frame_number):
    r = frame_number % 255
    g = (2 * frame_number) % 255
    b = (3 * frame_number) % 255
    return np.full((height, width, 3), (b, g, r), dtype=np.uint8)

# Try using a different codec and file format
fourcc_xvid = cv2.VideoWriter_fourcc(*'XVID')
video_path_atsc_xvid = os.path.join(output_dir, 'video_atsc_xvid.avi')
video_writer_atsc_xvid = cv2.VideoWriter(video_path_atsc_xvid, fourcc_xvid, fps, (width, height))

# Generate and write frames
for frame_number in range(total_frames):
    frame = generate_frame(frame_number)
    video_writer_atsc_xvid.write(frame)

# Release the video writer
video_writer_atsc_xvid.release()

# Check if the video file was created and is not empty
if not os.path.exists(video_path_atsc_xvid) or os.path.getsize(video_path_atsc_xvid) == 0:
    raise Exception("The video file was not created successfully.")

# Load the generated video using the new path and format
video_clip = VideoFileClip(video_path_atsc_xvid)

# Proceed with the rest of your processing...
print("Video has been saved to:", video_path_atsc_xvid)