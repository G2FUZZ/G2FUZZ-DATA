import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'enhanced_output.flv')

# Define the path to the watermark image
watermark_image = 'watermark.png'  # Path to the watermark image

# Sample command to generate a video with:
# - VP6 codec and alpha channel
# - Custom resolution
# - Watermark overlay
# - Enhanced contrast using the curves filter
# This example assumes you have a source video with an alpha channel.
# Replace 'input_with_alpha.mov' with your actual input video file path.
# FFmpeg is used here for demonstration; it must be installed in the system.
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input_with_alpha.mov',  # Input file
    '-i', watermark_image,  # Watermark image input
    '-filter_complex', 
    "[0:v]scale=1280:720,curves=lighter[bg];"  # Resize to 1280x720 and adjust curves for the video
    "[bg][1:v]overlay=W-w-10:H-h-10",  # Overlay watermark on the top right corner
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully with enhanced features.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create enhanced FLV file: {e}")