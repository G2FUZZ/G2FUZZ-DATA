import cv2
import numpy as np
from pydub.generators import Sine
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip

# Parameters for the video
width, height = 640, 480
fps = 24
duration = 5  # in seconds
output_video_path = './tmp/generated_video.mp4'
output_audio_path = './tmp/generated_audio.mp3'
output_final_path = './tmp/final_output.mp4'

# Create a video with OpenCV
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(frame, (frame_num*5 % width, 50), ((frame_num*5 % width) + 50, 100), (255, 0, 0), -1)
    video.write(frame)

video.release()

# Generate a tone using pydub
tone = Sine(440).to_audio_segment(duration=duration*1000)
tone.export(output_audio_path, format="mp3")

# Combine the video and audio using moviepy
video_clip = VideoFileClip(output_video_path)
audio_clip = AudioFileClip(output_audio_path)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(output_final_path, codec="libx264", fps=fps)

print("MP4 file with video and audio has been generated.")