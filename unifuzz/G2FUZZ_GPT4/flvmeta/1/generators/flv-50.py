import subprocess
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, "complex_generated_video.flv")

# Ensure you have the necessary files in the expected paths
# For the purposes of this example, these files are placeholders and need to exist
video_file_1 = "path/to/your/first/video.mp4"
video_file_2 = "path/to/your/second/video.mp4"
audio_file = "path/to/your/audio.mp3"
subtitle_file = "path/to/your/subtitle.srt"

# FFmpeg command to generate a complex FLV file
ffmpeg_command = [
    'ffmpeg',
    '-i', video_file_1,  # First video input
    '-i', video_file_2,  # Second video input
    '-i', audio_file,  # Audio input
    '-filter_complex', 
    "[0:v][1:v]hstack=inputs=2[top];"  # Combine two videos side by side
    "[top][2:a]amerge=inputs=2,volume=2[final];",  # Merge audio and adjust volume
    '-map', '[final]',  # Map the final video and audio stream
    '-vf', 'subtitles=' + subtitle_file,  # Add subtitles
    '-vcodec', 'flv',  # Specify the codec compatible with FLV
    '-acodec', 'libmp3lame',  # Specify the audio codec
    output_file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_command)

print(f"Complex FLV file saved to {output_file}")