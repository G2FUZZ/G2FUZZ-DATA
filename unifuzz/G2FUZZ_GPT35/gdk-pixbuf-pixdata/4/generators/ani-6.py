import numpy as np
import imageio

# Create a random image for demonstration
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Save the image as an animated file with compression
output_file = './tmp/compressed_animation.gif'  # Specify the output file format as GIF
imageio.mimsave(output_file, [image_data]*10, duration=0.2, palettesize=256)