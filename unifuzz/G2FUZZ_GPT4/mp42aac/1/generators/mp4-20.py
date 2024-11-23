import numpy as np
import cv2
import os
from datetime import datetime, timedelta

def generate_video_with_timecode(stream_id, output_dir, frame_width, frame_height, fps, duration_seconds):
    total_frames = duration_seconds * fps
    output_file = os.path.join(output_dir, f'output_video_stream_{stream_id}_with_timecode.mp4')
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    # Start timecode at 00:00:00:00 (HH:MM:SS:FF)
    start_timecode = datetime.strptime("00:00:00:00", "%H:%M:%S:%f")
    frame_duration = timedelta(seconds=1/fps)

    for frame_num in range(total_frames):
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

        # Calculate current timecode
        current_timecode = start_timecode + frame_num * frame_duration
        timecode_str = current_timecode.strftime("%H:%M:%S:") + f"{int(current_timecode.microsecond / 1000000 * fps):02d}"

        if stream_id == 1:
            # First video stream: moving rectangle
            start_point = (frame_num % frame_width, 50)
            end_point = (start_point[0] + 100, 150)
            color = (255, 0, 0)  # red rectangle for stream 1
            cv2.rectangle(frame, start_point, end_point, color, -1)
        else:
            # Second video stream: moving circle
            center = (frame_num % frame_width, frame_height // 2)
            radius = 50
            color = (0, 255, 0)  # green circle for stream 2
            frame = cv2.circle(frame, center, radius, color, -1)

        # Optionally, overlay the timecode on the video frame
        cv2.putText(frame, timecode_str, (50, frame_height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        out.write(frame)

    out.release()
    print(f"Video stream {stream_id} file with timecode saved as {output_file}")

output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the videos
frame_width = 640
frame_height = 480
fps = 24
duration_seconds = 10

# Generate two video files for different streams with timecode
generate_video_with_timecode(1, output_dir, frame_width, frame_height, fps, duration_seconds)
generate_video_with_timecode(2, output_dir, frame_width, frame_height, fps, duration_seconds)

# Instruct users for the next steps
print("Two separate video streams with timecode have been generated.")
print("Use a player or editing software that supports timecode tracks for video editing or synchronization purposes.")