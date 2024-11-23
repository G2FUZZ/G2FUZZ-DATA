import cv2
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip, ImageClip, concatenate_videoclips
import os
from scipy.io.wavfile import write
import subprocess  # Import subprocess

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
video_file_path = './tmp/generated_video.mp4'
audio_file_path = './tmp/generated_audio.mp3'
still_picture_path = './tmp/still_picture.jpg'
final_output_path = './tmp/final_output_with_still.mp4'
fragmented_output_path = './tmp/final_output_with_still_fragmented.mp4'  # Fragmented MP4 output

# Generate video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height))

for frame_number in range(fps * duration):
    # Create a frame with a moving circle
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.circle(frame, (frame_number % width, height // 2), 50, (255, 0, 0), -1)
    video.write(frame)

video.release()

# Generate a synthetic audio (sine wave) and save
sample_rate = 44100
T = duration
t = np.linspace(0, T, int(T*sample_rate), endpoint=False)
audio = 0.5*np.sin(2*np.pi*220*t)  # 220 Hz sine wave

write(audio_file_path.replace('.mp3', '.wav'), sample_rate, audio.astype(np.float32))

# Convert WAV to MP3
audio_clip = AudioFileClip(audio_file_path.replace('.mp3', '.wav'))
audio_clip.write_audiofile(audio_file_path)

# Generate Still Picture and save it
still_image = np.zeros((height, width, 3), dtype=np.uint8)
cv2.putText(still_image, "Still Picture", (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite(still_picture_path, still_image)

# Add audio to video
video_clip = VideoFileClip(video_file_path)
video_clip = video_clip.set_audio(AudioFileClip(audio_file_path))

# Adding the still picture as the first frame with a duration
still_frame = ImageClip(still_picture_path).set_duration(3)
final_clip = concatenate_videoclips([still_frame, video_clip])

final_clip.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

# Convert the MP4 to Fragmented MP4 (fMP4) using FFmpeg directly
command = [
    'ffmpeg',
    '-i', final_output_path,  # Input file
    '-movflags', 'frag_keyframe+empty_moov',  # Fragmented MP4 flags
    '-codec', 'copy',  # Copy video and audio streams without re-encoding
    fragmented_output_path  # Output file
]
subprocess.run(command, check=True)

# Clean up intermediate files if needed
os.remove(video_file_path)
os.remove(audio_file_path)
os.remove(audio_file_path.replace('.mp3', '.wav'))
# Optionally remove the still picture file if not needed
# os.remove(still_picture_path)