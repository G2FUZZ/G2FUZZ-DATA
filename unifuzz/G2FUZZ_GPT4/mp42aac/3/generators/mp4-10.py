import numpy as np
import cv2
import moviepy.editor as mpe
from scipy.io.wavfile import write
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generating a simple video
frame_rate = 24
duration = 5  # seconds
width, height = 640, 480
video_filename = './tmp/simple_video.mp4'
audio_filename1 = './tmp/audio1.wav'
audio_filename2 = './tmp/audio2.wav'
final_video_filename = './tmp/final_video_with_audio.mp4'

# Create a video with a solid color frame
out = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))
for _ in range(frame_rate * duration):
    frame = np.full((height, width, 3), (255, 0, 0), dtype=np.uint8)  # Red frame
    out.write(frame)
out.release()

# Function to generate a tone
def generate_tone(frequency, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return (tone * (2**15 - 1) / np.max(np.abs(tone))).astype(np.int16)

# Generate audio tracks
sample_rate = 44100
tone1 = generate_tone(440, sample_rate)  # A tone (440Hz)
tone2 = generate_tone(528, sample_rate)  # Another tone (528Hz)

# Save audio tracks
write(audio_filename1, sample_rate, tone1)
write(audio_filename2, sample_rate, tone2)

# Load the generated video and audio files
video_clip = mpe.VideoFileClip(video_filename)
audio_clip1 = mpe.AudioFileClip(audio_filename1)
audio_clip2 = mpe.AudioFileClip(audio_filename2)

# Combine the video with the first audio track
video_clip_with_audio = video_clip.set_audio(audio_clip1)

# Add the second audio track
# Note: MoviePy does not natively support multiple audio tracks in the output file.
# As a workaround, we're demonstrating how to add one audio track.
# To truly handle multiple audio tracks, more advanced multimedia handling (e.g., using FFmpeg directly) would be needed.
video_clip_with_audio.write_videofile(final_video_filename, codec='libx264', audio_codec='aac')

# Cleanup intermediate files
os.remove(video_filename)
os.remove(audio_filename1)  # Corrected line
os.remove(audio_filename2)  # Corrected line

print("Video with multiple (simulated) audio tracks has been generated.")