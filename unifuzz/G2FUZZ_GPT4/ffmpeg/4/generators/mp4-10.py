import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object with H264 which supports VBR
fourcc = cv2.VideoWriter_fourcc(*'X264')

output_path = os.path.join(output_dir, 'generated_video_vbr.mp4')

# For incorporating VBR, we utilize the VideoWriter's parameters. However, 
# OpenCV's VideoWriter does not directly support setting VBR through public API parameters.
# Instead, VBR is often a feature of the codec and container. H.264 in an MP4 container, 
# as specified, can use VBR if configured in the codec settings externally.
# We proceed with the assumption that the codec defaults or external configuration enable VBR.
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

# Generate 100 frames with changing colors and complexity to potentially benefit from VBR
for i in range(100):
    # Create a frame with varying complexity
    if i % 2 == 0:
        # Simpler frame: a single color
        frame = np.ones((480, 640, 3), dtype=np.uint8) * np.random.randint(0, 255, (1, 3)).astype(np.uint8)
    else:
        # More complex frame: random noise
        frame = np.random.randint(0, 255, (480, 640, 3)).astype(np.uint8)
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f"Video successfully saved to {output_path}")