import numpy as np
import cv2

# Generate a random video frame
height, width = 240, 320
frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/random_video_with_quiz.flv', fourcc, 30, (width, height))

# Simulate adding an interactive quiz frame after every 10 frames
quiz_frame = np.zeros((height, width, 3), dtype=np.uint8)  # Placeholder for quiz frame

for i in range(100):
    out.write(frame)
    if i % 10 == 0:
        out.write(quiz_frame)  # Add quiz frame every 10 frames

# Release the VideoWriter and close the file
out.release()