import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the 3D graphics function to animate
def generate_3d_animation(filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Generate data for a three-dimensional line
    t = np.linspace(0, 2*np.pi, 100)
    x = t
    y = np.sin(t)
    z = np.cos(t)
    line, = ax.plot(x, y, z)

    # Setting the axes properties
    ax.set_xlim3d([0.0, 2*np.pi])
    ax.set_xlabel('X')
    ax.set_ylim3d([-1.0, 1.0])
    ax.set_ylabel('Y')
    ax.set_zlim3d([-1.0, 1.0])
    ax.set_zlabel('Z')
    ax.set_title('3D Animated Sine Wave')

    # Animation function
    def update_line(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])
        return line,

    # Creating the Animation object
    data = np.array([x, y, z])
    ani = animation.FuncAnimation(fig, update_line, frames=100, fargs=(data, line), interval=100)

    # Save the animation as an mp4 file
    ani.save(filename, writer='ffmpeg', fps=10)

# Generate and save the 3D graphics animation
generate_3d_animation(output_dir + '3d_graphics.mp4')