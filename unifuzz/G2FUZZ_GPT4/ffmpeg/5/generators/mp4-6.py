import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define video specifications
width, height = 640, 480
fps = 30
duration_sec = 5
total_frames = fps * duration_sec

# Function to generate a frame
def generate_frame(frame_number):
    # Create a synthetic image with changing colors
    r = frame_number % 255
    g = (2 * frame_number) % 255
    b = (3 * frame_number) % 255
    return np.full((height, width, 3), (b, g, r), dtype=np.uint8)

# Create and configure the video writer for H.264
fourcc_h264 = cv2.VideoWriter_fourcc(*'avc1')  # Use 'X264' if 'avc1' does not work
video_path_h264 = os.path.join(output_dir, 'video_h264.mp4')  # Corrected variable name here
video_writer_h264 = cv2.VideoWriter(video_path_h264, fourcc_h264, fps, (width, height))

# Create and configure the video writer for H.265
fourcc_h265 = cv2.VideoWriter_fourcc(*'hevc')  # Use 'H265' if 'hevc' does not work
video_path_h265 = os.path.join(output_dir, 'video_h265.mp4')  # Corrected variable name here
video_writer_h265 = cv2.VideoWriter(video_path_h265, fourcc_h265, fps, (width, height))

# Generate and write frames
for frame_number in range(total_frames):
    frame = generate_frame(frame_number)
    video_writer_h264.write(frame)
    video_writer_h265.write(frame)

# Release the video writers
video_writer_h264.release()
video_writer_h265.release()

print("Videos have been saved to:", output_dir)