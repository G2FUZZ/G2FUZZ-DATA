import subprocess

# Set the input and output file paths
input_file = "./tmp/audio_aac.mp4"
output_file = "./tmp/audio_aac_multicam_live_streaming.mp4"

# Use ffmpeg to add the Fast Start, Aspect Ratio, Multi-camera Angles, and Live Streaming features to the mp4 file
subprocess.run(["ffmpeg", "-i", input_file, "-c", "copy", "-movflags", "faststart", "-aspect", "16:9", "-map", "0:v", "-map", "0:a", "-map", "0:v", "-map", "0:a", "-f", "mp4", "-movflags", "+frag_keyframe+empty_moov", output_file])