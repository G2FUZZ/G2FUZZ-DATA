import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a sine wave audio segment
sine_wave = Sine(440).to_audio_segment(duration=1000)  # 440 Hz frequency, 1 second duration

# Set the bitrate for constant bit rate (CBR)
bitrate = '128k'

# Save the sine wave audio segment as an mp3 file with constant bit rate
output_path = './tmp/sine_wave_cbr.mp3'
sine_wave.export(output_path, format='mp3', bitrate=bitrate)

# Check if the file was saved successfully
if os.path.exists(output_path):
    print(f'MP3 file with constant bit rate saved successfully at: {output_path}')
else:
    print('Failed to save MP3 file with constant bit rate.')