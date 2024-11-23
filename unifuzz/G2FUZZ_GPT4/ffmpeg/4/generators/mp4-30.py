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

# Variables for animation
n_frames = 100
rotation_angle = 360 / n_frames

# Simplify writer parameters for troubleshooting
writer = imageio.get_writer('./tmp/rotating_cube.mp4', fps=20)

for angle in np.linspace(0, 360, n_frames, endpoint=False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_axis_off()
    
    draw_cube(ax, (0, 0, 0), size=1.0, color='skyblue', alpha=0.5)
    ax.view_init(30, angle)
    
    # Capture the current plot as an image frame
    fig.canvas.draw()  # This was changed from plt.draw()
    frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    w, h = fig.canvas.get_width_height()
    image = frame.reshape((h, w, 3))
    writer.append_data(image)
    
    plt.close(fig)  # Close the figure properly after each iteration

# Close the writer to finalize the video file
writer.close()