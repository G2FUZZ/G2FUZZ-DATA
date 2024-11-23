import numpy as np
from PIL import Image, ImageFilter

# Create a more complex numpy array (e.g., a gradient image)
gradient_data = np.zeros((200, 200, 3), dtype=np.uint8)
gradient_data[:, :100] = [255, 0, 0]  # Left side is red
gradient_data[:, 100:] = [0, 0, 255]  # Right side is blue

# Convert the numpy array to an image
gradient_image = Image.fromarray(gradient_data)

# Apply a blur filter to the image
blurred_image = gradient_image.filter(ImageFilter.BLUR)

# Save the blurred image as a PNG file with a custom file name
blurred_image.save('./tmp/blurred_gradient_image.png')

print("PNG file with a color filter applied and saved successfully.")