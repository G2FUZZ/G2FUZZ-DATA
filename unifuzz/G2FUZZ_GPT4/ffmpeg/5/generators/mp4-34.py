import cv2
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Define the output directory
output_directory = './tmp/'

# Ensure the tmp directory exists
os.makedirs(output_directory, exist_ok=True)

# Video parameters
width, height = 1920, 480  # Updated for panoramic view
fps = 30
duration = 5  # seconds
video_filename = os.path.join(output_directory, 'video.mp4')
audio_filename = os.path.join(output_directory, 'audio.wav')
output_filename = os.path.join(output_directory, 'output_with_panoramic_and_iso_compatibility.mp4')

# Generate video with panoramic dimensions
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Using 'mp4v' ensures compatibility with the ISO base media file format
video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    img = np.zeros((height, width, 3), dtype='uint8')
    cv2.rectangle(img, (frame_num*5 % width, 100), ((frame_num*5 % width) + 50, 150), (0, 255, 0), -1)
    video.write(img)

video.release()

# Generate a sine wave audio tone
tone = Sine(440)  # A4 note, 440 Hz
audio = tone.to_audio_segment(duration=duration*1000)
audio.export(audio_filename, format='wav')

# Combine video and audio
video_clip = VideoFileClip(video_filename)
audio_clip = AudioFileClip(audio_filename)
final_clip = video_clip.set_audio(audio_clip)

# Write the final video file ensuring ISO Base Media File Format Compatibility
final_clip.write_videofile(output_filename, codec="libx264", fps=fps)

# Clean up the temporary video and audio files
os.remove(video_filename)
os.remove(audio_filename)

print(f"MP4 file with panoramic video, audio, and ISO Base Media File Format Compatibility has been saved to {output_directory}")