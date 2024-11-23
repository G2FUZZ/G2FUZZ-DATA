from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a silent audio segment (10 seconds long)
silent_audio = AudioSegment.silent(duration=10000)  # duration in milliseconds

# Looping the silent audio segment to create a longer segment
# Let's say we want to loop it 5 times to create a 50-second long audio
looped_audio = silent_audio * 5

# Export the looped audio as an MP3 file
output_path = os.path.join(output_dir, "looped_silent.mp3")
looped_audio.export(output_path, format="mp3")

print(f"MP3 file with looping capability has been saved to {output_path}")