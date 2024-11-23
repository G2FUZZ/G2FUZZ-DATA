import numpy as np
from scipy.io.wavfile import write
import os
import subprocess

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

def generate_chord_tones(frequencies, duration=5, sample_rate=44100):
    """
    Generate a chord from a list of frequencies, with a given duration and sample rate.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    chord = np.zeros(int(sample_rate * duration))
    for frequency in frequencies:
        tone = np.sin(frequency * 2 * np.pi * t)
        chord += tone
    # Normalize chord
    max_val = np.max(np.abs(chord))
    if max_val > 0:
        chord = chord / max_val
    # Convert to stereo by duplicating the mono track
    chord = np.int16(chord * 32767)
    stereo_chord = np.column_stack((chord, chord))
    return stereo_chord

def save_to_wav(data, sample_rate, file_name):
    """
    Save audio data to a WAV file with a given sample rate.
    """
    write(file_name, sample_rate, data)

def convert_wav_to_mp3(input_file, output_file, sample_rate, bit_rate='192k'):
    """
    Convert a WAV file to an MP3 file using ffmpeg, with a specified bit rate.
    """
    subprocess.run(['ffmpeg', '-i', input_file, '-vn', '-ar', str(sample_rate), '-ac', '2', '-b:a', bit_rate, output_file], check=True)

# Define the sampling rates and bit rates for the MP3 files
sampling_bit_rates = [
    (44100, '192k'),
    (48000, '256k')
]

# Chords to generate (in Hz)
chords = [
    [440, 554.37, 659.25],  # A major
    [523.25, 659.25, 783.99]  # C major
]

for sample_rate, bit_rate in sampling_bit_rates:
    for i, chord in enumerate(chords, start=1):
        # Generate a chord
        stereo_chord = generate_chord_tones(chord, sample_rate=sample_rate)
        
        # Temporary WAV file name
        wav_file = os.path.join(output_dir, f"chord_{i}_{sample_rate}.wav")
        # MP3 file name
        mp3_file = os.path.join(output_dir, f"chord_{i}_{sample_rate}_{bit_rate}.mp3")
        
        # Save the chord as a WAV file
        save_to_wav(stereo_chord, sample_rate, wav_file)
        
        # Convert the WAV file to an MP3 file
        convert_wav_to_mp3(wav_file, mp3_file, sample_rate, bit_rate)
        
        # Optionally, remove the temporary WAV file
        os.remove(wav_file)

print("MP3 files with complex features have been generated.")