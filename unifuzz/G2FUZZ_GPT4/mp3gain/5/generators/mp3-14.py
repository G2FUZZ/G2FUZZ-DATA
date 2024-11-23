import numpy as np
from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequency=440, duration_seconds=1, sample_rate=44100):
    """
    Generate a tone at the specified frequency, duration, and sample rate.

    :param frequency: Frequency of the tone in Hz
    :param duration_seconds: Duration of the tone in seconds
    :param sample_rate: Sample rate in Hz
    :return: Numpy array containing the generated tone
    """
    t = np.linspace(0, duration_seconds, int(duration_seconds * sample_rate), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    # Normalize to the range of int16
    tone = (tone * 32767).astype(np.int16)
    return tone

def save_to_mp3(audio_data, filename, sample_rate=44100, bitrate="192k", quality=2):
    """
    Save audio data to an MP3 file with adjustable complexity settings.

    :param audio_data: Numpy array containing audio data to save
    :param filename: Filename for the MP3 file
    :param sample_rate: Sample rate in Hz
    :param bitrate: Bitrate of the MP3 file (e.g., '192k', '256k')
    :param quality: Quality setting for the LAME encoder, ranges from 0 (best) to 9 (worst)
    """
    # Convert numpy array to bytes
    audio_bytes = audio_data.tobytes()
    # Create an AudioSegment from the raw audio data
    audio_segment = AudioSegment(audio_bytes, sample_width=2, frame_rate=sample_rate, channels=1)
    # Export the audio segment to an MP3 file with specified bitrate and quality
    audio_segment.export(filename, format="mp3", bitrate=bitrate, parameters=["-q:a", str(quality)])

# Sampling rates and settings for MP3 files generation
sampling_rates = [44100, 48000]
bitrates = ["192k", "256k"]
qualities = [2, 5]  # Lower is better quality but higher complexity

for sample_rate in sampling_rates:
    for bitrate in bitrates:
        for quality in qualities:
            # Generate a 440 Hz tone for 1 second
            tone = generate_tone(sample_rate=sample_rate)
            # Save the tone to an MP3 file with the specified bitrate and quality settings
            filename = f'./tmp/tone_{sample_rate/1000}kHz_{bitrate}_quality{quality}.mp3'
            save_to_mp3(tone, filename, sample_rate=sample_rate, bitrate=bitrate, quality=quality)
            print(f'Generated MP3 file with {sample_rate/1000} kHz sampling rate, '
                  f'{bitrate} bitrate, quality level {quality} at {filename}')