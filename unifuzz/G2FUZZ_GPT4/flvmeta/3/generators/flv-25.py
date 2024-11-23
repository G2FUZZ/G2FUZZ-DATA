from moviepy.editor import AudioFileClip
import numpy as np
import os
from scipy.io.wavfile import write

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave
def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * freq * t)
    return (waveform * (2**15 - 1)).astype(np.int16)

# Function to create an audio file with a specific codec and package it into an FLV file with Audio Sample Rate Support
def create_flv_audio(audio_data, sample_rate=44100, codec='mp3', filename='output.flv'):
    # Temporary audio file path
    temp_audio_path = os.path.join(output_dir, 'temp_audio.wav')
    
    # Save the audio data to a temporary WAV file
    write(temp_audio_path, sample_rate, audio_data)
    
    # Use the temporary WAV file with AudioFileClip
    audio_clip = AudioFileClip(temp_audio_path)
    temp_mp3_path = os.path.join(output_dir, 'temp_audio.mp3')
    audio_clip.write_audiofile(temp_mp3_path, codec=codec, fps=sample_rate)
    
    # Use ffmpeg to package the MP3 into an FLV container, ensuring the sample rate is supported
    flv_output_path = os.path.join(output_dir, filename)  # Corrected variable name
    os.system(f"ffmpeg -i {temp_mp3_path} -ar {sample_rate} -c:a copy {flv_output_path}")
    
    # Cleanup the temporary audio files
    os.remove(temp_audio_path)
    os.remove(temp_mp3_path)

# Example usage with different audio sample rates
freq = 440  # Frequency in Hz (A4 note)
duration = 5  # Duration in seconds

# Generate example audio data at different sample rates
sample_rates = [11025, 22050, 44100]  # Example sample rates

for rate in sample_rates:
    waveform = generate_sine_wave(freq, duration, sample_rate=rate)
    filename = f'example_audio_{rate}.flv'
    create_flv_audio(waveform, sample_rate=rate, codec='mp3', filename=filename)