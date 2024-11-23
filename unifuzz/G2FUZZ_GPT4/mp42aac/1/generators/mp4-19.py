import numpy as np
import cv2
import os

def generate_video(stream_id, output_dir, frame_width, frame_height, fps, duration_seconds):
    total_frames = duration_seconds * fps
    output_file = os.path.join(output_dir, f'output_video_stream_{stream_id}.mp4')
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'avc1'), fps, (frame_width, frame_height))

    for frame_num in range(total_frames):
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        if stream_id == 1:
            # First video stream: moving rectangle
            start_point = (frame_num % frame_width, 50)
            end_point = (start_point[0] + 100, 150)
            color = (255, 0, 0)  # red rectangle for stream 1
        else:
            # Second video stream: moving circle
            center = (frame_num % frame_width, frame_height // 2)
            radius = 50
            color = (0, 255, 0)  # green circle for stream 2
            frame = cv2.circle(frame, center, radius, color, -1)
        out.write(frame)
    
    out.release()
    print(f"Video stream {stream_id} file saved as {output_file}")

output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the videos
frame_width = 640
frame_height = 480
fps = 24
duration_seconds = 10

# Generate two video files for different streams
generate_video(1, output_dir, frame_width, frame_height, fps, duration_seconds)
generate_video(2, output_dir, frame_width, frame_height, fps, duration_seconds)

# Instruct users for the next steps
print("Two separate video streams have been generated.")
print("Use a player or streaming service that supports switchable video streams to integrate these videos for adaptive streaming or multi-view experiences.")