import os
from PIL import Image, ImageDraw

# Create a new directory to store the generated gif files
os.makedirs('./tmp/', exist_ok=True)

# Set the size of the image and number of frames
width, height = 200, 200
frames = 5

# Create frames for the gif
images = []
for i in range(frames):
    new_image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    draw.text((10, 10), f"Frame {i+1}", fill='black')
    images.append(new_image)

# Set disposal method for each frame
disposal = [2, 2, 2, 2, 2]  # 2 means that the previous frame should be restored before displaying the current frame

# Save the frames as a gif with the specified disposal method
images[0].save('./tmp/disposal_method.gif', save_all=True, append_images=images[1:], duration=100, disposal=disposal)