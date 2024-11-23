import numpy as np
import os
import wave
from moviepy.editor import AudioFileClip, ColorClip

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave as an example audio signal
duration = 10  # duration of the audio clip in seconds
sample_rate = 44100  # sample rate in Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # time variable
frequency = 440  # sine frequency in Hz
audio = np.sin(2 * np.pi * frequency * t)  # generate sine wave

# Convert the numpy array to a suitable format
audio = (audio * 32767).astype(np.int16)  # convert to 16-bit PCM

# Save the audio as a temporary WAV file (will be used to create the MP4)
temp_audio_file = os.path.join(output_dir, "temp_audio.wav")
with wave.open(temp_audio_file, 'w') as wav_file:
    wav_file.setnchannels(1)  # mono audio
    wav_file.setsampwidth(2)  # 16 bits per sample
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio)

# Create a video clip with a blank frame and attach the audio
audio_clip = AudioFileClip(temp_audio_file)
video_clip = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio_clip.duration)
video_clip = video_clip.set_audio(audio_clip)

# Create an MP4 file containing the AAC encoded audio
mp4_output = os.path.join(output_dir, "output.mp4")
video_clip.write_videofile(mp4_output, codec="libx264", audio_codec="aac", fps=24)

# Clean up the temporary WAV file and video clip
os.remove(temp_audio_file)
video_clip.close()
audio_clip.close()