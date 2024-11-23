from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a silent audio segment (10 seconds long)
silent_audio = AudioSegment.silent(duration=10000)  # duration in milliseconds

# Export the silent audio as an MP3 file
output_path = os.path.join(output_dir, "silent.mp3")
silent_audio.export(output_path, format="mp3")

# Generate a redundant copy of the MP3 file to illustrate the Redundancy feature
redundant_output_path = os.path.join(output_dir, "silent_redundant.mp3")
silent_audio.export(redundant_output_path, format="mp3")

print(f"MP3 file has been saved to {output_path}")
print(f"Redundant MP3 file has been saved to {redundant_output_path}")