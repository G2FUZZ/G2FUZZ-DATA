import numpy as np
import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4V codec for MP4 files
out = cv2.VideoWriter('./tmp/generated_video_with_closed_captions.mp4', fourcc, 20.0, (640, 480))

# Generate a sample video frame
for _ in range(100):
    frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
    
    # Add Closed Captions to the frame
    # For demonstration purposes, let's add a simple text overlay as closed captions
    cv2.putText(frame, 'Closed Captions Example', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    out.write(frame)

# Release the VideoWriter and close the file
out.release()