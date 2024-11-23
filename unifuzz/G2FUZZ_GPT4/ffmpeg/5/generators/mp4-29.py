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

# Function to generate a frame with varying complexity (to simulate different bitrates)
def generate_frame(frame_number, complexity=1):
    # Create a synthetic image with changing colors and variable complexity
    step = complexity * 5  # Adjust step size to simulate different bitrates
    r = (frame_number * step) % 255
    g = ((2 * frame_number) * step) % 255
    b = ((3 * frame_number) * step) % 255
    return np.full((height, width, 3), (b, g, r), dtype=np.uint8)

# Create and configure the video writers for different bitrates (simulating Switch Tracks)
video_paths = [os.path.join(output_dir, f'video_bitrate_{i}.mp4') for i in range(1, 4)]
video_writers = [cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'avc1'), fps, (width, height)) for path in video_paths]

# Generate and write frames for each bitrate version
for frame_number in range(total_frames):
    for i, writer in enumerate(video_writers):
        frame = generate_frame(frame_number, complexity=i+1)
        writer.write(frame)

# Release the video writers
for writer in video_writers:
    writer.release()

print("Videos with different bitrates have been saved. Please utilize an external tool to create Switch Tracks.")

# Note: OpenCV's cv2.VideoWriter does not directly support generating Switch Tracks.
# Creating Switch Tracks typically involves using a different library or post-processing tool,
# such as MP4Box from the GPAC suite or FFmpeg, after the video files have been created.

# Example using FFmpeg to create a DASH (Dynamic Adaptive Streaming over HTTP) manifest which supports Switch Tracks:
# ffmpeg -i video_bitrate_1.mp4 -i video_bitrate_2.mp4 -i video_bitrate_3.mp4 -map 0 -map 1 -map 2 -c copy -f dash output.mpd

print("To create Switch Tracks, use an external tool like FFmpeg to create a DASH manifest or similar.")