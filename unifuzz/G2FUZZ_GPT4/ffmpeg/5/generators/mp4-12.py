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
t = np.linspace(0, duration, int(sample_rate*duration))
sine_wave = np.sin(2*np.pi*220*t)  # 220 Hz sine wave
write(output_dir + 'sine_wave.wav', sample_rate, sine_wave.astype(np.float32))

# Generate a cosine wave for the second track
cosine_wave = np.cos(2*np.pi*220*t)  # 220 Hz cosine wave
write(output_dir + 'cosine_wave.wav', sample_rate, cosine_wave.astype(np.float32))

# Create a silent video clip of the same duration
video_clip = ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration)

# Set the fps for the video clip
video_clip.fsp = 24  # Set the frames per second

# Set the audio of the video clip to the first audio track (sine wave)
video_clip = video_clip.set_audio(AudioFileClip(output_dir + 'sine_wave.wav'))

# Export the video clip with the first audio track to an MP4 file
video_clip.write_videofile(output_dir + 'video_with_sine_wave.mp4', codec='libx264', audio_codec='aac', fps=24)

# Use ffmpeg to add the second audio track (cosine wave) to the MP4
# This will create a final MP4 with two audio tracks
os.system(f"ffmpeg -i {output_dir}video_with_sine_wave.mp4 -i {output_dir}cosine_wave.wav -map 0:v -map 0:a -map 1:a -c copy -shortest {output_dir}final_video_with_multi_track_audio.mp4")

# To add VR content, we need to specify a spherical video metadata to the output video
# This metadata can be added using ffmpeg with the following command
# The metadata indicates that the video is in equirectangular format, suitable for VR playback
os.system(f"ffmpeg -i {output_dir}final_video_with_multi_track_audio.mp4 -metadata:s:v:0 stereo_mode=1 -c copy {output_dir}final_vr_video.mp4")

# Clean up temporary audio files
os.remove(output_dir + 'sine_wave.wav')
os.remove(output_dir + 'cosine_wave.wav')