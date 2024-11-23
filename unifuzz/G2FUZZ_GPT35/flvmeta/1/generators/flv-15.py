import cv2
import numpy as np

# Create a VideoWriter object with DRM protection
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/generated_video_with_DRM.flv', video_codec, 30, (640, 480), True)  # Added DRM protection flag

# Generate a sample frame
frame = np.zeros((480, 640, 3), dtype=np.uint8) + 255  # Create a white image
frame = cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), -1)  # Draw a red filled rectangle

# Write the frame to the video
for _ in range(100):
    output.write(frame)

# Release the VideoWriter object
output.release()