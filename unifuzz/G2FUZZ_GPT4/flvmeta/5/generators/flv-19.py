import os
import numpy as np
from moviepy.editor import AudioFileClip, CompositeVideoClip  # Using moviepy.editor for audio and potentially video
from moviepy.audio.fx.all import audio_normalize
from moviepy.video.VideoClip import ColorClip  # Importing for creating a dummy video
from scipy.io.wavfile import write  # Importing for saving the audio array to a WAV file

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave for audio
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
t = np.linspace(0, duration, int(sample_rate * duration))
audio = np.sin(2 * np.pi * frequency * t)

# Save the audio array to a WAV file
audio_file_path = os.path.join(output_dir, "generated_audio.wav")
write(audio_file_path, sample_rate, audio.astype(np.float32))

# Convert the audio array to an audio clip
audio_clip = AudioFileClip(audio_file_path)  # Now using the path to the audio file

# Normalize audio to prevent clipping
normalized_audio = audio_normalize(audio_clip)

# Create a dummy video clip of the same duration as the audio clip
# Here we create a black screen as a placeholder
video_clip = ColorClip(size=(640, 480), color=(0, 0, 0), duration=duration)

# Set the audio of the video clip as the normalized audio
video_clip = video_clip.set_audio(normalized_audio)

# Set the fps for the video clip
video_clip.fps = 24  # Setting fps to 24, but you can adjust this value as needed

# Export the combined clip as an FLV file with AAC audio
# Including video enables the use of keyframes for navigation
output_file = os.path.join(output_dir, "generated_video_with_audio.flv")
video_clip.write_videofile(output_file, codec='flv', audio_codec='aac', fps=24)  # Specifying fps here as well

print(f"Generated video with keyframe navigation at: {output_file}")