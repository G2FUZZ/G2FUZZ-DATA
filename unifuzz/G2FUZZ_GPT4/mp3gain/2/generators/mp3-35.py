import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return np.sin(2*np.pi*freq*t)

# Parameters for the audio
base_freq = 440  # Frequency of the base sine wave (A4)
overlay_freq = 554.37  # Frequency of the overlay sine wave (C#5/D♭5)
sequential_freq = 659.25  # Frequency of the sequential sine wave (E5)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds for each part

# Generate audio signals
base_audio = generate_sine_wave(base_freq, sample_rate, duration)
overlay_audio = generate_sine_wave(overlay_freq, sample_rate, duration)
sequential_audio = generate_sine_wave(sequential_freq, sample_rate, duration)

# Normalize to 16-bit range for WAV format
base_audio_normalized = np.int16((base_audio / base_audio.max()) * 32767)
overlay_audio_normalized = np.int16((overlay_audio / overlay_audio.max()) * 32767)
sequential_audio_normalized = np.int16((sequential_audio / sequential_audio.max()) * 32767)

# Use a temporary directory to first save as WAV (since direct MP3 generation might not be supported)
with TemporaryDirectory() as tmpdirname:
    base_wav_path = os.path.join(tmpdirname, 'base_temp.wav')
    overlay_wav_path = os.path.join(tmpdirname, 'overlay_temp.wav')
    sequential_wav_path = os.path.join(tmpdirname, 'sequential_temp.wav')
    complex_mp3_path = './tmp/complex_structure_audio.mp3'
    
    # Write the audio data as WAV files
    wavfile.write(base_wav_path, sample_rate, base_audio_normalized)
    wavfile.write(overlay_wav_path, sample_rate, overlay_audio_normalized)
    wavfile.write(sequential_wav_path, sample_rate, sequential_audio_normalized)
    
    # Load WAV into pydub AudioSegments
    base_sound = AudioSegment.from_wav(base_wav_path)
    overlay_sound = AudioSegment.from_wav(overlay_wav_path)
    sequential_sound = AudioSegment.from_wav(sequential_wav_path)
    
    # Mix overlay_sound with base_sound starting from the beginning
    combined_sounds = base_sound.overlay(overlay_sound)
    
    # Append sequential_sound after the combined sounds
    final_composition = combined_sounds + sequential_sound
    
    # Export the complex structure to an MP3 file
    final_composition.export(complex_mp3_path, format="mp3")

print(f"Generated MP3 with a complex structure saved to: {complex_mp3_path}")