import cv2
import numpy as np
import os
import subprocess

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file including HEVC feature
output_filename_hevc = output_directory + 'streaming_example_hevc.mp4'
# Define the filename for the final output video with lossless audio
output_filename_final = output_directory + 'streaming_example_hevc_lossless_audio.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec for HEVC (High Efficiency Video Coding) and create VideoWriter object
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Use 'HEVC' or 'hvc1' depending on platform support
out_hevc = cv2.VideoWriter(output_filename_hevc, fourcc_hevc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    
    # Write the frame into the file using HEVC codec
    out_hevc.write(frame)

# Release the VideoWriter object for HEVC
out_hevc.release()

# Generate a silent lossless audio file with the same duration as the video
audio_filename = output_directory + 'silent_lossless.m4a'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-c:a', 'alac', '-t', str(duration_sec), audio_filename])

# Combine the video and the lossless audio into one file
subprocess.run(['ffmpeg', '-y', '-i', output_filename_hevc, '-i', audio_filename, '-c:v', 'copy', '-c:a', 'copy', output_filename_final])

# Cleanup temporary audio file
os.remove(audio_filename)

print(f'HEVC video file with Lossless Audio has been saved to {output_filename_final}')