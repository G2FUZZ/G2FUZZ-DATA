import numpy as np
from pydub import AudioSegment
import os
import random

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

def introduce_errors(samples, error_rate=0.001):
    """
    Introduce random errors into the audio samples to simulate error resilience.

    :param samples: Numpy array containing audio samples.
    :param error_rate: Probability of an error in a given sample.
    :return: Numpy array containing audio samples with errors.
    """
    num_samples = len(samples)
    num_errors = int(num_samples * error_rate)
    
    for _ in range(num_errors):
        error_position = random.randint(0, num_samples - 1)
        samples[error_position] = random.randint(-32768, 32767)
    
    return samples

def watermark_audio(samples, sample_rate, watermark_text):
    """
    Embed a watermark into the audio samples.

    :param samples: Numpy array containing audio samples.
    :param sample_rate: Sampling rate in samples per second.
    :param watermark_text: Text to be embedded as a watermark.
    :return: Numpy array containing audio samples with embedded watermark.
    """
    # Simple watermark embedding by modifying specific samples based on the watermark text
    # This is a simplistic approach for demonstration purposes only
    watermark_bytes = watermark_text.encode('utf-8')
    watermark_bits = ''.join(f'{byte:08b}' for byte in watermark_bytes)
    
    for i, bit in enumerate(watermark_bits[:len(samples) // 1000]):
        if bit == '1':
            samples[i * 1000] = min(max(samples[i * 1000] + 100, -32768), 32767)
    
    return samples

def save_to_mp3(filename, samples, sample_rate):
    """
    Save the given audio samples as an MP3 file.

    :param filename: Path to the MP3 file to be saved.
    :param samples: Numpy array containing audio samples.
    :param sample_rate: Sampling rate in samples per second.
    """
    audio = AudioSegment(samples.tobytes(), frame_rate=sample_rate, sample_width=samples.dtype.itemsize, channels=1)
    audio.export(filename, format="mp3", bitrate="192k")

# Define the properties of the tone to be generated
frequency = 440  # A4 note, in Hz
duration = 2  # seconds

# Sampling rates to be used for the MP3 files
sampling_rates = [44100, 48000]

# Watermark text
watermark_text = "Copyright 2023 MyCompany"

# Generate and save tones with different sampling rates
for sample_rate in sampling_rates:
    samples = generate_tone(frequency, duration, sample_rate)
    # Introduce errors to simulate Error Resilience
    samples_with_errors = introduce_errors(samples)
    # Embed watermark
    samples_with_watermark = watermark_audio(samples_with_errors, sample_rate, watermark_text)
    filename = f'./tmp/tone_{sample_rate // 1000}kHz_error_resilient_watermarked.mp3'
    save_to_mp3(filename, samples_with_watermark, sample_rate)

print("MP3 files with Error Resilience and Watermarking have been generated and saved.")