import numpy as np
import cv2
import os
import random

def generate_gradient_background(frame_size, color1, color2):
    """
    Generates a linear gradient background from color1 to color2.
    """
    # Create an empty image
    background = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    for i in range(frame_size[1]):
        ratio = i / frame_size[1]
        # Interpolate between color1 and color2
        color = tuple([int((1 - ratio) * c1 + ratio * c2) for c1, c2 in zip(color1, color2)])
        cv2.line(background, (0, i), (frame_size[0], i), color, 1)
    return background

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications
output_filename = output_dir + "complex_features_video.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec definition
duration_sec = 10  # Duration of the video in seconds
background_color1 = (0, 18, 255)  # Gradient start color (Red)
background_color2 = (255, 196, 0)  # Gradient end color (Blue)

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

# Generate frames
for i in range(fps * duration_sec):
    # Create a gradient background
    frame = generate_gradient_background(frame_size, background_color1, background_color2)
    
    # Generate random moving circles
    for _ in range(10):  # Draw 10 circles per frame
        center = (random.randint(0, frame_size[0]), random.randint(0, frame_size[1]))
        radius = random.randint(10, 30)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        thickness = -1  # Solid
        frame = cv2.circle(frame, center, radius, color, thickness)
    
    # Add a text overlay with the frame number
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Frame: {i}"
    text_position = (10, frame_size[1] - 10)
    font_scale = 1
    font_color = (0, 0, 0)  # Black
    line_type = 2
    cv2.putText(frame, text, text_position, font, font_scale, font_color, line_type)
    
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f"Video successfully saved to {output_filename}")