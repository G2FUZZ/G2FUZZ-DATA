from moviepy.editor import concatenate_audioclips, AudioFileClip, ColorClip
from pydub.generators import Sine
from pydub import AudioSegment
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate synthetic audio tracks using pydub
def generate_sine_wave(frequency=440, duration=3000):
    # Generate a sine wave of a given frequency (Hz) and duration (milliseconds)
    sine_wave = Sine(frequency)
    audio = sine_wave.to_audio_segment(duration=duration)
    return audio

# Generate two audio tracks with different frequencies
audio1 = generate_sine_wave(440, 5000)  # A4 note
audio2 = generate_sine_wave(494, 5000)  # B4 note

# Export these audio tracks as temporary files
audio1.export("./tmp/audio1.mp3", format="mp3")
audio2.export("./tmp/audio2.mp3", format="mp3")

# Use moviepy to combine these audio tracks into an mp4 file
# Create a silent video clip as a placeholder for the audio
video_clip = ColorClip(size=(640, 480), color=(0, 0, 0), duration=5)

# Load the audio tracks
audio_clip1 = AudioFileClip("./tmp/audio1.mp3")
audio_clip2 = AudioFileClip("./tmp/audio2.mp3")

# Combine audio tracks
final_audio = concatenate_audioclips([audio_clip1, audio_clip2])

# Set the audio of the video clip
video_clip = video_clip.set_audio(final_audio)

# Write the result to a file, specifying the fps
video_clip.write_videofile("./tmp/multi_track_audio.mp4", codec="libx264", audio_codec="aac", fps=24)

# Clean up temporary audio files if desired
os.remove("./tmp/audio1.mp3")
os.remove("./tmp/audio2.mp3")