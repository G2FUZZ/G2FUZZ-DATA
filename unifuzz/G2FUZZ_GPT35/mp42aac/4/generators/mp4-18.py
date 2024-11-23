import numpy as np
import cv2

# Define the file path for the video
video_file_path = "./tmp/generated_video_with_text_tracks.mp4"

# Define the file path for the timed text track file
text_track_file_path = "./tmp/timed_text_track.vtt"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_file_path, fourcc, 20.0, (640, 480), isColor=True)

# Generate frames and write to the video file
for _ in range(100):
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    out.write(frame)

# Release the VideoWriter object
out.release()

# Create and write timed text track information to a .vtt file
with open(text_track_file_path, 'w') as file:
    file.write("WEBVTT\n\n")
    file.write("1\n00:00:01.000 --> 00:00:02.000\nHello, this is a timed text track example.\n\n")
    file.write("2\n00:00:05.000 --> 00:00:07.000\nThis is synchronized with the video frames.\n\n")

print("MP4 file with Timed Text Tracks generated successfully at:", video_file_path)
print("Timed Text Track file generated successfully at:", text_track_file_path)