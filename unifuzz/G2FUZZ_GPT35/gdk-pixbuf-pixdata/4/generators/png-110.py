import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Creating a noisy image with text overlay
width, height = 200, 200
image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = np.where(image < 50, 0, image)  # Applying threshold to add some structure

# Adding text overlay
image_pil = Image.fromarray(image)
draw = ImageDraw.Draw(image_pil)
font = ImageFont.load_default()  # Using a default font
text = "Generated Image"
draw.text((width//4, height//2), text, fill=(255, 255, 255), font=font)

# Applying gamma correction
gamma = 2.2
image_gamma_corrected = (image / 255.0) ** (1 / gamma) * 255
image_gamma_corrected = image_gamma_corrected.astype(np.uint8)

# Saving the image with text overlay and gamma correction
plt.imsave('./tmp/complex_image.png', image_gamma_corrected)