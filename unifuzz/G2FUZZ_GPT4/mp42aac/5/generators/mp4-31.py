import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename
filename = './tmp/scalable_multiview_video_with_descriptors_and_scene_description_with_progressive_download.mp4'

# Define video properties
frame_width = 640
frame_height = 480
fps = 30
frame_count = 60  # 2 seconds of video at 30 fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height), isColor=True)

# Generate a simple video with colored frames, object descriptors, and scene descriptions
for i in range(frame_count):
    # Create a frame with a gradient, text, object descriptor, and scene description
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.putText(frame, f'Frame {i+1}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_value = int((i / frame_count) * 255)
    frame[:] = [color_value, color_value, 255 - color_value]  # Blue to yellow gradient

    # Simulate the addition of an object descriptor by drawing a shape
    if i % 10 == 0:  # Add a descriptor shape every 10 frames
        cv2.rectangle(frame, (10, 10), (100, 100), (0, 255, 0), 3)
        cv2.putText(frame, 'Obj Desc', (15, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Simulate the addition of a scene description (note: in actual MP4 files, this would be metadata)
    if i % 15 == 0:  # Add a scene description every 15 frames
        cv2.putText(frame, 'Scene Description', (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, f'Scene {i//15 + 1}', (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()

# To support progressive download, optimize the MP4 file for fast start (moov atom at the beginning)
# This requires using external tools like 'ffmpeg' as OpenCV does not provide this functionality directly
os.system(f"ffmpeg -i {filename} -movflags +faststart -profile:v baseline -level 3.0 -pix_fmt yuv420p {filename.replace('.mp4', '_faststart.mp4')}")

print(f'Video saved as {filename.replace(".mp4", "_faststart.mp4")}')