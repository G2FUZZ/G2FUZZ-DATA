import subprocess
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path for the generated video
output_file = os.path.join(output_dir, "complex_generated_video.flv")

# Path to an audio file to add as background music
# Ensure this path points to a valid audio file on your system
background_audio = "/path/to/background.mp3"

# Command to generate a video file using FFmpeg
# This command now includes complex features like text overlay, background audio, and a fade-in effect
ffmpeg_command = [
    'ffmpeg',
    '-f', 'lavfi',  # Use the Libavfilter input virtual device
    '-i', 'color=c=blue:size=640x480:d=10',  # Generate 10 seconds of blue video
    '-f', 'lavfi',
    '-i', 'anullsrc',  # Generate silent audio as placeholder
    '-i', background_audio,  # The background audio file
    '-filter_complex', '[0:v]drawtext=text=\'Sample Text\':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2,'
                        'fade=t=in:st=0:d=2[v];'  # Applying a fade-in video effect for 2 seconds at the start
                        '[1:a][2:a]amerge=inputs=2,'
                        'afade=t=in:st=0:d=5[a]',  # Applying a fade-in audio effect for 5 seconds at the start
    '-map', '[v]',  # Map the video output from filter_complex to the output file
    '-map', '[a]',  # Map the audio output from filter_complex to the output file
    '-ac', '2',  # Set the audio output to stereo
    '-vcodec', 'flv',  # Attempt to use an FLV-compatible codec
    '-shortest',  # Finish encoding when the shortest input stream ends
    output_file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_command)

print(f"Complex FLV file saved to {output_file}")