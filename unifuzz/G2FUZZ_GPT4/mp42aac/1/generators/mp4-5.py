import numpy as np
from moviepy.editor import AudioFileClip
import os
from scipy.io.wavfile import write  # Import the correct function to save WAV files

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the audio signal
duration = 10  # seconds
frequency = 440  # Hz, A4 note
sampling_rate = 44100  # Hz
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
audio_signal = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave

# Save the raw audio to a temporary WAV file (MoviePy requires a file)
wav_filename = os.path.join(output_dir, 'temp_audio.wav')
# Correctly save the audio signal as a WAV file
write(wav_filename, sampling_rate, (audio_signal * 32767).astype(np.int16))

# Create an MP4 file with AAC audio
mp4_filename = os.path.join(output_dir, 'generated_audio.mp4')
audio_clip = AudioFileClip(wav_filename)
audio_clip.write_audiofile(mp4_filename, codec='aac')

# Clean up the temporary WAV file
os.remove(wav_filename)