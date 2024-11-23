import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate an example image
x = np.linspace(0, 1, 256, endpoint=True)
y = np.linspace(0, 1, 256, endpoint=True)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2

# Apply gamma correction
gamma = 0.5  # Example gamma value
gamma_corrected = np.power(Z, gamma)

# Plot the gamma-corrected image
plt.imshow(gamma_corrected, cmap='gray')
plt.axis('off')  # Don't show axes for an image

# Save the image with gamma correction information
# Note: matplotlib's plt.imsave() and plt.savefig() do not store gamma information in the PNG file.
# For demonstration purposes, we save the image without explicit gamma metadata.
# In practical applications, consider using PIL or imageio for more control over metadata including gamma.
plt.savefig(os.path.join(output_dir, "gamma_corrected_image.png"), bbox_inches='tight', pad_inches=0)

# Note: This example demonstrates generating and saving an image with gamma correction applied to its content.
# Actual gamma metadata handling requires formats and libraries that support it explicitly.