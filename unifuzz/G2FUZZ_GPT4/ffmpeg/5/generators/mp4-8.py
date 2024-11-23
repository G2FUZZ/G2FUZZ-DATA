import cv2
import numpy as np

# Define the resolution, video codec, frame rate, and duration
width, height = 1920, 1080
fps = 30
duration_sec = 10
codec = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
output_file = './tmp/generated_video.mp4'

# Create a video writer object
video = cv2.VideoWriter(output_file, codec, fps, (width, height))

# Generate a blank image (you can change the color as needed)
# Here, it's set to black using zeros. For other colors, use cv2.cvtColor if needed.
frame = np.zeros((height, width, 3), np.uint8)

# Fill the video with the blank image for the duration specified
for _ in range(fps * duration_sec):
    video.write(frame)

# Release the video writer
video.release()

print("Video generation completed.")