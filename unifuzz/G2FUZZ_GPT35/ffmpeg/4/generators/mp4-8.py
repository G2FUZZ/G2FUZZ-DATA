import numpy as np
import cv2

# Create a simple video using OpenCV with random frames and timecode metadata
output_path = './tmp/sample_video_with_timecode.mp4'
codec = 'mp4v'  # MPEG-4 Video Codec
fps = 24
frames = 100
frame_width = 640
frame_height = 480

out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*codec), fps, (frame_width, frame_height))

# Add timecode information to the video
for frame_number in range(frames):
    frame = np.random.randint(0, 256, (frame_height, frame_width, 3), dtype=np.uint8)
    
    # Generate timecode information
    timecode_info = f"Frame: {frame_number + 1} Time: {frame_number/fps:.2f}s"
    
    # Add timecode information to the frame (displayed at the top-left corner)
    cv2.putText(frame, timecode_info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    out.write(frame)

out.release()
print(f'Video with Timecode information saved to: {output_path}')