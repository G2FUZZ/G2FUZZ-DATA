import cv2
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
video_file_path = './tmp/generated_video.mp4'
audio_file_path = './tmp/generated_audio.mp3'

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
import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
T = duration
t = np.linspace(0, T, int(T*sample_rate), endpoint=False)
audio = 0.5*np.sin(2*np.pi*220*t)  # 220 Hz sine wave

write(audio_file_path.replace('.mp3', '.wav'), sample_rate, audio.astype(np.float32))

# Convert WAV to MP3 (if needed, depending on the system's available codecs)
from moviepy.audio.io.AudioFileClip import AudioFileClip
audio_clip = AudioFileClip(audio_file_path.replace('.mp3', '.wav'))
audio_clip.write_audiofile(audio_file_path)

# Add audio to video
video_clip = VideoFileClip(video_file_path)
video_clip = video_clip.set_audio(AudioFileClip(audio_file_path))
video_clip.write_videofile('./tmp/final_output.mp4', codec='libx264', audio_codec='aac')

# Clean up intermediate files if needed
os.remove(video_file_path)
os.remove(audio_file_path)
os.remove(audio_file_path.replace('.mp3', '.wav'))