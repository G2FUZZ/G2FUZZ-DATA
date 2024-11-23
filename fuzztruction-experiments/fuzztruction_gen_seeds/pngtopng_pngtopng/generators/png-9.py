import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image to demonstrate PNG's robustness to file corruption
# Using a basic plot for simplicity

# Creating a simple plot
plt.figure(figsize=(6, 4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sin(x)')
plt.title('Robustness to File Corruption: PNG Format')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

# Save the plot as a PNG file
output_path = os.path.join(output_dir, 'robustness_to_file_corruption.png')
plt.savefig(output_path)
plt.close()

print(f"Image saved at: {output_path}")