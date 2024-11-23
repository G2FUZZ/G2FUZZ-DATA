from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip
import numpy as np
import os
from scipy.io import wavfile

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration=1, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_duration * sample_rate), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 32767).astype(np.int16)

# Generate a 1-second tone at 440Hz (A4 note)
sample_duration = 1  # in seconds
audio_data = generate_tone()

# Save the tone as a temporary WAV file (since moviepy can read WAV to create AudioFileClip)
temp_audio_filename = os.path.join(output_dir, 'temp_audio.wav')
wavfile.write(temp_audio_filename, 44100, audio_data)

# Create an AudioFileClip
audio_clip = AudioFileClip(temp_audio_filename)

# Create a blank image (e.g., black) for the video background
# Here, we create a black image of size 640x360
blank_image = np.zeros((360, 640, 3), dtype=np.uint8)
image_clip = ImageClip(blank_image, duration=audio_clip.duration).set_fps(24)

# Combine the audio and the blank video clip
video_clip = CompositeVideoClip([image_clip.set_position("center")], size=(640,360))
video_clip = video_clip.set_audio(audio_clip)

# Export the combination as an FLV file
flv_filename = os.path.join(output_dir, 'output_audio.flv')
video_clip.write_videofile(flv_filename, codec='flv')

# Clean up the temporary WAV file
os.remove(temp_audio_filename)

print(f"FLV file with audio has been saved to: {flv_filename}")