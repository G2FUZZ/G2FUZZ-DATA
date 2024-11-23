import os
import cv2
import numpy as np
import subprocess

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the texts to be added to the video with their properties
texts = [
    {"text": "Compatibility: FLV files are compatible with many media players.",
     "font_scale": 1.0, "text_color": (255, 255, 255), "font": cv2.FONT_HERSHEY_SIMPLEX},
    {"text": "Metadata Injection: FLV files support metadata.",
     "font_scale": 0.8, "text_color": (0, 255, 0), "font": cv2.FONT_HERSHEY_COMPLEX_SMALL},
    {"text": "Efficiency: Despite newer formats, FLV is still in use.",
     "font_scale": 0.6, "text_color": (0, 0, 255), "font": cv2.FONT_HERSHEY_TRIPLEX}
]

# Basic video parameters
width, height = 640, 480
fps = 24
duration = 10  # seconds
background_colors = [(0, 0, 0), (32, 32, 32), (64, 64, 64)]  # Cycling background colors

# Calculate the number of frames and frames per text
num_frames = duration * fps
frames_per_text = num_frames // len(texts)

# OpenCV doesn't directly support FLV, so we use XVID codec and later convert the file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
temp_video_path = './tmp/output.avi'
audio_file_path = './tmp/audio.mp3'  # Assume there's an audio file at this path
video_with_audio_path = './tmp/output_with_audio.flv'
metadata_injected_flv_path = './tmp/output_with_metadata.flv'

# Create a VideoWriter object
out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

current_background_index = 0

for frame_index in range(num_frames):
    # Cycle through background colors
    if frame_index % frames_per_text == 0:
        current_background_index = (current_background_index + 1) % len(background_colors)
    frame = np.full((height, width, 3), background_colors[current_background_index], np.uint8)
    
    # Determine which text to use
    text_index = frame_index // frames_per_text
    text_properties = texts[min(text_index, len(texts) - 1)]
    
    # Calculate text position
    (text_width, text_height), _ = cv2.getTextSize(text_properties["text"], text_properties["font"], fontScale=text_properties["font_scale"], thickness=1)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Add text to frame
    cv2.putText(frame, text_properties["text"], (x, y), text_properties["font"], text_properties["font_scale"], text_properties["text_color"], 1, cv2.LINE_AA)
    
    # Write frame to video
    out.write(frame)

# Release the VideoWriter
out.release()

# Convert the AVI video to FLV using FFmpeg, including the audio track
ffmpeg_command = [
    "ffmpeg", "-i", temp_video_path, "-i", audio_file_path, 
    "-c:v", "flv", "-c:a", "aac", "-strict", "experimental", "-f", "flv", 
    video_with_audio_path
]
result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("FFmpeg command failed:", result.stderr)
else:
    print("FFmpeg command succeeded.")

# Inject metadata into the FLV file
metadata_command = [
    "ffmpeg", "-i", video_with_audio_path, "-metadata", "title=Sample Video", 
    "-metadata", "comment=A sample video showcasing FLV features.", 
    metadata_injected_flv_path
]
result = subprocess.run(metadata_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Metadata injection command failed:", result.stderr)
else:
    print("Metadata injection command succeeded.")

# Clean up temporary files
if os.path.exists(temp_video_path):
    os.remove(temp_video_path)
if os.path.exists(video_with_audio_path):
    os.remove(video_with_audio_path)