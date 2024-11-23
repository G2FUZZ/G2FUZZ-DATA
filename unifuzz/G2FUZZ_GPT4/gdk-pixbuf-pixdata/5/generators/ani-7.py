from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_frame_image(size, color):
    """Create a single frame image with specified size and color."""
    image = Image.new('RGBA', size, color)
    return image

def save_ani_sequence(frames, durations, filename):
    """
    Save a sequence of frames as an .ani file (in reality, saves as a .gif for demonstration).
    The durations specify the display time for each frame in the sequence.
    """
    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        format='GIF'
    )

def generate_step_sequence_animation():
    # Parameters for the animation
    frame_size = (64, 64)
    steps = [
        ('red', 500),  # color, display duration in milliseconds
        ('green', 500),
        ('blue', 500),
        ('yellow', 500),
    ]

    frames = []
    durations = []

    # Generate frames based on the step sequence
    for color, duration in steps:
        frame = create_frame_image(frame_size, color)
        frames.append(frame)
        durations.append(duration)
    
    # Save the animation sequence
    ani_filename = os.path.join(output_dir, 'step_sequence_animation.ani')
    save_ani_sequence(frames, durations, ani_filename)

# Generate the animation
generate_step_sequence_animation()