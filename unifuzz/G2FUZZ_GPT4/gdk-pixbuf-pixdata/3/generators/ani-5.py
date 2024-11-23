import os
from PIL import Image

# Create tmp directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a single frame for the ANI file
def generate_frame(size=(32, 32), color=(0, 0, 0, 0), border_color=(0, 0, 0, 255), border_width=4):
    """
    Generate a single frame with transparency.

    :param size: The size of the image (width, height).
    :param color: The fill color (R, G, B, A).
    :param border_color: The border color (R, G, B, A).
    :param border_width: The width of the border.
    :return: A PIL Image object.
    """
    # Create an image with transparency
    image = Image.new("RGBA", size, color)
    # Draw a border
    for i in range(border_width):
        Image.Image.paste(image, Image.new("RGBA", (size[0] - i*2, size[1] - i*2), border_color), (i, i))
    return image

# Parameters for the cursor animation
frames_count = 10  # Number of frames in the animation
size = (32, 32)  # Size of each frame
border_width = 4  # Width of the border around each frame

frames = []

# Generate frames
for i in range(frames_count):
    # Calculate color for the border to create a simple animation effect
    border_color = (255, 0, 0, 255) if i % 2 == 0 else (0, 0, 255, 255)
    frame = generate_frame(size=size, border_color=border_color, border_width=border_width)
    frames.append(frame)

# Save the frames as an ANI file (using .gif for demonstration, as true .ani saving would require a more complex approach)
frames[0].save('./tmp/animated_cursor.gif',
               save_all=True,
               append_images=frames[1:],
               duration=100,  # Duration of each frame in milliseconds
               loop=0,  # Loop forever
               transparency=0,
               disposal=2)  # Restore to background color.