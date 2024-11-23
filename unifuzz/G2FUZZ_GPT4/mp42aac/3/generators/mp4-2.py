import numpy as np
import os
import wave

from moviepy.editor import AudioFileClip

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a 440 Hz sine wave (A4 note) for 5 seconds
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_wave = np.sin(2 * np.pi * frequency * t) * 0.5

# Convert the numpy array to a format suitable for audio files
audio_wave = (audio_wave * 32767).astype(np.int16)

# Save the audio wave to a WAV file
wav_file_path = os.path.join(output_dir, 'audio.wav')
with wave.open(wav_file_path, 'w') as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # Two bytes per sample, since we're using np.int16
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_wave.tobytes())

# Use the saved WAV file to create an AudioFileClip
audio_clip = AudioFileClip(wav_file_path)

# Save the audio clip as an MP4 file using MoviePy
audio_clip.write_audiofile(os.path.join(output_dir, 'audio.mp4'), codec='aac')