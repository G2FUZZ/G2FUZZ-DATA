import numpy as np
import cv2
import os
import wave
import contextlib
from scipy.io.wavfile import write as wav_write
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
from mutagen.mp3 import MP3

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video and audio specifications
output_filename = output_dir + "complex_example_streaming_with_aux.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
duration_sec = 10  # Duration of the video in seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec definition
audio_sample_rate = 44100  # Sample rate for audio
audio_filename = output_dir + "temp_audio.wav"  # Temporary audio file

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

# Generate video frames
for i in range(fps * duration_sec):
    # Create a black image for the background
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Dynamically adjust the rectangle's movement
    x_speed = 2  # Speed of the rectangle along the x-axis
    start_point = ((i * x_speed) % frame_size[0], 100)  # Moving along the x-axis with wrap-around
    end_point = (start_point[0] + 100, 200)  # Fixed size
    color = (255, 255, 255)  # White color for the rectangle
    thickness = -1  # Solid rectangle
    
    # Draw the rectangle on the frame
    cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Add custom text overlay on each frame
    text_position = (10, frame_size[1] - 10)
    cv2.putText(frame, f"Frame {i+1}", text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Write the frame into the video file
    out.write(frame)

# Release the VideoWriter object
out.release()

# Generate a simple sine wave as the audio track
t = np.linspace(0, duration_sec, int(audio_sample_rate * duration_sec), False)
# Generate sine wave sound
freq = 440.0  # Frequency of the sine wave (A4)
audio = np.sin(freq * 2 * np.pi * t)
audio = np.int16(audio * 32767)
wav_write(audio_filename, audio_sample_rate, audio)

# Combine the video with the generated audio
video = MP4(output_filename)
video["\xa9nam"] = "Complex Example Video"
video["\xa9ART"] = "AI Generated"
video["\xa9alb"] = "AI Album"
video.save()

# Add cover image with dynamically created content
cover_img_path = './tmp/cover_complex.jpg'
cover_img = np.zeros((300, 300, 3), dtype=np.uint8)  # Create a black image for the cover
cover_img = cv2.putText(cover_img, 'Complex Cover', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.imwrite(cover_img_path, cover_img)

# Embed the cover image and save the final video file
with open(cover_img_path, 'rb') as img:
    video["covr"] = [MP4Cover(img.read(), imageformat=MP4Cover.FORMAT_JPEG)]
video.save()

# Clean up temporary audio file
os.remove(audio_filename)

print(f"Complex video with auxiliary information successfully saved to {output_filename}")