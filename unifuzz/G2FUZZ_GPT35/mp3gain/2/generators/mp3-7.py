import os
import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Sampling Frequency in Hz
sampling_frequencies = [44100, 48000, 96000]

for idx, freq in enumerate(sampling_frequencies):
    duration = 5  # 5 seconds
    sample_rate = freq
    t = np.linspace(0, duration, int(duration*sample_rate), endpoint=False)
    
    # Generate a sine wave signal
    amplitude = 2**15 - 1
    frequency = 440  # Hz
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Save as WAV file
    wav_filename = f'{output_dir}sine_wave_{idx}.wav'
    wavfile.write(wav_filename, sample_rate, sine_wave.astype(np.int16))
    
    # Convert WAV to MP3
    audio = AudioSegment.from_wav(wav_filename)
    mp3_filename = f'{output_dir}sine_wave_{idx}.mp3'
    audio.export(mp3_filename, format="mp3")

print("MP3 files with different sampling frequencies generated successfully.")