import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageFont

# Function to add text overlay to a frame
def add_text_overlay(frame, text):
    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 255, 255), font=font)
    return np.array(img_pil)

# Create frames for the gif with text overlay
frames = []
for i in range(10):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, :, i % 3] = 255
    frame_with_text = add_text_overlay(frame, f"Frame {i+1}")  # Add text overlay with frame number
    frames.append(frame_with_text)

# Save frames with text overlay as gif
imageio.mimsave('./tmp/complex_animation.gif', frames, duration=0.5)