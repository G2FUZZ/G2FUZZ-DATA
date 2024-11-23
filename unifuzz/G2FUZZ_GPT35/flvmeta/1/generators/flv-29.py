import cv2
import numpy as np

# Create a VideoWriter object with Dynamic streaming feature
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/generated_video_dynamic_streaming.flv', video_codec, 30, (640, 480))

# Generate a sample frame with Dynamic streaming
frame = np.zeros((480, 640, 3), dtype=np.uint8) + 255  # Create a white image
frame = cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), -1)  # Draw a red filled rectangle

# Write the frame to the video with Dynamic streaming
for _ in range(100):
    output.write(frame)

# Release the VideoWriter object
output.release()