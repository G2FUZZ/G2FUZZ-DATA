import numpy as np
from scipy.io.wavfile import write
import moviepy.editor as mpe
import os
import subprocess  # For executing an external command

# Parameters for the audio
duration_seconds = 5  # Duration of the audio in seconds
frequency = 440  # Sine wave frequency, A4 note
sample_rate = 44100  # Sample rate in Hz

# Generate a sine wave for the audio
t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
audio_wave = np.sin(frequency * 2 * np.pi * t)

# Ensure the values are in 16-bit format and create a stereo file
audio_wave_16bit = np.int16(audio_wave * 32767)
stereo_audio_wave = np.vstack((audio_wave_16bit, audio_wave_16bit)).T

# Create a temporary WAV file
wav_file_path = './tmp/temp_audio.wav'
write(wav_file_path, sample_rate, stereo_audio_wave)

# Generate a blank video clip (as we don't have any video input, a blank video is generated)
video_clip = mpe.ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration_seconds)

# Load the audio file
audio_background = mpe.AudioFileClip(wav_file_path)

# Set the audio of the video clip
final_clip = video_clip.set_audio(audio_background)

# Write the final video file with AAC audio and specify fps
mp4_file_path = './tmp/generated_video.mp4'
final_clip.write_videofile(mp4_file_path, codec='libx264', audio_codec='aac', fps=24)

# Clean up the temporary WAV file
os.remove(wav_file_path)

# Adding Hint Tracks using ffmpeg
# Ensure ffmpeg is installed and accessible in the system's PATH
ffmpeg_command = [
    "ffmpeg",
    "-i", mp4_file_path,  # Input file
    "-movflags", "faststart",  # Optimize for fast web start
    "-c", "copy",  # Copy video and audio streams
    "-hint",  # Add hinting for optimized streaming
    mp4_file_path.replace(".mp4", "_hinted.mp4")  # Output file
]

subprocess.run(ffmpeg_command)

print(f"MP4 file with AAC audio and Hint Tracks generated at: {mp4_file_path.replace('.mp4', '_hinted.mp4')}")