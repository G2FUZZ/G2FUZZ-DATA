import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object
# Using 'X264' for Advanced Video Coding (AVC)
fourcc = cv2.VideoWriter_fourcc(*'X264')
output_path = os.path.join(output_dir, 'output_avc.mp4')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

# Generate 100 frames with dynamic content
for i in range(100):
    # Create a blank image with some dynamic elements
    img = np.zeros((480, 640, 3), np.uint8)
    cv2.putText(img, f'Frame {i}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
    cv2.ellipse(img, (320, 240), (100, 50), 0, 0, i*360/100, (255, 0, 0), -1)

    # Write the frame into the file
    out.write(img)

# Release everything when the job is finished
out.release()
cv2.destroyAllWindows()

print(f"Video successfully saved to {output_path}")