import os
import cv2
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the text to be added to the video
text = """
8. Compatibility: Despite the decline in usage due to the rise of HTML5 video and newer, more efficient formats like MP4, FLV files are still compatible with many standalone media players, video editing software, and some web browsers with the appropriate plugins.
2. **3GP and MP4 Compatibility**: FLV files can encapsulate material that is originally encoded in other formats like 3GP and MP4 without significant re-encoding. This makes FLV a versatile container for various types of multimedia content.
7. **Frame Skipping for Smooth Playback**: FLV players can be designed to skip frames to maintain audio and video synchronization on slower systems. This ensures that the audio continues to play smoothly even if the video has to drop frames to catch up.
"""

# Define basic parameters for the video
width, height = 640, 480
fps = 24
duration = 15  # Adjusted duration to fit additional text
font_scale = 0.5  # Adjust font scale to fit additional text
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# Calculate the number of frames
num_frames = duration * fps

# Prepare to calculate text size and position
# Splitting text into lines for better handling
lines = text.strip().split('\n')
line_height = cv2.getTextSize(text="Tg", fontFace=font, fontScale=font_scale, thickness=1)[0][1] + 5  # Adding a small space between lines

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
temp_video_path = './tmp/output_with_frame_skipping.avi'
flv_video_path = './tmp/output_with_frame_skipping.flv'
out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

for _ in range(num_frames):
    frame = np.full((height, width, 3), background_color, np.uint8)
    y = 100  # Starting y position
    for line in lines:
        # Calculate text size for each line
        (text_width, _), _ = cv2.getTextSize(line, font, fontScale=font_scale, thickness=1)
        x = (width - text_width) // 2
        cv2.putText(frame, line, (x, y), font, font_scale, text_color, 1, cv2.LINE_AA)
        y += line_height  # Move to the next line position
    out.write(frame)

# Release the VideoWriter
out.release()

# Convert the AVI video to FLV using FFmpeg
os.system(f"ffmpeg -i {temp_video_path} -c:v flv -f flv {flv_video_path}")

# Optionally, delete the temporary AVI file
os.remove(temp_video_path)