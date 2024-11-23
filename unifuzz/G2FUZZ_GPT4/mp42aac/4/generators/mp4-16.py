import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # AVC / H.264 codec
output_filename = os.path.join(output_dir, 'example_avc.mp4')
subtitle_filename = os.path.join(output_dir, 'example_avc.srt')

# Create a video writer object
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Function to convert frame number to timestamp
def frame_to_timestamp(frame_number, fps):
    total_seconds = frame_number / fps
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Generate frames and subtitles
subtitles = []
for i in range(duration * fps):
    # Create a black image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the square's position to create a moving effect
    center_x = int((width // 2) + (width // 4) * np.sin(2 * np.pi * i / (fps * 2)))
    center_y = int((height // 2) + (height // 4) * np.cos(2 * np.pi * i / (fps * 2)))
    start_point = (center_x - 50, center_y - 50)
    end_point = (center_x + 50, center_y + 50)
    
    # Draw a blue square
    cv2.rectangle(frame, start_point, end_point, (255, 0, 0), -1)
    
    # Write the frame to the video file
    out.write(frame)

    # Every second, add a subtitle
    if i % fps == 0:
        start_time = frame_to_timestamp(i, fps)
        end_time = frame_to_timestamp(i + fps - 1, fps)
        subtitles.append(f"{i // fps + 1}\n{start_time} --> {end_time}\nMoving square at second {i // fps + 1}\n")

# Release the video writer
out.release()

# Write the subtitle file
with open(subtitle_filename, "w") as srt_file:
    srt_file.writelines(subtitles)

print(f"Video saved as {output_filename}")
print(f"Subtitles saved as {subtitle_filename}")