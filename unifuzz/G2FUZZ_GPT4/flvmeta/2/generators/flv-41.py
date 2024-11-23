import cv2
import numpy as np
import os
from scipy.io import wavfile
from moviepy.editor import *

# Function to generate a colored frame with optional text
def generate_colored_frame(color, frame_height=720, frame_width=1280, text=None):
    image = np.zeros((frame_height, frame_width, 3), np.uint8)
    image[:] = color  # BGR Format
    if text:
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(text, font, 1, 2)[0]
        textX = (image.shape[1] - textsize[0]) / 2
        textY = (image.shape[0] + textsize[1]) / 2
        cv2.putText(image, text, (int(textX), int(textY)), font, 1, (255, 255, 255), 2)
    return image

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Frame dimensions and video properties
frame_height = 720
frame_width = 1280
duration = 5  # seconds for the video
fps = 24  # frames per second

# Specify the output path and the codec for video
output_path = './tmp/output_video_complex.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create a VideoWriter object to add multiple frames
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Generate and write frames of different colors with "Hello World!" text on the first color
first_color = True
for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:  # Blue, Green, Red
    for _ in range(fps * duration):  # Add each color for 'duration' seconds
        if first_color:
            frame = generate_colored_frame(color, frame_height, frame_width, "Hello World!")
            first_color = False
        else:
            frame = generate_colored_frame(color, frame_height, frame_width)
        out.write(frame)

out.release()

# The rest of your code for generating audio and combining it with the video remains the same