import cv2
import numpy as np
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the filename
filename = './tmp/sample_video_with_mpegj.mp4'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # You may also use 'avc1' for H.264, but 'mp4v' is more universally supported
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,  480))

# Generate 10 seconds of video (assuming 20 FPS)
for _ in range(200):
    # Create a frame (Here, just creating a frame with random colors)
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    
    # Write the frame into the file
    out.write(frame)

# Release everything if job is finished
out.release()

# MPEG-J Support is not directly implemented in Python or OpenCV, as it requires embedding Java applications within the MP4 container.
# This functionality goes beyond the scope of a simple Python script and involves post-processing the MP4 file with specialized tools
# or using a multimedia framework that supports MPEG-J, such as GPAC or similar, to inject Java applications into the MP4 container.
# Here, we would need to use external tools or manual processes to add MPEG-J support to the generated MP4 file.

print(f"Video saved as {filename}")
# Note: Additional steps required to embed MPEG-J applications are not covered in this script.