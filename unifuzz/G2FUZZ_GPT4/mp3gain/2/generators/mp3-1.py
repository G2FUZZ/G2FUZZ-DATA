import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave as an example of audio
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return np.sin(2*np.pi*freq*t)

# Parameters for the audio
freq = 440  # Frequency of the sine wave (A4)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Generate a sine wave audio signal
audio = generate_sine_wave(freq, sample_rate, duration)

# Normalize to 16-bit range for WAV format
audio_normalized = np.int16((audio / audio.max()) * 32767)

# Use a temporary directory to first save as WAV (since direct MP3 generation might not be supported)
with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path = './tmp/generated_audio.mp3'
    
    # Write the audio data as a WAV file
    wavfile.write(wav_path, sample_rate, audio_normalized)
    
    # Convert WAV to MP3
    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3", bitrate="192k")

print(f"Generated MP3 saved to: {mp3_path}")