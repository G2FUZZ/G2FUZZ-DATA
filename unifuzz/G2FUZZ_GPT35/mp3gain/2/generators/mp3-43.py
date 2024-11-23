import os
import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define parameters for generating sine wave signals
parameters = [
    {"frequency": 440, "amplitude": 2**15 - 1, "duration": 5, "sampling_rate": 44100},
    {"frequency": 880, "amplitude": 2**14 - 1, "duration": 10, "sampling_rate": 48000},
    {"frequency": 220, "amplitude": 2**16 - 1, "duration": 3, "sampling_rate": 96000}
]

for idx, param in enumerate(parameters):
    frequency = param["frequency"]
    amplitude = param["amplitude"]
    duration = param["duration"]
    sampling_rate = param["sampling_rate"]
    
    t = np.linspace(0, duration, int(duration*sampling_rate), endpoint=False)
    
    # Generate a sine wave signal
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Save as WAV file
    wav_filename = f'{output_dir}sine_wave_{idx}.wav'
    wavfile.write(wav_filename, sampling_rate, sine_wave.astype(np.int16))
    
    # Convert WAV to MP3 with custom bitrate and codec options
    audio = AudioSegment.from_wav(wav_filename)
    mp3_filename = f'{output_dir}sine_wave_{idx}.mp3'
    audio.export(mp3_filename, format="mp3", bitrate="192k", codec="libmp3lame")

print("MP3 files with different parameters generated successfully.")