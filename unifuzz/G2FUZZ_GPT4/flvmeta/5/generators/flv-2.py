import os
import numpy as np
from moviepy.audio.AudioClip import AudioArrayClip  # Corrected import statement
from moviepy.audio.fx.all import audio_normalize

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave for audio
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
t = np.linspace(0, duration, int(sample_rate * duration))
audio = np.sin(2 * np.pi * frequency * t)

# Convert the audio array to an audio clip
# Ensure the audio array is in the correct shape (2D with 2 columns for stereo or 1 column for mono)
audio_clip = AudioArrayClip(audio.reshape(-1, 1), fps=sample_rate)  # Assuming mono audio

# Normalize audio to prevent clipping
normalized_audio = audio_normalize(audio_clip)

# Export the audio clip as an FLV file with AAC audio
normalized_audio.write_audiofile(os.path.join(output_dir, "generated_audio.flv"), codec='aac')