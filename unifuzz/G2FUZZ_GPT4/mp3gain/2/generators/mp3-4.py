import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the output directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a sine wave tone as an example audio source
duration_in_milliseconds = 5000  # 5 seconds
frequency_hz = 440  # A4 note, commonly used as a tuning standard (440 Hz)
volume = -20.0  # dB

audio = Sine(frequency_hz).to_audio_segment(duration=duration_in_milliseconds, volume=volume)

# Export the audio to an MP3 file with Variable Bit Rate (VBR)
vbr_quality = "0"  # V0 is typically the highest quality VBR setting in LAME encoder terms, equivalent to "-V 0"
output_path = os.path.join(output_dir, "vbr_example.mp3")
audio.export(output_path, format="mp3", parameters=["-q:a", vbr_quality])

print(f"Generated MP3 file with VBR at {output_path}")