import numpy as np
from scipy.io.wavfile import write
import os
import subprocess
from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB, APIC, TYER, ID3NoHeaderError

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)  # This ensures the ./tmp/ directory is created

def generate_tone(frequency=440, duration=5, sample_rate=44100):
    """
    Generate a tone of a given frequency, duration, and sample rate.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    tone = np.int16(tone * 32767)  # Normalize to 16-bit range
    return tone

def save_to_wav(data, sample_rate, file_name):
    """
    Save audio data to a WAV file with a given sample rate.
    """
    write(file_name, sample_rate, data)  # Saves the WAV file

def convert_wav_to_mp3(input_file, output_file, sample_rate):
    """
    Convert a WAV file to an MP3 file using ffmpeg.
    """
    subprocess.run(['ffmpeg', '-i', input_file, '-vn', '-ar', str(sample_rate), '-ac', '2', '-b:a', '192k', output_file], check=True)  # Converts and saves the MP3 file

def add_id3_tags(file_name, file_title, album_name, track_number, year, artist_name, cover_art_path=None):
    """
    Add ID3 tags to an MP3 file.
    """
    try:
        audio = ID3(file_name)
    except ID3NoHeaderError:
        audio = ID3()
    
    # Adding various ID3 tags
    audio.add(TIT2(encoding=3, text=file_title))
    audio.add(TPE1(encoding=3, text=artist_name))
    audio.add(TRCK(encoding=3, text=str(track_number)))
    audio.add(TALB(encoding=3, text=album_name))
    audio.add(TYER(encoding=3, text=str(year)))
    if cover_art_path:
        with open(cover_art_path, 'rb') as img:
            audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img.read()))
    audio.save(file_name)  # Saves the MP3 file with ID3 tags

# Define the sampling rates for the MP3 files
sampling_rates = [44100, 48000]

for sample_rate in sampling_rates:
    tone = generate_tone(sample_rate=sample_rate)  # Generate a tone
    
    wav_file = os.path.join(output_dir, f"tone_{sample_rate}.wav")  # Temporary WAV file name
    mp3_file = os.path.join(output_dir, f"tone_{sample_rate}.mp3")  # MP3 file name
    
    save_to_wav(tone, sample_rate, wav_file)  # Save the tone as a WAV file
    convert_wav_to_mp3(wav_file, mp3_file, sample_rate)  # Convert the WAV file to an MP3 file
    add_id3_tags(mp3_file, "Test Tone", "Test Album", 1, "2023", "Test Artist", None)  # Add ID3 tags to the MP3 file
    
    os.remove(wav_file)  # Optionally, remove the temporary WAV file

print("MP3 files have been generated with ID3 tags.")