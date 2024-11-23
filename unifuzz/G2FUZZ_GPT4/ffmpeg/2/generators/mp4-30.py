import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Feature text to be included in the MP4 file, now with an added MPEG-21 Part 2 Compliance feature, Standardized Branding, BIFS (Binary Format for Scenes),
# and now including Private Streams for Custom Data
features_text = """
4. **MPEG-21 Part 2 Compliance**: They are compliant with MPEG-21 Part 2 (Digital Item Declaration), allowing them to handle an array of digital objects and associated metadata more effectively, facilitating better management and distribution of digital content.

5. **BIFS (Binary Format for Scenes)**: MP4 can support BIFS, allowing for interactive and hybrid 2D/3D graphics scenes to be embedded within media content. This is particularly useful for integrating rich multimedia presentations and interactive applications.

8. **Standardized Branding**: The MP4 file format includes a mechanism for 'branding', which helps in identifying the specific capabilities or features supported by the file. This assists in ensuring compatibility across different devices and software.

9. **Compatibility and Interoperability**: MP4 files are designed to be highly compatible and interoperable, 
meaning they can be played on a wide range of devices and media players. This universal support has contributed 
to the format's popularity across different platforms and applications.

10. **Private Streams for Custom Data**: They can include private streams, which allow for embedding custom data not defined by the standard. This could be used for proprietary information, application-specific data, or additional content that enhances the main media.
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