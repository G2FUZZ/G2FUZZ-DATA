import cv2
import numpy as np
import os
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_audioclips
from scipy.io.wavfile import write

# Ensure tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video settings
width, height = 640, 480
fps = 24
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files

# Audio settings
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz

def generate_audio(filename, duration, frequency):
    t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
    audio_data = np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit data
    write(filename, sample_rate, audio_data)

def generate_video(video_filename, audio_filename, final_output_filename, effect):
    # Generate audio
    generate_audio(audio_filename, duration, frequency)

    # Create VideoWriter object
    out = cv2.VideoWriter(video_filename, codec, fps, (width, height))

    # Generate video content with a specific effect
    num_frames = int(fps * duration)
    for i in range(num_frames):
        frame = np.zeros((height, width, 3), np.uint8)
        if effect == "move":
            cv2.rectangle(frame, (10 + i*5, 50), (60 + i*5, 100), (255, 255, 255), -1)
        elif effect == "color":
            color = (0, 255, 0) if i < num_frames // 2 else (0, 0, 255)
            cv2.rectangle(frame, (100, 50), (150, 100), color, -1)
        elif effect == "expand":
            cv2.rectangle(frame, (100, 50), (100 + i, 100 + i), (255, 255, 255), -1)
        out.write(frame)

    # Release everything when job is finished
    out.release()

    # Combine the video file with the audio file
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(final_output_filename, codec='libx264', audio_codec='aac')

# Generate videos with different effects
generate_video('./tmp/sample_video_move.mp4', './tmp/sample_audio_move.wav', './tmp/final_output_move.mp4', "move")
generate_video('./tmp/sample_video_color.mp4', './tmp/sample_audio_color.wav', './tmp/final_output_color.mp4', "color")
generate_video('./tmp/sample_video_expand.mp4', './tmp/sample_audio_expand.wav', './tmp/final_output_expand.mp4', "expand")

# Implementing the user interactivity feature to allow users to choose which video to play would require a separate platform or web technologies.