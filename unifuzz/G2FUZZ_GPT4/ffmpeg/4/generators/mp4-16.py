import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os
from itertools import product, combinations
from cryptography.fernet import Fernet

# Function to encrypt the MP4 file
def encrypt_file(input_file, output_file, key):
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Function to draw a cube
def draw_cube(ax, position, size=1.0, color='blue', alpha=1.0):
    r = [-size/2, size/2]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s+position, e+position), color=color, alpha=alpha)

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

# Create a writer object
temp_video_path = './tmp/rotating_cube_temp.mp4'
final_video_path = './tmp/rotating_cube_encrypted.mp4'
writer = imageio.get_writer(temp_video_path, fps=20)

for angle in angles:
    ax.view_init(30, angle)
    plt.draw()
    # Capture the current plot as an image frame
    frame = fig.canvas.tostring_rgb()
    image = np.frombuffer(frame, dtype='uint8')
    w, h = fig.canvas.get_width_height()
    image = image.reshape((h, w, 3))
    writer.append_data(image)
    ax.cla()  # Clear the plot for the next frame
    draw_cube(ax, (0, 0, 0), size=1.0, color='skyblue', alpha=0.5)  # Redraw the cube

# Close the writer to finalize the video file
writer.close()

# Generate a key for encryption
key = Fernet.generate_key()

# Encrypt the MP4 file
encrypt_file(temp_video_path, final_video_path, key)

# Optionally, remove the original unencrypted file
os.remove(temp_video_path)

# Output the encryption key for decryption
print(f"Encryption Key: {key.decode()}")