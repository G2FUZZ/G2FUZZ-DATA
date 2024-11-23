import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Feature text to be included in the MP4 file, now including the new feature
features_text = """
9. **Compatibility and Interoperability**: MP4 files are designed to be highly compatible and interoperable, 
meaning they can be played on a wide range of devices and media players. This universal support has contributed 
to the format's popularity across different platforms and applications.
1. **Efficient Encoding for Various Media Types**: MP4 files can efficiently encode not just video and audio, but also still images and text, making them a comprehensive container for multimedia content.
8. **Auxiliary Data**: MP4 files can store auxiliary data such as depth maps or additional non-visual information related to the main media content. This is useful for advanced imaging techniques, including computational photography and augmented reality applications.
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