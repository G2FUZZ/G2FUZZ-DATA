import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the audio file
sample_rate = 44100  # Sample rate in Hz
duration = 10  # Duration in seconds
frequency_left = 440  # Frequency of the sine wave for the left channel in Hz
frequency_right = 554  # Frequency of the sine wave for the right channel in Hz
fade_in_ms = 500  # Duration of fade in in milliseconds
fade_out_ms = 500  # Duration of fade out in milliseconds

# Generate the sine wave for both channels
t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
audio_left = np.sin(2 * np.pi * frequency_left * t) * 0.3  # Generate sine wave for the left channel
audio_right = np.sin(2 * np.pi * frequency_right * t) * 0.3  # Generate sine wave for the right channel

# Convert to 16-bit signed integers
audio_left = np.int16(audio_left * 32767)
audio_right = np.int16(audio_right * 32767)

# Interleave audio_left and audio_right to create a stereo effect
audio_stereo = np.vstack((audio_left, audio_right)).T

# Save the stereo sine wave as a WAV file first
wav_path = './tmp/example_stereo.wav'
write(wav_path, sample_rate, audio_stereo)

# Convert the WAV file to MP3 with fades
audio_segment = AudioSegment.from_wav(wav_path)
audio_segment_with_fades = audio_segment.fade_in(fade_in_ms).fade_out(fade_out_ms)
mp3_path = './tmp/example_stereo_fade.mp3'
audio_segment_with_fades.export(mp3_path, format="mp3")

# Clean up the WAV file as it's no longer needed
os.remove(wav_path)

print(f"MP3 file saved to {mp3_path}")