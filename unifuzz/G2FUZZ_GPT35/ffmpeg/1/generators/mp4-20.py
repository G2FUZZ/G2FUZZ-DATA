import os
import subprocess

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy mp4 file with a random file size
file_name = './tmp/generated_video.mp4'
file_size = 10  # in MB (dummy value)
with open(file_name, 'wb') as f:
    f.seek(file_size * 1024 * 1024 - 1)
    f.write(b'\0')

# Add Poster Frames to the generated video
poster_frame_path = './tmp/poster_frame.jpg'
# Generate a dummy poster frame image
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'color=c=red:s=320x240', poster_frame_path])

# Add Rotation Metadata to the video
rotation_degrees = 90  # Dummy rotation value
subprocess.run(['ffmpeg', '-i', file_name, '-vf', f'transpose={rotation_degrees}', '-c:a', 'copy', file_name.replace('.mp4', '_rotated.mp4')])

print(f"Generated mp4 file with a size of {file_size} MB, poster frames, and rotation metadata at '{file_name.replace('.mp4', '_rotated.mp4')}'")