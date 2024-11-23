import numpy as np
import cv2
import wave
import contextlib
import os
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a simple animation with OpenCV
frame_count = 300
frame_width = 640
frame_height = 480
fps = 30

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_path = os.path.join(tmp_dir, 'lossless_compression_video.mp4')
out = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

for i in range(frame_count):
    # Create a frame with a moving circle
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.circle(frame, (frame_width // 2 + int(frame_width * 0.3 * np.sin(2 * np.pi * i / frame_count)),
                       frame_height // 2 + int(frame_height * 0.3 * np.cos(2 * np.pi * i / frame_count))),
               50, (0, 255, 0), -1)
    out.write(frame)

# Release everything
out.release()

# Generate a lossless WAV file
sample_rate = 44100  # Sample rate in Hz
duration = frame_count / fps  # seconds

t = np.linspace(0., duration, int(sample_rate * duration))
audio_data = (np.sin(2 * np.pi * 440 * t) * 32767).astype(np.int16)

wav_path = os.path.join(tmp_dir, 'lossless_audio.wav')
with wave.open(wav_path, 'w') as wav:
    wav.setnchannels(1)  # mono
    wav.setsampwidth(2)  # two bytes per sample
    wav.setframerate(sample_rate)
    wav.writeframes(audio_data.tobytes())

# Combine the video and audio using MoviePy
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(wav_path)
final_clip = video_clip.set_audio(audio_clip)

# Before saving, let's apply the Edit Lists feature by trimming and reordering
# Example: Let's cut the video in three parts, reorder them, and skip some parts
# Assuming each part is of equal duration (for simplicity)
part_duration = duration / 3  # in seconds

# Temporary clips for the demonstration, adjust indices as needed
clip1 = video_clip.subclip(0, part_duration)
clip2 = video_clip.subclip(part_duration, 2*part_duration)
clip3 = video_clip.subclip(2*part_duration, 3*part_duration)

# Reordering clips (e.g., 3 -> 1 -> 2) and skipping clip 2 for this example
edited_clip = concatenate_videoclips([clip3, clip1], method="compose")

# Set the audio for the edited clip
# For simplicity, use the same audio throughout. For more complex edits, adjust the audio accordingly.
edited_clip = edited_clip.set_audio(audio_clip)

# Save the final video with the Edit Lists
edited_clip.write_videofile(os.path.join(tmp_dir, 'final_lossless_video_with_edits.mp4'), codec='libx264', audio_codec='aac')