import cv2
import numpy as np
import os
import subprocess  # To use FFmpeg for making the video suitable for progressive download

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object for the main video
fourcc_main = cv2.VideoWriter_fourcc(*'mp4v')
output_path_main = os.path.join(output_dir, 'output_with_pip.mp4')
out_main = cv2.VideoWriter(output_path_main, fourcc_main, 20.0, (640, 480))

# Define the codec and create VideoWriter object for the PiP video
fourcc_pip = cv2.VideoWriter_fourcc(*'mp4v')
output_path_pip = os.path.join(output_dir, 'pip_video.mp4')
out_pip = cv2.VideoWriter(output_path_pip, fourcc_pip, 20.0, (160, 120))  # Smaller resolution for PiP

# Generate 100 frames with dynamic content for both videos
for i in range(100):
    # Main video frame
    img_main = np.zeros((480, 640, 3), np.uint8)
    cv2.putText(img_main, f'Frame {i}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
    cv2.ellipse(img_main, (320, 240), (100, 50), 0, 0, i * 360 / 100, (255, 0, 0), -1)

    # PiP video frame (smaller and simpler content)
    img_pip = np.zeros((120, 160, 3), np.uint8)
    cv2.putText(img_pip, f'PiP {i}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Write the frames into their respective files
    out_main.write(img_main)
    out_pip.write(img_pip)

# Release everything when the job is finished
out_main.release()
out_pip.release()
cv2.destroyAllWindows()

# Use FFmpeg to overlay PiP video onto the main video
overlay_output_path = os.path.join(output_dir, 'final_output_with_pip.mp4')
ffmpeg_cmd_overlay = f"ffmpeg -i {output_path_main} -i {output_path_pip} -filter_complex \"[0:v][1:v] overlay=480:360\" -c:a copy {overlay_output_path}"
subprocess.run(ffmpeg_cmd_overlay, shell=True)

# Use FFmpeg to make the final video suitable for progressive download
progressive_output_path = os.path.join(output_dir, 'progressive_final_output_with_pip.mp4')
ffmpeg_cmd_progressive = f"ffmpeg -i {overlay_output_path} -c copy -movflags +faststart {progressive_output_path}"
subprocess.run(ffmpeg_cmd_progressive, shell=True)

print(f"Video successfully saved with PiP and Progressive Download feature to {progressive_output_path}")