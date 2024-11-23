# Import necessary libraries
import numpy as np
import cv2

# Define the video codec to be used
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'h264' or 'h265' for other codecs

# Specify the output file path
output_file = './tmp/generated_video_with_text_tracks.mp4'

# Define the resolution and frame rate
width = 640
height = 480
fps = 30

# Create a VideoWriter object to write the video with text tracks
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height), isColor=True)

# Generate a simple color gradient video
for i in range(100):
    img = np.ones((height, width, 3), np.uint8) * i
    out.write(img)

# Add text tracks for subtitles or captions
text_track_file = './tmp/subtitles.srt'
with open(text_track_file, 'w') as f:
    f.write("1\n00:00:00,000 --> 00:00:02,000\nHello, World!")

# Release the VideoWriter object and close the file
out.release()