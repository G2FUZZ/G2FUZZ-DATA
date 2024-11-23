import cv2
import numpy as np

# Path to save the generated mp4 files
output_path = './tmp/'

# Define the properties for the video
width = 640
height = 480
fps = 30
seconds = 5

# Generate frames with varying frame rates
frames = []
for i in range(fps * seconds):
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    frames.append(frame)

# Write the frames to a video file with 360-degree video support
out = cv2.VideoWriter(output_path + '360_degree_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height), isColor=True)
for frame in frames:
    out.write(frame)

# Release the video writer
out.release()