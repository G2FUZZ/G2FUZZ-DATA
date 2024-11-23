import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequency, duration, sample_rate):
    """
    Generate a tone using a sine wave.

    :param frequency: Frequency of the sine wave in Hz.
    :param duration: Duration of the tone in seconds.
    :param sample_rate: Sampling rate in samples per second.
    :return: Numpy array containing the generated samples.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    # Normalize to 16-bit range
    tone = np.int16(tone * 32767)
    return tone

def apply_equalization(audio_segment, bands):
    """
    Apply equalization to the audio segment.

    :param audio_segment: An AudioSegment instance to apply EQ.
    :param bands: A list of (frequency, gain) tuples.
    :return: An equalized AudioSegment instance.
    """
    # Apply equalization
    equalized_audio = audio_segment
    for band in bands:
        frequency, gain = band
        equalized_audio = equalized_audio.apply_gain_stereo(frequency, gain)
    return equalized_audio

def save_to_mp3(filename, samples, sample_rate, eq_bands=None):
    """
    Save the given audio samples as an MP3 file with optional equalization.

    :param filename: Path to the MP3 file to be saved.
    :param samples: Numpy array containing audio samples.
    :param sample_rate: Sampling rate in samples per second.
    :param eq_bands: Optional list of tuples for EQ settings (frequency, gain).
    """
    audio = AudioSegment(samples.tobytes(), frame_rate=sample_rate, sample_width=samples.dtype.itemsize, channels=1)
    if eq_bands:
        audio = apply_equalization(audio, eq_bands)
    audio = normalize(audio)
    audio.export(filename, format="mp3", bitrate="192k")

# Define the properties of the tone to be generated
frequency = 440  # A4 note, in Hz
duration = 2  # seconds

# Sampling rates to be used for the MP3 files
sampling_rates = [44100, 48000]

# Equalization settings: A list of (frequency, gain) to adjust the balance of frequency components
eq_settings = [(500, -3), (1000, 2), (5000, 5)]

# Generate and save tones with different sampling rates and equalization
for sample_rate in sampling_rates:
    samples = generate_tone(frequency, duration, sample_rate)
    filename = f'./tmp/tone_{sample_rate // 1000}kHz_EQ.mp3'
    save_to_mp3(filename, samples, sample_rate, eq_bands=eq_settings)

print("MP3 files with EQ have been generated and saved.")