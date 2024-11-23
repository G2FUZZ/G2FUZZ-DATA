import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

# Create a directory for the output if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Text to be added including the new feature description
text = """
10. **Compatibility**: Designed with broad compatibility in mind, MP4 files can be played on a wide range of devices and platforms, from smartphones and tablets to desktop computers and TVs.
3. **Alternate Track Support**: They can include alternate tracks, allowing the storage of multiple versions of a track within a single file. This can be used for different language versions of an audio track or different resolution versions of a video track.
10. **Cover Art**: MP4 files can include cover art images, which are displayed by media players as the visual representation of the video or audio content, enhancing the user interface experience.
"""

# Create an image with PIL
width, height = 800, 600  # Width and height of the image
background_color = (255, 255, 255)  # White background
font_color = (0, 0, 0)  # Black font color
font_size = 24
image = Image.new("RGB", (width, height), color=background_color)
draw = ImageDraw.Draw(image)

# Use a default font provided by PIL
font = ImageFont.load_default()

draw.multiline_text((10, 10), text, fill=font_color, font=font)

# Convert PIL image to an array
frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used
fps = 1  # Frame per second, adjust according to your needs
output_filename = os.path.join(output_dir, "output_with_cover_art_feature.mp4")
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Write the frame into the file 'output_with_cover_art_feature.mp4'
out.write(frame)

# Release everything when the job is finished
out.release()

print(f"MP4 file with Cover Art feature has been saved to {output_filename}")