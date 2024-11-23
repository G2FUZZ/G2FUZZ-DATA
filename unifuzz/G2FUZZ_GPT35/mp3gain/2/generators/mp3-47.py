import os
from pydub import AudioSegment
from pydub.generators import Sine, Square

# Create multiple audio segments (sine wave and square wave)
sine_wave = Sine(440).to_audio_segment(duration=1000)  # 440 Hz frequency, 1 second duration
square_wave = Square(880).to_audio_segment(duration=1500)  # 880 Hz frequency, 1.5 second duration

# Concatenate the audio segments
complex_audio = sine_wave + square_wave

# Set the bitrate for constant bit rate (CBR)
bitrate = '192k'

# Save the complex audio segment as an mp3 file with constant bit rate
output_path = './tmp/complex_audio_cbr.mp3'
complex_audio.export(output_path, format='mp3', bitrate=bitrate)

# Check if the file was saved successfully
if os.path.exists(output_path):
    print(f'MP3 file with complex audio structures saved successfully at: {output_path}')
else:
    print('Failed to save MP3 file with complex audio structures.')