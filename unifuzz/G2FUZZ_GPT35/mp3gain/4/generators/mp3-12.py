import os
from pydub import AudioSegment

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample audio file with variable bit rate and preset mode
audio = AudioSegment.silent(duration=5000)  # 5 seconds of silent audio
audio.export('./tmp/sample_vbr_preset.mp3', format='mp3', bitrate='192k', codec='libmp3lame', parameters=['-preset', 'fast'])

print("Generated 'mp3' file with variable bit rate and preset mode successfully.")