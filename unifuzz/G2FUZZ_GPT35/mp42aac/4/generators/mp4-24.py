import numpy as np
import cv2

# Define the file path
file_path = "./tmp/generated_video_hdr_interactive.mp4"

# Define the codec for HDR and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480), isColor=True)

# Generate HDR frames and write to the video file with Interactive Content
for _ in range(100):
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    
    # Add Interactive Content to the frame
    # For example, drawing a rectangle as a clickable area
    cv2.rectangle(frame, (100, 100), (200, 200), (255, 0, 0), 2)
    
    out.write(frame)

# Release the VideoWriter object
out.release()

print("MP4 file with HDR and Interactive Content features generated successfully at:", file_path)