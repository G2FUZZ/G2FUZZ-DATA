from moviepy.editor import AudioFileClip
import numpy as np
import os
from scipy.io.wavfile import write  # Import the write function from scipy.io.wavfile

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave (as an example audio)
def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * freq * t)
    return (waveform * (2**15 - 1)).astype(np.int16)

# Function to create an audio file with a specific codec and package it into an FLV file
def create_flv_audio(audio_data, sample_rate=44100, codec='mp3', filename='output.flv'):
    # Temporary audio file path (to be encoded into FLV)
    temp_audio_path = os.path.join(output_dir, 'temp_audio.wav')  # Change to WAV format
    
    # Save the audio data to a temporary WAV file
    write(temp_audio_path, sample_rate, audio_data)  # Save the waveform to a file
    
    # Use the temporary WAV file with AudioFileClip
    audio_clip = AudioFileClip(temp_audio_path)
    temp_mp3_path = os.path.join(output_dir, 'temp_audio.mp3')
    audio_clip.write_audiofile(temp_mp3_path, codec=codec)
    
    # Use ffmpeg to package the MP3 into an FLV container
    flv_output_path = os.path.join(output_dir, filename)
    os.system(f"ffmpeg -i {temp_mp3_path} -c:a copy {flv_output_path}")
    
    # Cleanup the temporary audio files
    os.remove(temp_audio_path)
    os.remove(temp_mp3_path)

# Generate a sine wave as example audio data
freq = 440  # Frequency in Hz (A4 note)
duration = 5  # Duration in seconds
sample_rate = 44100  # Sample rate in Hz
waveform = generate_sine_wave(freq, duration, sample_rate)

# Create an FLV file with the generated audio
create_flv_audio(waveform, sample_rate=sample_rate, codec='mp3', filename='example_audio.flv')