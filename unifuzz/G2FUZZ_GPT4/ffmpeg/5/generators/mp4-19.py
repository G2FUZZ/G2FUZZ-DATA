import os
import numpy as np
from moviepy.editor import *
from moviepy.audio.AudioClip import AudioArrayClip
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define parameters for the animation
frames = 100  # Number of frames in the animation
fps = 10  # Frames per second

# Create a figure for plotting
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')

# Initialize the animation
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

# Update function for the animation
def update(frame):
    xdata.append(frame * 2 * np.pi / frames)
    ydata.append(np.sin(xdata[-1]))
    ln.set_data(xdata, ydata)
    return ln,

# Create an animation
ani = FuncAnimation(fig, update, frames=range(frames),
                    init_func=init, blit=True)

# Save the animation as an MP4 file
mp4_file = os.path.join(output_dir, "animation_with_he_aac.mp4")
ani.save(mp4_file, writer='ffmpeg', fps=fps)

# Generate a silent audio clip
audio_duration = frames / fps  # Duration of the video in seconds
silent_audio_array = np.zeros((int(audio_duration * 44100), 2))  # Assuming stereo audio
silent_audio = AudioArrayClip(silent_audio_array, fps=44100)

# Loading video file
video_clip = VideoFileClip(mp4_file)

# Adding the silent audio to the video
final_clip = video_clip.set_audio(silent_audio)

# Exporting the video with audio
final_output = os.path.join(output_dir, "final_animation_with_he_aac.mp4")
final_clip.write_videofile(final_output, codec="libx264", audio_codec="aac")

print("MP4 file with HE-AAC audio feature generated at:", final_output)