from moviepy.config import change_settings
from moviepy.editor import ColorClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import numpy as np
from scipy.io.wavfile import write
import os

# Update this path to the actual location of the ImageMagick binary on your system
imagemagick_path = "/path/to/your/imagemagick/binary"
change_settings({"IMAGEMAGICK_BINARY": imagemagick_path})

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Your existing code follows here...

# Example settings and clips for demonstration. Replace or modify as needed.
clip1 = ColorClip(size=(640, 480), color=(255, 0, 0), duration=2)
clip2 = ColorClip(size=(640, 480), color=(0, 255, 0), duration=3).set_fps(24)
clip3 = ColorClip(size=(640, 480), color=(0, 0, 255), duration=3).set_fps(30)

# Concatenate clips with potentially different frame rates
final_clip = concatenate_videoclips([clip1, clip2, clip3])

# Generating a sine wave audio for demonstration
freq = 440  # Frequency in Hz
duration = final_clip.duration  # Duration in seconds
sampling_rate = 44100  # Sampling rate in Hz
t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
audio = np.sin(2*np.pi*freq*t).astype(np.float32)

# Save the audio to a file
audio_filename = os.path.join(output_dir, 'example_audio.wav')
write(audio_filename, sampling_rate, audio)

# Add the audio to the final clip
audio_clip = AudioFileClip(audio_filename)
final_clip = final_clip.set_audio(audio_clip)

# Write the output file. Note: write_videofile will automatically adjust the frame rate
# according to the varying fps of the input clips if the codec and container support VFR.
output_filename = os.path.join(output_dir, 'final_video_with_vfr.mp4')
final_clip.write_videofile(output_filename, codec='libx264', audio_codec='aac')
