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

# Introduce a function to simulate transmission errors in the audio signal
def simulate_transmission_errors(audio_signal, sample_rate, error_rate=0.001):
    """
    Simulates transmission errors in the audio signal by randomly zeroing out
    small chunks of the audio signal, representing lost or corrupted frames.
    
    :param audio_signal: The input audio signal.
    :param sample_rate: The sample rate of the audio signal.
    :param error_rate: The probability of any given frame to be corrupted.
    :return: Audio signal with simulated transmission errors.
    """
    frame_length = int(sample_rate * 0.026)  # Calculate frame length for 26 ms
    num_frames = len(audio_signal) // frame_length
    
    for frame_idx in range(num_frames):
        if np.random.rand() < error_rate:  # Randomly decide if a frame is corrupted
            start = frame_idx * frame_length
            end = start + frame_length
            audio_signal[start:end] = 0  # Zero out the frame to simulate corruption
    
    return audio_signal

# Parameters for the audio
freq = 440  # Frequency of the sine wave (A4)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
error_rate = 0.002  # Probability of frame corruption

# Generate a sine wave audio signal
audio = generate_sine_wave(freq, sample_rate, duration)

# Simulate transmission errors in the audio signal
audio_with_errors = simulate_transmission_errors(audio.copy(), sample_rate, error_rate)

# Normalize to 16-bit range for WAV format
audio_normalized = np.int16((audio_with_errors / audio_with_errors.max()) * 32767)

# Use a temporary directory to first save as WAV (since direct MP3 generation might not be supported)
with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path = './tmp/generated_audio_with_errors.mp3'
    
    # Write the audio data as a WAV file
    wavfile.write(wav_path, sample_rate, audio_normalized)
    
    # Convert WAV to MP3
    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3", bitrate="192k")

print(f"Generated MP3 saved to: {mp3_path}")