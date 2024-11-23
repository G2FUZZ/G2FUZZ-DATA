import os
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import pydub.effects

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the audio signal
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz

# Generate a sine wave for the given parameters
t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_signal = np.sin(2 * np.pi * frequency * t)

# Convert the audio signal to 16-bit integers
audio_signal_int16 = np.int16(audio_signal * 32767)

# Save the audio signal to a WAV file
wav_file_path = './tmp/generated_audio.wav'
write(wav_file_path, sample_rate, audio_signal_int16)

# Convert the WAV file to MP3 with different bit rates
bit_rates = [128, 192, 256, 320]

# Generate a silent audio segment for watermarking purposes
watermark_duration_ms = 5000  # 5 seconds
silent_segment = AudioSegment.silent(duration=watermark_duration_ms)

# Generate a high-frequency sine wave to serve as the watermark
watermark_frequency = 16000  # Frequency of the watermark sine wave
watermark_volume = -20.0  # Volume of the watermark in dB
sampling_rate = 44100  # Sampling rate for the watermark audio
t_watermark = np.linspace(0, watermark_duration_ms / 1000.0, int(sampling_rate * (watermark_duration_ms / 1000.0)), False)
watermark_signal = np.sin(2 * np.pi * watermark_frequency * t_watermark)
watermark_signal_int16 = np.int16(watermark_signal * 32767)
watermark = AudioSegment(
    watermark_signal_int16.tobytes(),
    frame_rate=sampling_rate,
    sample_width=watermark_signal_int16.dtype.itemsize,
    channels=1
)
watermark = watermark + watermark_volume  # Adjust watermark volume

# Load the original audio
original_audio = AudioSegment.from_wav(wav_file_path)

# Overlay the watermark on the silent segment
watermarked_silent_segment = silent_segment.overlay(watermark)

# Concatenate the watermarked silent segment with the original audio
watermarked_audio = watermarked_silent_segment + original_audio

for bit_rate in bit_rates:
    mp3_file_path = f'./tmp/generated_audio_{bit_rate}kbps_watermarked.mp3'
    # Export the watermarked audio to an MP3 file with the specified bitrate
    watermarked_audio.export(mp3_file_path, format="mp3", bitrate=f"{bit_rate}k")

# Remove the temporary WAV file
os.remove(wav_file_path)