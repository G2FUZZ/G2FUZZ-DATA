import cv2
import numpy as np
import os
import subprocess
from mutagen.mp4 import MP4

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# File paths for generated components
output_video_path = os.path.join(output_dir, 'complex_structure_video.mp4')
output_audio_path = os.path.join(output_dir, 'complex_structure_audio.mp3')
final_output_path = output_video_path.replace('.mp4', '_final.mp4')

# Assuming video and audio generation code remains the same and is successful...

# Combine video and audio using ffmpeg, adding multiple audio tracks
command = [
    'ffmpeg', '-i', output_video_path, '-i', output_audio_path,
    '-filter_complex', '[0:a][1:a]amerge=inputs=2[a]',
    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', final_output_path
]

try:
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("ffmpeg command executed successfully")
except subprocess.CalledProcessError as e:
    print(f"ffmpeg command failed with error: {e.stderr.decode()}")

# Before accessing the file, check if it exists to avoid the error
if os.path.exists(final_output_path):
    video_file = MP4(final_output_path)
    video_file["\xa9nam"] = "Complex Structure Video"
    video_file["\xa9ART"] = "Author Name"
    video_file["\xa9alb"] = "Sample Album"
    video_file["\xa9gen"] = "Experimental"
    # For chapters, a more complex process involving other libraries or direct MP4 box manipulation might be necessary

    video_file.save()

    print(f'Complex structured video saved to {final_output_path}')
else:
    print(f"Failed to create the video file at {final_output_path}. Please check the ffmpeg command output for errors.")