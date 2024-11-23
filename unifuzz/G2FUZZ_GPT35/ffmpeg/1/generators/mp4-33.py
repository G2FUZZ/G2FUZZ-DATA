import subprocess

# Set the input and output file paths
input_file = "./tmp/audio_aac.mp4"
output_file = "./tmp/audio_aac_multicam.mp4"

# Use ffmpeg to add the Fast Start, Aspect Ratio, and Multi-camera Angles features to the mp4 file
subprocess.run(["ffmpeg", "-i", input_file, "-c", "copy", "-movflags", "faststart", "-aspect", "16:9", "-map", "0:v", "-map", "0:a", "-map", "0:v", "-map", "0:a", output_file])