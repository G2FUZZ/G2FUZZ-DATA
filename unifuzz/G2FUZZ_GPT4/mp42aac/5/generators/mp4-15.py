import cv2
import numpy as np
import os
import json

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define filenames
video_filename = './tmp/scalable_multiview_video.mp4'
private_stream_filename = './tmp/private_stream.json'

# Define video properties
frame_width = 640
frame_height = 480
fps = 30
frame_count = 60  # 2 seconds of video at 30 fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

# Initialize a dictionary to hold our private stream data
private_stream_data = {}

# Generate a simple video with colored frames and corresponding private stream data
for i in range(frame_count):
    # Create a frame with a gradient and text
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.putText(frame, f'Frame {i+1}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_value = int((i / frame_count) * 255)
    frame[:] = [color_value, color_value, 255 - color_value]  # Blue to yellow gradient

    # Write the frame into the file
    out.write(frame)

    # Simultaneously, build our "private stream" data
    # For demonstration, let's log the frame number and a simple message
    private_stream_data[f'Frame_{i+1}'] = f'This is private data for frame {i+1}.'

# Release the video writer object
out.release()

# Now, write our private stream data to a separate file
with open(private_stream_filename, 'w') as file:
    json.dump(private_stream_data, file, indent=4)

print(f'Video saved as {video_filename}')
print(f'Private stream data saved as {private_stream_filename}')