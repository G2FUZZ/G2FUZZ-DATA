import numpy as np
import matplotlib.pyplot as plt

def save_bmp_file(file_path, image_data):
    image_data = np.clip(image_data, 0, 255).astype(np.uint8)
    plt.imsave(file_path, image_data)

# Create a simple 100x100 red image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[:, :, 0] = 255  # Set red channel to 255

# Save the image as a BMP file
save_bmp_file('./tmp/red_image.bmp', image_data)