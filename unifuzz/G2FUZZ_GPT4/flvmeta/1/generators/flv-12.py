from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips
import numpy as np
import os
from scipy.io import wavfile

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration=1, sample_rate=44100):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 32767).astype(np.int16)

# Function to create a temporary audio file given frequency and duration
def create_temp_audio_file(frequency, duration, filename):
    audio_data = generate_tone(frequency, duration)
    wavfile.write(filename, 44100, audio_data)
    return AudioFileClip(filename)

# Generate a 1-second tone at 440Hz (A4 note)
temp_audio_filename1 = os.path.join(output_dir, 'temp_audio1.wav')
audio_clip1 = create_temp_audio_file(440, 1, temp_audio_filename1)

# Generate a 0.5-second tone at 660Hz (E5 note), to demonstrate multiple audio streams
temp_audio_filename2 = os.path.join(output_dir, 'temp_audio2.wav')
audio_clip2 = create_temp_audio_file(660, 0.5, temp_audio_filename2)

# Create a blank image (e.g., black) for the video background
blank_image = np.zeros((360, 640, 3), dtype=np.uint8)

# Create image clips with the duration of each audio clip
image_clip1 = ImageClip(blank_image, duration=audio_clip1.duration).set_fps(24)
image_clip2 = ImageClip(blank_image, duration=audio_clip2.duration).set_fps(24)

# Combine the audio and the blank video clips
video_clip1 = CompositeVideoClip([image_clip1.set_position("center")], size=(640,360)).set_audio(audio_clip1)
video_clip2 = CompositeVideoClip([image_clip2.set_position("center")], size=(640,360)).set_audio(audio_clip2)

# Concatenate the video clips to demonstrate multiple data streams in sequence
final_video_clip = concatenate_videoclips([video_clip1, video_clip2])

# Export the combination as an FLV file
flv_filename = os.path.join(output_dir, 'output_audio_with_multiple_streams.flv')
final_video_clip.write_videofile(flv_filename, codec='flv')

# Clean up the temporary WAV files
os.remove(temp_audio_filename1)
os.remove(temp_audio_filename2)

print(f"FLV file with multiple data streams has been saved to: {flv_filename}")