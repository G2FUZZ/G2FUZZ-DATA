import os
from PIL import Image, ImageDraw
import ffmpeg

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a simple sequence of images to use as video frames
frame_count = 10
frame_size = (320, 240)
for i in range(frame_count):
    img = Image.new('RGB', frame_size, (i*25, i*10, i*5))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), f"Frame {i}", fill=(255, 255, 255))
    img.save(f"./tmp/frame_{i:03}.png")

# Use ffmpeg to compile the images into an FLV video
(
    ffmpeg
    .input('./tmp/frame_%03d.png', framerate=2)
    .output('./tmp/output.flv', vcodec='flv')
    .run()
)

# Clean up images
for i in range(frame_count):
    os.remove(f"./tmp/frame_{i:03}.png")

# Note: This code does not add navigation markers to the FLV file.
# Adding navigation markers involves manipulating the FLV file's metadata or using specialized video editing tools.