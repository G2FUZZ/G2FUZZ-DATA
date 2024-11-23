import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def generate_3d_animation():
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

    # Save the animation
    ani.save('./tmp/3d_graphics_animation.mp4', writer='ffmpeg', fps=30)

generate_3d_animation()