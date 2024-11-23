import cv2
import numpy as np
import os
import subprocess  # To use FFmpeg for making the video suitable for progressive download

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object
# Using 'mp4v' as a codec compatible with most environments
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
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

# Use FFmpeg to make the video suitable for progressive download
# This involves moving some metadata to the beginning of the file (faststart)
progressive_output_path = os.path.join(output_dir, 'progressive_output_avc.mp4')
ffmpeg_cmd = f"ffmpeg -i {output_path} -c copy -movflags +faststart {progressive_output_path}"
subprocess.run(ffmpeg_cmd, shell=True)

print(f"Video successfully saved with Progressive Download feature to {progressive_output_path}")