import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'alpha_support_vp6.flv')

# Sample command to generate a video with VP6 codec and alpha channel.
# This example assumes you have a source video with an alpha channel.
# Replace 'input_with_alpha.mov' with your actual input video file path.
# FFmpeg is used here for demonstration; it must be installed in the system.
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input_with_alpha.mov',  # Input file
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create FLV file: {e}")