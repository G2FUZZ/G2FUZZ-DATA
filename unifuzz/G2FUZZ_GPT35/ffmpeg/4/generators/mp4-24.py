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

# Write the frames to a video file
out = cv2.VideoWriter(output_path + 'variable_frame_rate_with_object_oriented_media.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Add Object-oriented media feature: Interactive object
for i in range(fps * seconds):
    interactive_object = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)  # Creating an interactive object
    frame_with_object = frames[i].copy()
    frame_with_object[50:100, 50:100] = interactive_object  # Adding the interactive object to the frame
    out.write(frame_with_object)

# Release the video writer
out.release()