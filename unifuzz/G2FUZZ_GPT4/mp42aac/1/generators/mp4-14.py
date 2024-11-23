import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import imageio

# Prepare the output directory
output_dir = './tmp/'
output_filename = '3d_dynamic_graphics.mp4'
output_path = os.path.join(output_dir, output_filename)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_dynamic_frame(angle, amplitude):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)
    Z = amplitude * np.sin(np.sqrt(X**2 + Y**2) + np.deg2rad(angle))
    
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-2 * amplitude, 2 * amplitude])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    
    plt.close(fig)
    return image

# Generate frames with dynamic amplitude changes
angles = np.linspace(0, 360, 60)  # Generate 60 frames for a 360-degree rotation
amplitudes = np.linspace(1, 2, 60)  # Dynamically change amplitude from 1 to 2
frames = [generate_dynamic_frame(angle, amplitude) for angle, amplitude in zip(angles, amplitudes)]

# Save frames as an MP4 file
imageio.mimsave(output_path, frames, fps=10)