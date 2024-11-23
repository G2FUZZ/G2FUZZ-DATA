import numpy as np
import cv2

# Define the file path
file_path = "./tmp/extended_video.mp4"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

# Generate frames with text overlay and write to the video file
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(100):
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    text = f'Frame: {i}'
    cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    out.write(frame)

# Release the VideoWriter object
out.release()

print("MP4 file with text overlay generated successfully at:", file_path)