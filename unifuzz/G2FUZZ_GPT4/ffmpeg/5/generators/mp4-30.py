from moviepy.editor import ColorClip, AudioFileClip, concatenate_videoclips
import numpy as np
from scipy.io.wavfile import write
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate synthetic audio files
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Generate a sine wave for the first track
t = np.linspace(0, duration, int(sample_rate * duration))
sine_wave = np.sin(2 * np.pi * 220 * t)  # 220 Hz sine wave
write(output_dir + 'sine_wave.wav', sample_rate, sine_wave.astype(np.float32))

# Generate a cosine wave for the second track
cosine_wave = np.cos(2 * np.pi * 220 * t)  # 220 Hz cosine wave
write(output_dir + 'cosine_wave.wav', sample_rate, cosine_wave.astype(np.float32))

# Create a silent video clip of the same duration
video_clip = ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration)

# Set the fps for the video clip
video_clip.fps = 24  # Set the frames per second

# Set the audio of the video clip to the first audio track (sine wave)
video_clip = video_clip.set_audio(AudioFileClip(output_dir + 'sine_wave.wav'))

# Export the video clip with the first audio track to an MP4 file
video_clip.write_videofile(output_dir + 'video_with_sine_wave.mp4', codec='libx264', audio_codec='aac', fps=24)

# Use ffmpeg to add the second audio track (cosine wave) and GPS metadata to the MP4
# This will create a final MP4 with two audio tracks and embedded location data
# Sample GPS coordinates for metadata (Latitude and Longitude): 40.712776, -74.005974 (New York City)
latitude = "40.712776"
longitude = "-74.005974"
os.system(f"ffmpeg -i {output_dir}video_with_sine_wave.mp4 -i {output_dir}cosine_wave.wav -map 0:v -map 0:a -map 1:a -metadata:s:v:0 rotate=0 -metadata location={latitude} {longitude} -c copy -shortest {output_dir}final_video_with_location.mp4")

# Clean up temporary audio files
os.remove(output_dir + 'sine_wave.wav')
os.remove(output_dir + 'cosine_wave.wav')