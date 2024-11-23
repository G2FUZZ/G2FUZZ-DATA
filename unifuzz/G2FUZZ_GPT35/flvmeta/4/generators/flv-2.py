import os
import numpy as np
import cv2

# Create a new directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample video frame
frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

# Write the sample video frame to an FLV file
output_file = os.path.join(output_dir, 'sample.flv')
fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # FLV codec
out = cv2.VideoWriter(output_file, fourcc, 30.0, (640, 480))
for _ in range(100):
    out.write(frame)
out.release()

print(f'FLV file generated: {output_file}')