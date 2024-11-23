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
output_filename = os.path.join(output_dir, 'example_avc_with_panoramic.mp4')
subtitle_filename = os.path.join(output_dir, 'example_avc_with_panoramic.srt')

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

# Generate a panoramic background (e.g., 3 times wider than the video frame)
panoramic_width = width * 3
panoramic_height = height
# Here, we simulate a panoramic image by creating a gradient image
panoramic_image = np.zeros((panoramic_height, panoramic_width, 3), dtype=np.uint8)
for i in range(panoramic_image.shape[1]):
    panoramic_image[:, i, :] = (i % 255, i % 255, 255 - i % 255)

# Generate frames, subtitles, and simulate panoramic view by shifting the viewport
subtitles = []
for i in range(duration * fps):
    # Calculate the viewport's x position to simulate panning
    shift = (i * panoramic_width // (duration * fps)) - width // 2
    frame = panoramic_image[:, shift:shift+width, :]
    
    # Every second, add a subtitle with updated panoramic view information
    if i % fps == 0:
        start_time = frame_to_timestamp(i, fps)
        end_time = frame_to_timestamp(i + fps - 1, fps)
        subtitles.append(f"{i // fps + 1}\n{start_time} --> {end_time}\nPanoramic view at second {i // fps + 1}\n")

    # Write the frame to the video file
    out.write(frame)

# Release the video writer
out.release()

# Write the subtitle file
with open(subtitle_filename, "w") as srt_file:
    srt_file.writelines(subtitles)

print(f"Video saved as {output_filename}")
print(f"Subtitles saved as {subtitle_filename}")