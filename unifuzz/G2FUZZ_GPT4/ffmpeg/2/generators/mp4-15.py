import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os
from moviepy.editor import *

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def generate_3d_animation_with_audio():
    # Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Initial plot
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-1, 1, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    line, = ax.plot(x, y, z, label='3D curve')

    # Animation update function
    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])
        return line,

    # Generating data
    data = np.array([x, y, z])

    # Creating the animation
    ani = animation.FuncAnimation(fig, update, len(z), fargs=(data, line),
                                  interval=100, blit=False)

    # Temporary save path for the video without audio
    temp_video_path = './tmp/3d_graphics_animation_temp.mp4'
    # Save the animation
    ani.save(temp_video_path, writer='ffmpeg', fps=30)

    # Add Lossless Audio
    # Load or create an audio clip. Here, we're assuming the presence of a lossless audio file (e.g., .flac or .alac)
    # For demonstration, this step is commented out as it requires an actual audio file.
    # audio_clip = AudioFileClip('path_to_lossless_audio_file.flac')

    # Create a video clip from the temporary video
    video_clip = VideoFileClip(temp_video_path)

    # Assuming audio_clip is shorter than the video, we loop it. Uncomment and adjust as needed.
    # final_audio = audio_clip.fx(afx.audio_loop, duration=video_clip.duration)

    # Set the audio of the video clip. Uncomment and adjust the audio_clip variable as needed.
    # final_clip = video_clip.set_audio(final_audio)

    # Save the final video with audio. Adjust the filename as needed.
    # final_clip.write_videofile('./tmp/3d_graphics_animation_with_lossless_audio.mp4', codec='libx264', audio_codec='aac')

    # For this example, since we can't include an actual audio file, we just rename the temporary video.
    os.rename(temp_video_path, './tmp/3d_graphics_animation_with_lossless_audio.mp4')

generate_3d_animation_with_audio()