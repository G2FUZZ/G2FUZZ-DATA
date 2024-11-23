import numpy as np
import cv2

# Define the file path
file_path = "./tmp/extended_video_hdr_interactive.mp4"

# Define the codec for HDR and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480), isColor=True)

# Generate HDR frames with changing background color and text overlay
for i in range(100):
    frame = np.full((480, 640, 3), (i, 2*i, 3*i), dtype=np.uint8)  # Changing background color
    
    # Add text overlay to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Frame: {i}"
    cv2.putText(frame, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    out.write(frame)

# Release the VideoWriter object
out.release()

print("MP4 file with HDR and Interactive Content features generated successfully at:", file_path)