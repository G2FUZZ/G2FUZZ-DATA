import os
from pydub import AudioSegment

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample audio file with variable bit rate
sample_audio = AudioSegment.silent(duration=3000)  # 3 seconds of silence
sample_audio.export(os.path.join(output_dir, 'sample_vbr.mp3'), format='mp3', bitrate='192k')