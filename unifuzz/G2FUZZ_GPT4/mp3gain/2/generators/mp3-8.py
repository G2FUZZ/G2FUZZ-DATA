from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1 second sine wave tone at 440 Hz (A4)
tone = Sine(440).to_audio_segment(duration=1000)

# Set frame rate and other parameters
frame_rate = 44100  # Common frame rate for MP3
tone = tone.set_frame_rate(frame_rate)
tone = tone.set_channels(1)  # Mono audio

# Export the generated tone as an MP3 file
file_path = './tmp/generated_tone.mp3'
tone.export(file_path, format="mp3", bitrate="128k")

print(f"MP3 file has been generated and saved to {file_path}")