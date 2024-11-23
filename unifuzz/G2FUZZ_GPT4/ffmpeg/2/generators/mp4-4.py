import numpy as np
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips
import os
from scipy.io.wavfile import write

# Directory to save the generated MP4 file
output_dir = "./tmp/"
output_filename = "aac_audio_example.mp4"

# Generate synthetic audio (1kHz sine wave) for 10 seconds
sample_rate = 44100  # Samples per second
frequency = 1000  # Frequency of the sine wave
duration = 10  # Duration in seconds
t = np.linspace(0, duration, int(sample_rate * duration))
audio = np.sin(2 * np.pi * frequency * t)

# Save the synthetic audio into a temporary WAV file (as an intermediate step)
temp_audio_filename = "temp_audio.wav"
write(temp_audio_filename, sample_rate, audio.astype(np.float32))

# Create an audio clip from the temporary audio file
audio_clip = AudioFileClip(temp_audio_filename)

# Generate a silent video clip of the same duration as the audio
video_clip = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio_clip.duration)

# Set the audio of the video clip to the generated AAC audio
video_clip = video_clip.set_audio(audio_clip)

# Concatenate the video clip to itself to demonstrate video editing (optional)
final_clip = concatenate_videoclips([video_clip])

# Set the fps for the final clip
final_clip.fps = 24  # Setting fps to 24, but you can choose another value as needed

# Write the result to a file, specifying fps in the arguments (optional if fps is already set for the clip)
final_clip.write_videofile(f"{output_dir}{output_filename}", codec="libx264", audio_codec="aac", fps=24)

# Clean up the temporary audio file
os.remove(temp_audio_filename)