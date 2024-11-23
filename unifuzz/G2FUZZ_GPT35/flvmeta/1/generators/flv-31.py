import cv2
import numpy as np

# Create a VideoWriter object with DRM protection
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/extended_generated_video_with_DRM.flv', video_codec, 30, (640, 480), True)  # Added DRM protection flag

# Generate and write frames with varying rectangle sizes and text overlay
for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8) + 255  # Create a white image
    frame = cv2.rectangle(frame, (50+i, 50+i), (200+i, 200+i), (0, 0, 255), -1)  # Draw a red filled rectangle with increasing size
    text = f'Frame: {i+1}'
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Add text overlay with frame number
    output.write(frame)

# Release the VideoWriter object
output.release()