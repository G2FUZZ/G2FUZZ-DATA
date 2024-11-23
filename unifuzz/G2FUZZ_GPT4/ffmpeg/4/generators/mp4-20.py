import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os
from itertools import product, combinations

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Function to draw a cube
def draw_cube(ax, position, size=1.0, color='blue', alpha=1.0):
    r = [-size/2, size/2]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s+position, e+position), color=color, alpha=alpha)

def draw_vector_graphics(ax):
    # Add vector graphics (e.g., an arrow)
    ax.quiver(0, 0, 0, 1, 1, 1, length=0.5, color='red')

def add_text(ax, frame_number):
    # Add text (e.g., frame number)
    ax.text2D(0.05, 0.95, f"Frame: {frame_number}", transform=ax.transAxes, color='green')

# Prepare the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Hide axes
ax.set_axis_off()

# Variables for animation
n_frames = 100
rotation_angle = 360 / n_frames
angles = np.linspace(0, 360, n_frames, endpoint=False)

# Create a writer object with the ISOBMFF format
writer = imageio.get_writer('./tmp/rotating_cube_rich_media.mp4', fps=20, format='FFMPEG', codec='libx264', pixelformat='yuv420p')

for i, angle in enumerate(angles):
    ax.view_init(30, angle)
    plt.draw()
    draw_cube(ax, (0, 0, 0), size=1.0, color='skyblue', alpha=0.5)
    draw_vector_graphics(ax)
    add_text(ax, i+1)
    # Capture the current plot as an image frame
    frame = fig.canvas.tostring_rgb()
    image = np.frombuffer(frame, dtype='uint8')
    w, h = fig.canvas.get_width_height()
    image = image.reshape((h, w, 3))
    writer.append_data(image)
    ax.cla()  # Clear the plot for the next frame

# Close the writer to finalize the video file
writer.close()