import os
import cv2
import numpy as np
import subprocess

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define texts to be added to the video streams
texts = [
    "8. Compatibility: Despite the decline in usage due to the rise of HTML5 video...",
    "3. **Metadata Injection**: FLV files allow for the injection of additional metadata...",
]

# Define basic parameters for the videos
width, height = 640, 480
fps = 24
duration = 5  # seconds
font_scale = 1.0
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# Calculate the number of frames
num_frames = duration * fps

# OpenCV doesn't directly support FLV, so we use XVID codec for temporary files
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Paths for temporary and final videos
temp_video_paths = ['./tmp/output1.avi', './tmp/output2.avi']
flv_video_paths = ['./tmp/output1.flv', './tmp/output2.flv']
combined_flv_path = './tmp/combined_output.flv'
metadata_injected_flv_path = './tmp/combined_output_with_metadata.flv'

# Create each video stream with different text
for i, text in enumerate(texts):
    (text_width, text_height), _ = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    out = cv2.VideoWriter(temp_video_paths[i], fourcc, fps, (width, height))
    for _ in range(num_frames):
        frame = np.full((height, width, 3), background_color, np.uint8)
        cv2.putText(frame, text, (x, y), font, font_scale, text_color, 1, cv2.LINE_AA)
        out.write(frame)
    out.release()

    # Convert each AVI video to FLV using FFmpeg
    os.system(f"ffmpeg -i {temp_video_paths[i]} -c:v flv -f flv {flv_video_paths[i]}")

# Combine the FLV files into a single file with multiple video streams
combine_command = ["ffmpeg"]
for flv_path in flv_video_paths:
    combine_command += ["-i", flv_path]
combine_command += ["-filter_complex", "concat=n=2:v=1:a=0", combined_flv_path]
subprocess.run(combine_command)

# Inject metadata into the combined FLV file
metadata_command = f"ffmpeg -i {combined_flv_path} -metadata title='Sample Video' -metadata comment='Multiple Streams Example' {metadata_injected_flv_path}"
os.system(metadata_command)

# Optionally, delete the temporary AVI and FLV files
for path in temp_video_paths + flv_video_paths:
    os.remove(path)
os.remove(combined_flv_path)