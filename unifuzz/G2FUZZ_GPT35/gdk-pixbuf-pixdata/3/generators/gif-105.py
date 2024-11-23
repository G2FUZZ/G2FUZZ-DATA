import os
from PIL import Image, ImageDraw

# Create a new directory to store the generated gif files
os.makedirs('./tmp/', exist_ok=True)

# Set the size of the image and number of frames
width, height = 200, 200
frames = 5

# Create frames for the gif with custom delays
images = []
delays = [100, 150, 200, 250, 300]  # Custom delays for each frame
for i in range(frames):
    new_image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    draw.text((10, 10), f"Frame {i+1}", fill='black')
    images.append(new_image)

# Set disposal method for each frame
disposal = [2, 1, 2, 3, 2]  # Different disposal methods for each frame

# Save the frames as a gif with custom delays and disposal methods
images[0].save('./tmp/extended_disposal_method.gif', save_all=True, append_images=images[1:], duration=delays, disposal=disposal)