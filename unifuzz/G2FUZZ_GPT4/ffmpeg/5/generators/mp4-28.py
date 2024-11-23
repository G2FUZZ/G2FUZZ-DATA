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

# Create and configure the video writer for H.264 with Hint Tracks
fourcc_h264 = cv2.VideoWriter_fourcc(*'avc1')  # Use 'X264' if 'avc1' does not work
video_path_h264_hint = os.path.join(output_dir, 'video_h264_hint.mp4')  # Path for video with Hint Tracks
video_writer_h264_hint = cv2.VideoWriter(video_path_h264_hint, fourcc_h264, fps, (width, height))

# Unfortunately, OpenCV's cv2.VideoWriter does not directly support adding hint tracks to the video files.
# Adding hint tracks typically involves using a different library or post-processing tool,
# such as MP4Box from the GPAC suite or FFmpeg, after the video file has been created.

# Generate and write frames
for frame_number in range(total_frames):
    frame = generate_frame(frame_number)
    video_writer_h264_hint.write(frame)

# Release the video writer
video_writer_h264_hint.release()

print("Video with H.264 codec has been saved. Please utilize an external tool to add Hint Tracks.")

# Note: You will need to use an external tool like MP4Box or FFmpeg to add hint tracks.
# For example, using MP4Box to add a hint track:
# MP4Box -hint video_h264_hint.mp4

print("Please use an external tool like MP4Box or FFmpeg to add hint tracks.")