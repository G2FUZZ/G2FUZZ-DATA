import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with varying brightness
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Create a gradient from left (black) to right (white)
# For sRGB, we use a 3-channel image
for x in range(width):
    color_value = x
    image[:, x, :] = [color_value, color_value, color_value]  # RGB

# Apply gamma correction for sRGB
def srgb_gamma_correction(channel):
    # Normalize the pixel values
    channel = channel / 255.0
    # Apply sRGB gamma correction
    channel = np.where(channel <= 0.0031308,
                       channel * 12.92,
                       1.055 * np.power(channel, 1/2.4) - 0.055)
    return np.array(channel * 255, dtype='uint8')

image_srgb_gamma_corrected = np.zeros_like(image)
for i in range(3):  # Apply the correction to each channel
    image_srgb_gamma_corrected[:, :, i] = srgb_gamma_correction(image[:, :, i])

# Save the original and sRGB gamma-corrected images
plt.imsave(f'{output_dir}original_rgb.png', image)
plt.imsave(f'{output_dir}srgb_gamma_corrected.png', image_srgb_gamma_corrected)