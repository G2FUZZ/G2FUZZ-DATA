import cv2
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip
from pydub import AudioSegment
from pydub.generators import Sine
import os
import json

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Video parameters
width, height = 640, 480
fps = 30
duration = 5  # seconds
video_filename = './tmp/video.mp4'
audio_filename = './tmp/audio.wav'
output_filename = './tmp/output.mp4'
descriptors_filename = './tmp/descriptors.json'

# Generate video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

# Object Descriptors list
object_descriptors = []

for frame_num in range(fps * duration):
    img = np.zeros((height, width, 3), dtype='uint8')
    x_start, y_start, x_end, y_end = frame_num*5 % width, 100, (frame_num*5 % width) + 50, 150
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (0, 255, 0), -1)
    video.write(img)
    
    # Add object descriptor for the rectangle in each frame
    object_descriptors.append({
        "frame": frame_num,
        "object": "rectangle",
        "position": {
            "x_start": int(x_start),
            "y_start": int(y_start),
            "x_end": int(x_end),
            "y_end": int(y_end)
        },
        "color": "green"
    })

video.release()

# Generate a sine wave audio tone
tone = Sine(440)  # A4 note, 440 Hz
audio = tone.to_audio_segment(duration=duration*1000)
audio.export(audio_filename, format='wav')

# Save object descriptors to a JSON file
with open(descriptors_filename, 'w') as f:
    json.dump(object_descriptors, f, indent=4)

# Combine video and audio
video_clip = VideoFileClip(video_filename)
audio_clip = AudioFileClip(audio_filename)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(output_filename, codec="libx264", fps=fps)

# Clean up the temporary video and audio files, keeping the descriptors
os.remove(video_filename)
os.remove(audio_filename)

print(f"MP4 file with video, audio, and object descriptors has been saved to {output_filename}")
print(f"Object descriptors saved to {descriptors_filename}")