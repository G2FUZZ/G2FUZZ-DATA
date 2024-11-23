import subprocess

# Set the input and output file paths
input_file = "./tmp/audio_aac.mp4"
output_file = "./tmp/audio_aac_encrypted.mp4"

# Use ffmpeg to add the Fast Start and Encryption features to the mp4 file
subprocess.run(["ffmpeg", "-i", input_file, "-c", "copy", "-movflags", "faststart+faststart", "-encryption_scheme", "cenc-aes-ctr", "-encryption_key", "0123456789ABCDEF0123456789ABCDEF", output_file])