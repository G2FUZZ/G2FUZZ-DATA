import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave audio segment
frequency = 440  # A4 note, in Hertz
duration_in_ms = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

audio_segment = Sine(frequency).to_audio_segment(duration=duration_in_ms, volume=volume)

# Export the generated audio with a constant bitrate and MPEG-2.5 Extension
file_path = './tmp/generated_audio_mpeg2_5.mp3'
# Specify the parameters for MPEG-2.5 Extension
# Note: The MPEG-2.5 is not an official standard, and its support may vary.
# Here we'll try to simulate its effect by manually setting a low sample rate (8 kHz),
# which is one of the features MPEG-2.5 allows for. 
# However, be aware that not all players or libraries may support playing these files correctly.
audio_segment.set_frame_rate(8000).export(file_path, format="mp3", bitrate="192k", parameters=["-ar", "8000"])

print(f"Generated mp3 file with MPEG-2.5 Extension at {file_path}")