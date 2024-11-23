import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file = os.path.join(output_dir, 'streaming_video_multi_layer.mp4')

# Video properties
width, height = 640, 480
fps = 24  # Frames per second
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec

# Assuming the "Multi-layer Video Coding" feature is simulated by creating two layers:
# 1. Base layer - Lower resolution and lower bitrate
# 2. Enhancement layer - Higher resolution and bitrate, enhancing the base layer

# Create a VideoWriter object for the base layer
base_layer_file = os.path.join(output_dir, 'base_layer.mp4')
base_width, base_height = width // 2, height // 2  # Lower resolution for the base layer
base_out = cv2.VideoWriter(base_layer_file, fourcc, fps, (base_width, base_height))

# Create a VideoWriter object for the enhancement layer
enhancement_layer_file = os.path.join(output_dir, 'enhancement_layer.mp4')
# Enhancement layer has the same resolution as the original in this simple example
enhancement_out = cv2.VideoWriter(enhancement_layer_file, fourcc, fps, (width, height))

# Generate each frame of the video
for i in range(fps * duration):
    # Create a frame with synthetic content
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color_value = int((i / (fps * duration)) * 255)
    frame[:, :] = [color_value, 0, 255 - color_value]  # BGR format

    # Base layer frame - downscale for lower resolution
    base_layer_frame = cv2.resize(frame, (base_width, base_height), interpolation=cv2.INTER_AREA)

    # Write the frames to their respective video files
    base_out.write(base_layer_frame)
    enhancement_out.write(frame)

# Release the VideoWriter objects
base_out.release()
enhancement_out.release()

# Note: Actual multi-layer video coding (e.g., SVC, MVC) involves more complex encoding processes
# that are not directly supported through OpenCV's VideoWriter. This simulation separates the video
# into two layers manually, which is not equivalent to the standard's capabilities but demonstrates
# the concept of having multiple layers of video content.

print(f"Base layer video saved to {base_layer_file}")
print(f"Enhancement layer video saved to {enhancement_layer_file}")