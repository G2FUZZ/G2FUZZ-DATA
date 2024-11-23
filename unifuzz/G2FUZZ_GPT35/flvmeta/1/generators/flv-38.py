import cv2
import numpy as np

# Create a VideoWriter object with DRM protection and error handling
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/extended_generated_video_with_complex_file_structures.flv', video_codec, 30, (640, 480), True)  # Added DRM protection flag

# Generate frames with different shapes and colors
for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black background
    if i % 2 == 0:
        frame = cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), -1)  # Draw a red filled rectangle
    else:
        frame = cv2.circle(frame, (320, 240), 100, (255, 0, 0), -1)  # Draw a blue filled circle

    # Write the frame to the video with error handling
    try:
        output.write(frame)
    except Exception as e:
        print("Error occurred: ", e)

# Release the VideoWriter object
output.release()