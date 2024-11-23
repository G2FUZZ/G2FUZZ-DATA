import numpy as np
import cv2

# Generate a random video frame
height, width = 240, 320
frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/random_video_with_complex_features.flv', fourcc, 30, (width, height))

# Simulate adding an interactive quiz frame after every 10 frames with text overlay
quiz_text = "Question: What is the capital of France?"
quiz_frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background
cv2.putText(quiz_frame, quiz_text, (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

for i in range(100):
    out.write(frame)
    if i % 10 == 0:
        out.write(quiz_frame)  # Add quiz frame with text overlay every 10 frames

# Simulate changing background color dynamically after 50 frames
for i in range(50, 100):
    dynamic_frame = np.ones((height, width, 3), dtype=np.uint8) * (i * 5)  # Changing background color
    out.write(dynamic_frame)

# Release the VideoWriter and close the file
out.release()