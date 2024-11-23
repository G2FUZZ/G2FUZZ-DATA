import numpy as np
import os
import wave
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips, VideoFileClip
import cv2

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave as an example audio signal
duration = 10  # duration of the audio clip in seconds
sample_rate = 44100  # sample rate in Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # time variable
frequency = 440  # sine frequency in Hz
audio = np.sin(2 * np.pi * frequency * t)  # generate sine wave

# Convert the numpy array to a suitable format
audio = (audio * 32767).astype(np.int16)  # convert to 16-bit PCM

# Save the audio as a temporary WAV file (will be used to create the MP4)
temp_audio_file = os.path.join(output_dir, "temp_audio.wav")
with wave.open(temp_audio_file, 'w') as wav_file:
    wav_file.setnchannels(1)  # mono audio
    wav_file.setsampwidth(2)  # 16 bits per sample
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio)

# Placeholder for generating a 360-degree video frame
def generate_360_video_frame(color, size, frame_number, total_frames):
    # This example will just change the color over time, more sophisticated 360 video generation can be done here
    progress = frame_number / total_duration
    new_color = tuple([int(c * progress) for c in color])
    frame = np.full((size[1], size[0], 3), new_color, dtype=np.uint8)
    return frame

# Create a video clip with 360-degree frames
total_duration = 10  # duration of the video in seconds
fps = 24  # frames per second for the video
total_frames = total_duration * fps

video_frames = []
for frame_number in range(total_frames):
    frame = generate_360_video_frame(color=(255, 0, 0), size=(640, 480), frame_number=frame_number, total_frames=total_frames)
    video_frames.append(frame)

# Convert frames to video
video_path = os.path.join(output_dir, "360_video_temp.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
video = cv2.VideoWriter(video_path, fourcc, float(fps), (640, 480))

for frame in video_frames:
    video.write(frame)
video.release()

# Combine the 360-degree video with the audio
audio_clip = AudioFileClip(temp_audio_file)
video_clip = VideoFileClip(video_path)
video_clip = video_clip.set_audio(audio_clip)

# Create an MP4 file containing the AAC encoded audio
mp4_output = os.path.join(output_dir, "output_with_360.mp4")
video_clip.write_videofile(mp4_output, codec="libx264", audio_codec="aac", fps=24)

# Clean up the temporary files and video clips
os.remove(temp_audio_file)
os.remove(video_path)
video_clip.close()
audio_clip.close()