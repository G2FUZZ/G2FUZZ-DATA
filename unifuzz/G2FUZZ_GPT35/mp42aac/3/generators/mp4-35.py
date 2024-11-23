import numpy as np
import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4V codec for MP4 files
out = cv2.VideoWriter('./tmp/generated_video_with_progress_bar.mp4', fourcc, 20.0, (640, 480))

# Generate a sample video frame with a dynamic progress bar overlay
for i in range(100):
    frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
    
    # Add Progress Bar overlay to the frame
    progress = int((i / 100) * 600)  # Calculate the progress bar length based on the frame count
    cv2.rectangle(frame, (20, 450), (20 + progress, 470), (0, 255, 0), -1)  # Draw progress bar
    
    cv2.putText(frame, f'Progress: {i}%', (25, 465), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  # Add progress text
    
    out.write(frame)

# Release the VideoWriter and close the file
out.release()