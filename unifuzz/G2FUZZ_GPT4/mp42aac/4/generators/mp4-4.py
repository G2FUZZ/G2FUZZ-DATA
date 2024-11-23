import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import imageio

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate frames for the animation
def generate_frames(num_frames=60):
    frames = []
    for angle in np.linspace(0, 360, num_frames):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X = np.linspace(-5, 5, 100)
        Y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(X, Y)
        Z = np.sin(np.sqrt(X**2 + Y**2) + np.deg2rad(angle))

        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_zlim(-1.5, 1.5)
        
        # Turn off the axes for a cleaner look
        ax.set_axis_off()

        # Save plot to a PIL image
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(image)

        plt.close(fig)
    
    return frames

# Create an animation
frames = generate_frames()
imageio.mimsave('./tmp/3d_graphics.mp4', frames, fps=20)