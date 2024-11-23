import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_3d_animation():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    # Initial setup for the plot, returns a tuple of line objects.
    def init():
        line, = ax.plot([], [], [], lw=2)
        return line,

    # Number of frames
    num_frames = 100

    # Generation of data for each frame
    def update(frame):
        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        t = np.linspace(0, 2*np.pi, 100)
        x = np.sin(t + 0.1*frame)
        y = np.cos(t + 0.1*frame)
        z = np.sin(t + 0.1*frame)
        line = ax.plot3D(x, y, z, 'gray')
        return line  # Return the line object

    # Creating the animation
    ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=False)

    # Save the animation
    ani.save('./tmp/3d_animation.mp4', writer='ffmpeg', fps=20)

if __name__ == "__main__":
    generate_3d_animation()