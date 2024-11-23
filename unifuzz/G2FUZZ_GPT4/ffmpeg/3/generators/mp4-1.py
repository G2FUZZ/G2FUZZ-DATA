import os
import numpy as np
import cv2
from scipy.io import wavfile  # Correct import for audio file handling
from moviepy.editor import VideoFileClip, AudioFileClip

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video settings
fps = 24
duration = 5  # seconds
width, height = 640, 480

# Generate video frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video_path = os.path.join(output_dir, 'temp_video.mp4')
video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.putText(frame, f'Frame {frame_num+1}', (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    video.write(frame)

video.release()

# Generate audio
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)
frequency = 440  # A4
audio_wave = np.sin(frequency * 2 * np.pi * t)
audio_wave = (audio_wave * 32767).astype(np.int16)
audio_path = os.path.join(output_dir, 'temp_audio.wav')

# Correctly save the audio file using wavfile.write
wavfile.write(audio_path, sample_rate, audio_wave)

# Use moviepy to combine the video and audio
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)
final_clip = video_clip.set_audio(audio_clip)
final_path = os.path.join(output_dir, 'final_output.mp4')
final_clip.write_videofile(final_path, codec='libx264', audio_codec='aac')

# Cleanup temporary files
os.remove(video_path)
os.remove(audio_path)

print(f'MP4 file with video and audio has been saved to {final_path}')