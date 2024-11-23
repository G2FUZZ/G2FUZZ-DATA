import numpy as np
from scipy.io.wavfile import write
import os
import subprocess

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

def generate_tone(frequency=440, duration=5, sample_rate=44100):
    """
    Generate a tone of a given frequency, duration, and sample rate.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    # Normalize to 16-bit range
    tone = np.int16(tone * 32767)
    return tone

def save_to_wav(data, sample_rate, file_name):
    """
    Save audio data to a WAV file with a given sample rate.
    """
    write(file_name, sample_rate, data)

def convert_wav_to_mp3(input_file, output_file):
    """
    Convert a WAV file to an MP3 file using ffmpeg.
    """
    subprocess.run(['ffmpeg', '-i', input_file, '-vn', '-ar', str(sample_rate), '-ac', '2', '-b:a', '192k', output_file], check=True)

# Define the sampling rates for the MP3 files
sampling_rates = [44100, 48000]

for sample_rate in sampling_rates:
    # Generate a tone
    tone = generate_tone(sample_rate=sample_rate)
    
    # Temporary WAV file name
    wav_file = os.path.join(output_dir, f"tone_{sample_rate}.wav")
    # MP3 file name
    mp3_file = os.path.join(output_dir, f"tone_{sample_rate}.mp3")
    
    # Save the tone as a WAV file
    save_to_wav(tone, sample_rate, wav_file)
    
    # Convert the WAV file to an MP3 file
    convert_wav_to_mp3(wav_file, mp3_file)
    
    # Optionally, remove the temporary WAV file
    os.remove(wav_file)

print("MP3 files have been generated.")