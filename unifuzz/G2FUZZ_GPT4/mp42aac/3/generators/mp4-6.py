import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import imageio

# Directory to save the generated MP4 file
output_directory = './tmp/'
output_filename = '3d_graphics_storage.mp4'

# Ensure the output directory exists
import os
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate 3D graphics (a rotating sine wave)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi)
z = np.linspace(0, 1, 100)

# Initial plot
line, = ax.plot(x, y, z)

def update(num, x, y, z, line):
    ax.view_init(elev=10., azim=num)
    line.set_data(x, np.sin(x * 2 * np.pi + np.pi * num / 50))
    line.set_3d_properties(np.linspace(0, 1, 100))
    return line,

ani = animation.FuncAnimation(fig, update, frames=360, fargs=(x, y, z, line), interval=50)

# Save the animation as an MP4 file
ani.save(os.path.join(output_directory, output_filename), writer='ffmpeg', fps=20)

plt.close(fig)