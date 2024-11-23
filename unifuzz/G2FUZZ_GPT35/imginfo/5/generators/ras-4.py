import numpy as np

# Generate random data for transparency
transparency_data = np.random.rand(100, 100, 4)  # 100x100 pixels with 4 channels (RGBA)

# Save transparency data to 'ras' file
np.save("./tmp/transparency.ras", transparency_data)