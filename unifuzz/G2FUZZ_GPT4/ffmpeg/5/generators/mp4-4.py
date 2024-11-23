import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import *

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
mp4_file = os.path.join(output_dir, "animation.mp4")  # Corrected variable name here
ani.save(mp4_file, writer='ffmpeg', fps=fps)

print(f"MP4 file generated at: {mp4_file}")