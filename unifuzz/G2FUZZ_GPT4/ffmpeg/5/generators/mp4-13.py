import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import clips_array, VideoFileClip

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define parameters for the animation
frames = 100  # Number of frames in the animation
fps = 10  # Frames per second

def create_animation(angle_function, file_path):
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'r-')

    def init():
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(-1, 1)
        return ln,

    def update(frame):
        xdata.append(frame * 2 * np.pi / frames)
        ydata.append(angle_function(xdata[-1]))
        ln.set_data(xdata, ydata)
        return ln,

    ani = FuncAnimation(fig, update, frames=range(frames),
                        init_func=init, blit=True)
    ani.save(file_path, writer='ffmpeg', fps=fps)
    plt.close(fig)

# Define different "angle" functions
def angle1(x):
    return np.sin(x)

def angle2(x):
    return np.cos(x)

# Create animations for each "angle"
mp4_files = []
for i, angle_function in enumerate([angle1, angle2], start=1):
    file_path = os.path.join(output_dir, f"animation_angle{i}.mp4")
    create_animation(angle_function, file_path)
    mp4_files.append(file_path)

# Combine videos side by side to simulate multiple angles
clips = [VideoFileClip(mp) for mp in mp4_files]
final_clip = clips_array([[clip] for clip in clips])
final_clip_path = os.path.join(output_dir, "combined_animation.mp4")
final_clip.write_videofile(final_clip_path, fps=fps)

for clip in clips:  # Close the clips to release resources
    clip.close()

print(f"Combined MP4 file generated at: {final_clip_path}")