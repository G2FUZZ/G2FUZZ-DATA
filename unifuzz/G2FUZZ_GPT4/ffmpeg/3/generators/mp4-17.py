import cv2
import numpy as np
import os
import subprocess
import shutil

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define video and audio specifications
output_filename_video = os.path.join(output_dir, 'example_video.mp4')
output_filename_audio = os.path.join(output_dir, 'example_audio.m4a')
output_filename_final = os.path.join(output_dir, 'final_video.mp4')
frame_width, frame_height = 640, 480
fps = 24
duration_sec = 5  # Duration of the video in seconds
frequency = 440  # Frequency in Hz (for the audio tone)

# Create a synthetic video using OpenCV
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the MP4 file
video = cv2.VideoWriter(output_filename_video, fourcc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Generate a frame with a color that changes over time
    frame = np.full((frame_height, frame_width, 3), (0, 0, 255 * i / (fps * duration_sec)), np.uint8)
    video.write(frame)

video.release()

# Generate a synthetic audio file with a tone of 440 Hz (A4) using ffmpeg (assuming ffmpeg is installed)
subprocess.run([
    'ffmpeg', '-y',  # Overwrite output file if it exists
    '-f', 'lavfi',  # Use lavfi pseudo-input device for synthetic input
    '-i', f'sine=frequency={frequency}:duration={duration_sec}',  # Generate a sine wave audio
    '-c:a', 'alac',  # Use ALAC codec for lossless audio encoding
    output_filename_audio
])

# Combine the video and audio into one file
subprocess.run([
    'ffmpeg', '-y',  # Overwrite output file if it exists
    '-i', output_filename_video,  # Input video file
    '-i', output_filename_audio,  # Input audio file
    '-c:v', 'copy',  # Copy video stream without re-encoding
    '-c:a', 'copy',  # Copy audio stream without re-encoding
    output_filename_final  # Output file
])

# Clean up temporary files if needed
os.remove(output_filename_video)
os.remove(output_filename_audio)

print(f"Video with lossless audio saved as {output_filename_final}")