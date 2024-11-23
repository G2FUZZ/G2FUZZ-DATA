import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/complex_mp3_files/', exist_ok=True)

# Generate a sample mp3 file with a variable bitrate and length
song = AudioSegment.silent(duration=10000)  # 10 seconds of silence
bitrates = [64, 128, 192]  # Variable bitrates
for bitrate in bitrates:
    song.export(f'./tmp/complex_mp3_files/sample_variable_bitrate_{bitrate}kbps.mp3', format="mp3", bitrate=f"{bitrate}k")

# Generate a sample mp3 file with metadata and custom audio
song = Sine(440).to_audio_segment(duration=5000)  # 5 seconds of 440 Hz sine wave
song.export('./tmp/complex_mp3_files/sample_metadata.mp3', format="mp3", tags={'artist': 'AI Music Generator', 'title': 'Sine Wave'})

print("Complex mp3 files generated successfully!")