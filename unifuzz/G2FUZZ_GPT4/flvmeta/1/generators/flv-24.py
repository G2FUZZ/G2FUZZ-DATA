from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip
from moviepy.video.fx.loop import loop as video_loop  # Assuming this is the correct import
from moviepy.audio.fx.audio_loop import audio_loop  # Assuming this is the correct import
import numpy as np
import os
from scipy.io import wavfile

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration=1, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 32767).astype(np.int16)

# Function to generate a looping video clip
def generate_looping_video(audio_clip, image_clip, loop_duration):
    # Calculate the number of loops required to reach the desired duration
    loops_required = int(np.ceil(loop_duration / audio_clip.duration))
    # Loop the audio and video clips
    looped_audio = audio_clip.fx(audio_loop, duration=loop_duration)
    looped_video = image_clip.fx(video_loop, duration=loop_duration)
    return looped_audio, looped_video

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

# Specify the desired total duration of the looping video in seconds
loop_duration = 60  # For example, 60 seconds

# Generate looped audio and video clips
looped_audio, looped_video = generate_looping_video(audio_clip, image_clip, loop_duration)

# Combine the looped audio and the blank video clip
video_clip = CompositeVideoClip([looped_video.set_position("center")], size=(640,360))
video_clip = video_clip.set_audio(looped_audio)

# Export the combination as an FLV file
flv_filename = os.path.join(output_dir, 'output_audio_looped.flv')
video_clip.write_videofile(flv_filename, codec='flv')

# Clean up the temporary WAV file
os.remove(temp_audio_filename)

print(f"FLV file with looping audio has been saved to: {flv_filename}")