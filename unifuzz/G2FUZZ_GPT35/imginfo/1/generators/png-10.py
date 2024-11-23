import matplotlib.pyplot as plt
import numpy as np
import os

# Create a directory to store the generated PNG files
os.makedirs('./tmp/', exist_ok=True)

# Generate frames for the animation
for i in range(5):
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))

    # Save each frame as a PNG file
    plt.savefig(f'./tmp/frame_{i}.png')
    plt.close()