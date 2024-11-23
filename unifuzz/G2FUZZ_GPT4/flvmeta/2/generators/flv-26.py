import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'complex_structure.flv')

# Define input files
input_video1 = 'input1_with_alpha.mov'
input_video2 = 'input2_with_alpha.mov'
input_audio = 'custom_audio.mp3'

# Create a file listing the files to concatenate
concat_file_path = os.path.join(output_dir, 'concat_list.txt')
with open(concat_file_path, 'w') as concat_file:
    concat_file.write(f"file '{input_video1}'\n")
    concat_file.write(f"file '{input_video2}'\n")

# Sample command to generate a video with VP6 codec, alpha channel, On2 VP6 Scaling, including the complexities mentioned.
ffmpeg_command = [
    'ffmpeg',
    '-f', 'concat',  # Indicates the input format for concatenation
    '-safe', '0',  # Allows using absolute paths in the concat file
    '-i', concat_file_path,  # Input concat file
    '-i', input_audio,  # Input audio file
    '-filter_complex', 
    "[0:v]scale=1280:720,setsar=1[v];"  # Scale video, set sample aspect ratio to 1
    "[v][1:a]",  # Map the scaled video and input audio
    '-map', '[v]',  # Map the video from filter_complex
    '-map', '1:a',  # Map the audio from the input audio file
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-vf', 'drawtext=text=\'Sample Text Overlay\':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2',  # Add text overlay
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully with complex file structures.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create FLV file with complex file structures: {e}")