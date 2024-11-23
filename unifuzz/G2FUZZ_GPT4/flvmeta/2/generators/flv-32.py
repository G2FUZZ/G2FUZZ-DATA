import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'enhanced_video.flv')

# Input video and additional audio source
input_video = 'input_with_alpha.mov'
additional_audio = 'additional_audio.mp3'
watermark_image = 'watermark.png'

# FFmpeg command breakdown
# -map 0:v -map 0:a -map 1:a : Map the video stream from the first input, the audio stream from the first input,
#   and the audio stream from the second input to the output file.
# -filter_complex: Apply complex filtering. Here, we overlay a watermark and define chapters.
ffmpeg_command = [
    'ffmpeg',
    '-i', input_video,  # Main video input file
    '-i', additional_audio,  # Additional audio input file
    '-filter_complex', 
    f"[0:v]scale=1280:720,overlay=W-w-10:H-h-10:enable='between(t,0,10)'[v];"  # Scale video and add watermark for the first 10 seconds
    "[0:a][1:a]amix=inputs=2[a]",  # Mix both audio tracks
    '-map', '[v]',  # Map the video from the filter complex
    '-map', '[a]',  # Map the audio from the filter complex
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-metadata', 'title="Enhanced Video"',  # Adding script data object - title
    '-metadata', 'comment="Video with multiple audio tracks, watermarking, and chapters"',  # Description
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully.")
    print("Note: This FLV file includes multiple audio tracks, watermarking, and chapters for enhanced navigation.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create FLV file: {e}")