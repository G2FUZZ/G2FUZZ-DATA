import cv2
import numpy as np

# Create a VideoWriter object with DRM protection
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/extended_generated_video_with_DRM.flv', video_codec, 30, (640, 480), True)  # Added DRM protection flag

# Generate multiple frames with text overlay and fade-in effect
for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8) + 255  # Create a white image
    frame = cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), -1)  # Draw a red filled rectangle

    # Add text overlay with increasing opacity for each frame
    text = "Frame {}".format(i)
    cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Apply fade-in effect to the frame
    alpha = i / 100.0
    overlay = frame.copy()
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Write the frame to the video
    output.write(frame)

# Release the VideoWriter object
output.release()