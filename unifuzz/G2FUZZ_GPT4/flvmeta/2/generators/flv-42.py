import subprocess
import os
import datetime

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'enhanced_complex_structure_with_more_layers.flv')

# Define input files
input_video1 = 'input1_with_alpha.mov'
input_video2 = 'input2_with_alpha.mov'
input_audio = 'custom_audio.mp3'
overlay_video1 = 'overlay_video1.mp4'  # First additional overlay video
overlay_video2 = 'overlay_video2.mp4'  # Second additional overlay video
watermark_image = 'watermark.png'  # Watermark image

# Create a file listing the files to concatenate
concat_file_path = os.path.join(output_dir, 'concat_list.txt')
with open(concat_file_path, 'w') as concat_file:
    concat_file.write(f"file '{input_video1}'\n")
    concat_file.write(f"file '{input_video2}'\n")

# More complex FFmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-f', 'concat',  # Indicates the input format for concatenation
    '-safe', '0',  # Allows using absolute paths in the concat file
    '-i', concat_file_path,  # Input concat file
    '-i', input_audio,  # Input audio file
    '-i', overlay_video1,  # Input first overlay video file
    '-i', overlay_video2,  # Input second overlay video file
    '-i', watermark_image,  # Input watermark image
    '-filter_complex',
    "[0:v]scale=1280:720,setsar=1[v0];"  # Scale main video, set sample aspect ratio to 1
    "[2:v]scale=320:180,setsar=1[v2];"  # Scale first overlay video, set sample aspect ratio to 1
    "[3:v]scale=640:360,setsar=1[v3];"  # Scale second overlay video, set sample aspect ratio to 1
    "[v0][v2]overlay=10:main_h-overlay_h-10:eval=init[ov1];"  # Overlay first video on the main video at bottom left
    "[ov1][v3]overlay=main_w-overlay_w-10:10:eval=init[ov2];"  # Overlay second video on the main video at top right
    "[ov2][4:v]overlay=W-w-10:H-h-10[video];"  # Overlay watermark on the video at top right corner
    "[1:a]volume=0.8[a1];"  # Adjust volume of the main audio
    "[2:a][3:a]amerge=inputs=2[a2];"  # Merge audio from the overlay videos
    "[a1][a2]amix=inputs=2:duration=first[audio];"  # Mix main audio with overlay audio
    "[video]drawtext=fontfile=/path/to/font.ttf:text='%{localtime\\:%X}':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=50[video_with_text];",  # Add dynamic text overlay with current time
    '-map', '[video_with_text]',  # Map the video from filter_complex
    '-map', '[audio]',  # Map the audio from filter_complex
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully with enhanced complex file structures with more layers.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create FLV file with enhanced complex file structures with more layers: {e}")