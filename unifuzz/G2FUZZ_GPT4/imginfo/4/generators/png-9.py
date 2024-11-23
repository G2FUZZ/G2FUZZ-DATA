from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with a white background
width, height = 800, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Text to be added
text = "9. Robust Error Detection: PNG uses CRC (Cyclic Redundancy Check) for error checking on critical chunks, ensuring the integrity of the file's data during transfer and storage."

# Use matplotlib to determine text size to wrap text accordingly
fig = plt.figure()
plt.axis([0, width, 0, height])
plt.text(0, 0, text, ha='left', wrap=True)
plt.xlim(0, width)
plt.ylim(height, 0)  # Inverted Y axis to match image coordinate system
fig.canvas.draw()

# Convert the text into an image (through a numpy array)
text_image = Image.frombytes('RGB', fig.canvas.get_width_height(), 
                             fig.canvas.tostring_rgb())

# Paste the text image onto the original image
# Assuming the text image might not perfectly fit, we might adjust or skip this step
# image.paste(text_image, (0,0))

# For simplicity, let's just save the text as a separate image
text_image_path = './tmp/error_detection_info.png'
text_image.save(text_image_path)

print(f"Image saved to {text_image_path}")