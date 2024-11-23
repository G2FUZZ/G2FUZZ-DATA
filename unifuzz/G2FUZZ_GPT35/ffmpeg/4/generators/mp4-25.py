import numpy as np
import cv2

# Create a simple video using OpenCV with random frames and variable duration frames
output_path = './tmp/sample_video_with_variable_duration_frames.mp4'
codec = 'mp4v'  # MPEG-4 Video Codec
fps = 24
frames = 100
frame_width = 640
frame_height = 480

# Additional feature: Variable duration frames
frame_durations = np.random.uniform(0.1, 0.5, frames)  # Random frame durations between 0.1 and 0.5 seconds

out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*codec), fps, (frame_width, frame_height), isColor=True)

for i in range(frames):
    frame = np.random.randint(0, 256, (frame_height, frame_width, 3), dtype=np.uint8)
    for _ in range(int(fps * frame_durations[i])):
        out.write(frame)

out.release()
print(f'Video with variable duration frames saved to: {output_path}')