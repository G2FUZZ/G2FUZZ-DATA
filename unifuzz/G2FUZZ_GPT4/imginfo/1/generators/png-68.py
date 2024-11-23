from PIL import Image, ImageDraw, ImageFont
from apng import APNG
import os

def create_frame(width, height, bg_color, fg_color, text, frame_number):
    """
    Create a single frame with a gradient background, a colored square, and overlay text.
    """
    # Create an image with gradient background
    image = Image.new('RGBA', (width, height), bg_color)
    for i in range(height):
        gradient_color = (
            bg_color[0] + int((fg_color[0] - bg_color[0]) * i / height),
            bg_color[1] + int((fg_color[1] - bg_color[1]) * i / height),
            bg_color[2] + int((fg_color[2] - bg_color[2]) * i / height),
            255
        )
        ImageDraw.Draw(image).line([(0, i), (width, i)], fill=gradient_color)
    
    # Draw a square in the center
    square_size = 50
    square_left = (width - square_size) / 2
    square_top = (height - square_size) / 2
    square_fill = (
        fg_color[0],
        fg_color[1],
        fg_color[2],
        255
    )
    ImageDraw.Draw(image).rectangle(
        [square_left, square_top, square_left+square_size, square_top+square_size],
        fill=square_fill
    )
    
    # Overlay text
    try:
        font = ImageFont.truetype("arial.ttf", 15)  # Adjust path as needed
    except IOError:
        font = ImageFont.load_default()
    text_width, text_height = ImageDraw.Draw(image).textsize(text, font=font)
    ImageDraw.Draw(image).text(
        ((width - text_width) / 2, height - text_height - 10),
        text,
        font=font,
        fill=(0, 0, 0, 255)
    )
    
    # Save the frame
    frame_path = f'./tmp/frame{frame_number}.png'
    image.save(frame_path)
    return frame_path

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the animation
frame_count = 10
width, height = 100, 100
frames = []

# Generate frames
for i in range(frame_count):
    bg_color = (255, 255 - i * 25, 255 - i * 25)  # From white to red
    fg_color = (0, 0, i * 25)  # From black to blue
    text = f"Frame {i + 1}"
    frame_path = create_frame(width, height, bg_color, fg_color, text, i)
    frames.append(frame_path)

# Create an animated PNG from the frames
apng_path = './tmp/animated_complex.png'
APNG.from_files(frames, delay=100).save(apng_path)

# Optionally, clean up the temporary frame files
for frame in frames:
    os.remove(frame)

print(f"Animated PNG saved at: {apng_path}")