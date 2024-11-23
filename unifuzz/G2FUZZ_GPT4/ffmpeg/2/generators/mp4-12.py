import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Feature text to be included in the MP4 file with an additional feature
features_text = """
3. **Scene Description and Navigation**: MP4 files can include scene description and navigation data, enabling complex interactive media experiences. This includes virtual reality (VR) content and interactive menus for enhanced user engagement.

9. **Compatibility and Interoperability**: MP4 files are designed to be highly compatible and interoperable, 
meaning they can be played on a wide range of devices and media players. This universal support has contributed 
to the format's popularity across different platforms and applications.
"""

# Create an image with the specified text
def text_to_image(text, img_size=(1920, 1080), bg_color=(255, 255, 255), font_size=24, font_color=(0, 0, 0)):
    font = ImageFont.load_default()  # Use PIL's default font
    img = Image.new('RGB', img_size, color=bg_color)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, fill=font_color, font=font)
    return np.array(img)

# Convert the text to an image
frame = text_to_image(features_text)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/features_video.mp4', fourcc, 1.0, (frame.shape[1], frame.shape[0]))

# Write the frame multiple times to create a short video
for _ in range(60):  # Creates a 60-second video at 1 frame per second
    out.write(frame)

# Release everything when job is finished
out.release()