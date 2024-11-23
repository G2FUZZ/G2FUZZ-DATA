import subprocess

# Set the input and output file paths
input_file = "./tmp/audio_aac.mp4"
output_file = "./tmp/audio_aac_faststart.mp4"

# Use ffmpeg to add the Fast Start feature to the mp4 file
subprocess.run(["ffmpeg", "-i", input_file, "-c", "copy", "-movflags", "faststart", output_file])