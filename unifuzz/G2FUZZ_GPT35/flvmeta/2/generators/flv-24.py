import numpy as np
import cv2
import json

# Generate a random video frame
frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the aspect ratio for the video
aspect_ratio = {
    "width": 640,
    "height": 480
}

# Define the codec and create VideoWriter object with aspect ratio
fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/generated_video_with_aspect_ratio.flv', fourcc, 30, (aspect_ratio['width'], aspect_ratio['height']))

# Write frame to the video
for _ in range(100):
    out.write(frame)

# Release the VideoWriter
out.release()

# Add Aspect Ratio information to the FLV file
with open('./tmp/aspect_ratio.json', 'w') as f:
    json.dump(aspect_ratio, f)