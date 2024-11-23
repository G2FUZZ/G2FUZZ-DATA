import cv2
import numpy as np
import os
from datetime import datetime

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object
# Using 'mp4v' for compatibility. Change it according to your needs.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'X264' might not be available in your default installation
output_path = os.path.join(output_dir, 'complex_output.mp4')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

# Generate 200 frames with dynamic content
for i in range(200):
    # Create a blank image with some dynamic elements
    img = np.zeros((480, 640, 3), np.uint8)
    
    # Moving shapes
    cv2.circle(img, (i*3 % 640, 240), 50, (0, 255, 0), -1)  # Moving circle
    if i < 100:
        cv2.ellipse(img, (320, 240), (i, i//2), 0, 0, 180, (255, 255, 0), -1)  # Expanding ellipse
    
    # Text with changing color
    color = (i % 255, (i*2) % 255, (i*3) % 255)
    cv2.putText(img, f'Frame {i}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
    
    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(img, timestamp, (10, 450), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Write the frame into the file
    out.write(img)

# Release everything when the job is finished
out.release()
cv2.destroyAllWindows()

print(f"Video successfully saved to {output_path}")