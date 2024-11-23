import numpy as np
import cv2

# Create a simple video using OpenCV with random frames
output_path = './tmp/sample_video.mp4'
codec = 'mp4v'  # MPEG-4 Video Codec
fps = 24
frames = 100
frame_width = 640
frame_height = 480

out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*codec), fps, (frame_width, frame_height))

for _ in range(frames):
    frame = np.random.randint(0, 256, (frame_height, frame_width, 3), dtype=np.uint8)
    out.write(frame)

out.release()
print(f'Video saved to: {output_path}')