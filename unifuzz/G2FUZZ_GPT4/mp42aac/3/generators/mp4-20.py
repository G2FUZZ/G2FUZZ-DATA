import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

# Directory to save the generated MP4 file
output_directory = './tmp/'
output_filename = '3d_graphics_with_motion_sensors.mp4'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate 3D graphics (a rotating sine wave with motion sensor simulation)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi)
z = np.linspace(0, 1, 100)

# Initial plot
line, = ax.plot(x, y, z)

# Adding a text annotation to simulate motion sensor data
text = fig.text(0.1, 0.9, '', transform=fig.transFigure)

def update(num, x, y, z, line, text):
    # View angle update simulating motion sensor change
    elev = 10
    azim = num
    ax.view_init(elev=elev, azim=azim)
    line.set_data(x, np.sin(x * 2 * np.pi + np.pi * num / 50))
    line.set_3d_properties(np.linspace(0, 1, 100))
    
    # Update text to simulate sensor data (could be real sensor data in an application)
    text.set_text('Orientation: {:.2f}, {:.2f}'.format(elev, azim))
    return line, text

ani = animation.FuncAnimation(fig, update, frames=360, fargs=(x, y, z, line, text), interval=50)

# Save the animation as an MP4 file
ani.save(os.path.join(output_directory, output_filename), writer='ffmpeg', fps=20)

plt.close(fig)