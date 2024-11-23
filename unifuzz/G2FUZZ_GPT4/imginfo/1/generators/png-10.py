from PIL import Image
from apng import APNG
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create two frames for the animation
frame1 = Image.new('RGBA', (100, 100), (255, 0, 0, 255))  # Red square
frame2 = Image.new('RGBA', (100, 100), (0, 0, 255, 255))  # Blue square

# Save frames as temporary PNG files
frame1_path = './tmp/frame1.png'
frame2_path = './tmp/frame2.png'
frame1.save(frame1_path)
frame2.save(frame2_path)

# Create an animated PNG from the frames
apng_path = './tmp/animated.png'
APNG.from_files([frame1_path, frame2_path], delay=500).save(apng_path)

# Optionally, clean up the temporary frame files
os.remove(frame1_path)
os.remove(frame2_path)

print(f"Animated PNG saved at: {apng_path}")