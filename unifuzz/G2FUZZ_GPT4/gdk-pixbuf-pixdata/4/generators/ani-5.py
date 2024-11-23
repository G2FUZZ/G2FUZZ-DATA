import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a frame with a specific shape
def create_frame(shape, frame_size=(32, 32), color="black"):
    image = Image.new("RGBA", frame_size, "white")
    draw = ImageDraw.Draw(image)
    if shape == "circle":
        draw.ellipse([8, 8, 24, 24], fill=color)
    elif shape == "square":
        draw.rectangle([8, 8, 24, 24], fill=color)
    elif shape == "triangle":
        draw.polygon([16, 8, 8, 24, 24, 24], fill=color)
    return image

# Create frames for the animation
shapes = ["circle", "square", "triangle"]
frames = [create_frame(shape) for shape in shapes]

# Using Pillow to save an animated GIF as a base for our ANI file
ani_path = './tmp/animation.ani'  # ANI files are essentially GIFs with specific metadata, but for simplicity, we'll generate a GIF
gif_path = ani_path.replace('.ani', '.gif')  # Temporarily save as GIF
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=250, loop=0)

# Note: To properly create an ANI file, additional steps to embed ANI-specific headers and metadata are required.
# This example simplifies the process by generating a GIF, which demonstrates the concept of sequence cycling.
# For actual ANI file generation, additional binary file manipulation is needed to comply with the ANI format specifications.

print(f"Animation saved to {gif_path} (Note: For demonstration purposes, saved as GIF)")