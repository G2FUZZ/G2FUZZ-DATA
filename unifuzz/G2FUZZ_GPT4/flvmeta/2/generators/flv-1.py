import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a single blue frame
frame_height = 720
frame_width = 1280
color_blue = (255, 0, 0)  # OpenCV uses BGR format
image = np.zeros((frame_height, frame_width, 3), np.uint8)
image[:] = color_blue

# Specify the output path and the codec
output_path = './tmp/output_video.mp4'  # Change to .mp4 for compatibility
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use a more compatible codec for MP4

# Create a VideoWriter object and write the frame
out = cv2.VideoWriter(output_path, fourcc, 1, (frame_width, frame_height))
out.write(image)
out.release()

# Convert the video to FLV format using moviepy (if necessary)
clip = VideoFileClip(output_path)
clip.write_videofile('./tmp/final_video.flv', codec='libx264', fps=24)