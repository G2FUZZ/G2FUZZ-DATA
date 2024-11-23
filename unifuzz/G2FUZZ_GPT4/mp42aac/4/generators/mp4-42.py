import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Video properties
width, height = 640, 480
fps = 30
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # AVC / H.264 codec
output_filename = os.path.join(output_dir, 'complex_avc_with_effects.mp4')
subtitle_filename = os.path.join(output_dir, 'complex_avc_with_effects.srt')

# Create a video writer object
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Generate a dynamic background image
def create_background(frame_number, width, height, fps):
    bg = np.zeros((height, width, 3), dtype=np.uint8)
    color_phase = np.sin(2 * np.pi * frame_number / (fps * 2)) * 127 + 128
    bg[:, :] = (0, color_phase, 255 - color_phase)
    return bg

# Overlay text that changes over time
def overlay_text(frame, text, position, font_scale=1.0, color=(255, 255, 255)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, position, font, font_scale, color, 2, cv2.LINE_AA)

# Draw shapes with animation
def draw_moving_circle(frame, frame_number, fps):
    radius = 20
    x_pos = int((frame_number / (fps * duration)) * frame.shape[1])
    y_pos = frame.shape[0] // 2
    cv2.circle(frame, (x_pos, y_pos), radius, (255, 0, 0), -1)

# Function to convert frame number to timestamp
def frame_to_timestamp(frame_number, fps):
    total_seconds = frame_number / fps
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Generate frames, subtitles, and add effects
subtitles = []
for i in range(duration * fps):
    frame = create_background(i, width, height, fps)
    
    # Add moving circle
    draw_moving_circle(frame, i, fps)
    
    # Overlay text
    text = f"Second: {i // fps}, Frame: {i}"
    overlay_text(frame, text, (50, 50))
    
    # Every second, add a subtitle
    if i % fps == 0:
        start_time = frame_to_timestamp(i, fps)
        end_time = frame_to_timestamp(i + fps - 1, fps)
        subtitles.append(f"{i // fps + 1}\n{start_time} --> {end_time}\nDynamic scene at second {i // fps + 1}\n")

    # Write the frame to the video file
    out.write(frame)

# Release the video writer
out.release()

# Write the subtitle file
with open(subtitle_filename, "w") as srt_file:
    srt_file.writelines(subtitles)

print(f"Video saved as {output_filename}")
print(f"Subtitles saved as {subtitle_filename}")