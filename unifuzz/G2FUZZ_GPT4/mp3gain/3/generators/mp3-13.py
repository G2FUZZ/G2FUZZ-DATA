import os
from pydub import AudioSegment
from pydub.generators import Sine
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone as an example of audio data
frequency = 440  # Frequency in Hz (A4 note)
duration_ms = 5000  # Duration in milliseconds of the generated tone

# Generate the sine wave tone
tone = Sine(frequency).to_audio_segment(duration=duration_ms)

# Setting up multiple frames (in a very basic representation)
# by concatenating the same tone, simulating multiple frames of data in an MP3 file
frames_to_generate = 5  # Number of frames to simulate
audio_frames = tone
for _ in range(1, frames_to_generate):
    audio_frames += tone

# Export the generated frames as an MP3 file
audio_frames.export("./tmp/generated_frames.mp3", format="mp3")

# Encapsulation: Incorporate the MP3 in an MP4 container format
# First, convert the audio file to a format usable with moviepy
audio_clip = AudioFileClip("./tmp/generated_frames.mp3")

# Create a silent color clip with the same duration as the audio clip
# This is a workaround to encapsulate audio as MP4 requires a video track, even if it's just a blank screen
video_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=audio_clip.duration)

# Set the audio of the color clip to our generated MP3
video_clip = video_clip.set_audio(audio_clip)

# Combine everything into one video clip, here it's just the color clip with audio
final_clip = concatenate_videoclips([video_clip])

# Export the final clip as an MP4, encapsulating the MP3 within it
# Specify the fps directly in the write_videofile function call
final_clip.write_videofile("./tmp/encapsulated_audio.mp4", codec="libx264", audio_codec="aac", fps=24)