import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
from scipy.io.wavfile import write
import datetime

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
output_video_path = './tmp/generated_video.mp4'

# Generate video frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    # Create a frame with changing colors
    color = tuple(np.random.randint(0, 255, size=3).tolist())
    frame = np.full((height, width, 3), color, dtype=np.uint8)
    video.write(frame)

video.release()

# Generate synthetic audio
audio_output_path = './tmp/generated_audio.wav'
samplerate = 44100
t = np.linspace(0., duration, samplerate * duration)
frequency = 440  # A4
audio = 0.5 * np.sin(2. * np.pi * frequency * t)

write(audio_output_path, samplerate, audio.astype(np.float32))

# Combine video and audio
video_clip = VideoFileClip(output_video_path)
audio_clip = AudioFileClip(audio_output_path)
final_clip = video_clip.set_audio(audio_clip)

# Specify final output path
final_output_path = './tmp/final_output.mp4'
final_clip.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

# Clean up temporary files
os.remove(output_video_path)
os.remove(audio_output_path)

# Add content identification and tracking metadata to the MP4 file
content_id = "UNIQUE_CONTENT_ID_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
video_file = MP4(final_output_path)
video_file["\xa9nam"] = "Generated Video with Content ID"
video_file["\xa9alb"] = "Generated Album"
video_file["\xa9ART"] = "Generated Artist"
video_file["\xa9day"] = datetime.datetime.now().strftime("%Y")
video_file["desc"] = "This is a generated video including content identification and tracking features."
video_file["cprt"] = "Copyright Notice"
video_file["----:com.apple.iTunes:CONTENTID"] = content_id.encode("utf-8")  # Custom metadata field for content ID

# Save the file with metadata
video_file.save()