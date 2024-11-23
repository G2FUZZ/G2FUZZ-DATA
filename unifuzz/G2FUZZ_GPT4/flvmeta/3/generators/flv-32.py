import os
import cv2
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the text to be added to the video
text = """
8. Compatibility: Despite the decline in usage due to the rise of HTML5 video and newer, more efficient formats like MP4, FLV files are still compatible with many standalone media players, video editing software, and some web browsers with the appropriate plugins.
2. **3GP and MP3 Compatibility**: FLV files can encapsulate material that is originally encoded in other formats like 3GP and MP4 without significant re-encoding. This makes FLV a versatile container for various types of multimedia content.
7. **Frame Skipping for Smooth Playback**: FLV players can be designed to skip frames to maintain audio and video synchronization on slower systems. This ensures that the audio continues to play smoothly even if the video has to drop frames to catch up.
"""

# Define basic parameters for the video
width, height = 640, 480
fps = 24
duration = 15  # Duration of the video in seconds
font_scale = 0.5
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)
background_colors = [(10*i % 256, 20*i % 256, 30*i % 256) for i in range(duration * fps)]  # Dynamic background color

# Calculate the number of frames
num_frames = duration * fps

# Splitting text into lines for better handling
lines = text.strip().split('\n')
line_height = cv2.getTextSize(text="Tg", fontFace=font, fontScale=font_scale, thickness=1)[0][1] + 5

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
temp_video_path = './tmp/output_with_dynamic_background_and_effects.avi'
flv_video_path = './tmp/output_with_dynamic_background_and_effects.flv'
out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

def apply_fade_effect(frame, current_frame, total_frames, fade_duration=3):
    """Apply fade-in and fade-out effect to the frame."""
    fade_frames = fade_duration * fps
    if current_frame <= fade_frames:  # Fade-in effect
        alpha = current_frame / fade_frames
    elif current_frame >= total_frames - fade_frames:  # Fade-out effect
        alpha = (total_frames - current_frame) / fade_frames
    else:
        alpha = 1
    return cv2.addWeighted(frame, alpha, frame, 0, 0)

for frame_num in range(num_frames):
    # Create a frame with dynamic background color
    frame = np.full((height, width, 3), background_colors[frame_num], np.uint8)
    y = 100  # Starting y position for the text
    for line in lines:
        # Calculate text size for each line
        (text_width, _), _ = cv2.getTextSize(line, font, fontScale=font_scale, thickness=1)
        x = (width - text_width) // 2
        cv2.putText(frame, line, (x, y), font, font_scale, text_color, 1, cv2.LINE_AA)
        y += line_height  # Move to the next line position
    # Display the current frame number
    cv2.putText(frame, f"Frame: {frame_num + 1}", (10, height - 10), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    # Apply fade-in and fade-out effect
    frame = apply_fade_effect(frame, frame_num, num_frames)
    out.write(frame)

# Release the VideoWriter
out.release()

# Convert the AVI video to FLV using FFmpeg
os.system(f"ffmpeg -i {temp_video_path} -c:v flv -f flv {flv_video_path}")

# Optionally, delete the temporary AVI file
os.remove(temp_video_path)