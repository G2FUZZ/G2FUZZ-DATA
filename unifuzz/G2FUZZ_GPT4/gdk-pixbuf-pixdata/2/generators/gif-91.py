from PIL import Image, ImageDraw
import os

def generate_concentric_circles_gif(output_dir, file_name, width, height, num_frames):
    """
    Generates an animated GIF with concentric circles that change color and expand over time.

    Args:
    - output_dir: Directory to save the GIF file.
    - file_name: Name of the GIF file.
    - width: Width of each frame.
    - height: Height of each frame.
    - num_frames: Number of frames in the animation.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parameters for the concentric circles
    max_diameter = min(width, height) * 0.9
    num_circles = 10  # Number of concentric circles

    frames = []  # List to hold the frames of the animation
    for i in range(num_frames):
        img = Image.new('RGB', (width, height), 'white')  # Create a new image with white background
        draw = ImageDraw.Draw(img)

        for j in range(num_circles):
            # Calculate the diameter of the current circle
            diameter = ((i + j) % num_frames) / num_frames * max_diameter
            # Calculate the bounding box of the current circle
            left_up = ((width - diameter) / 2, (height - diameter) / 2)
            right_down = ((width + diameter) / 2, (height + diameter) / 2)
            # Calculate the color of the current circle
            color = ((255 * (i + j) // num_frames) % 255, 125, (255 * (num_frames - (i + j)) // num_frames) % 255)
            # Draw the circle
            draw.ellipse([left_up, right_down], outline=color)

        frames.append(img)  # Add the frame to the list

    # Save the frames as an animated GIF
    output_path = os.path.join(output_dir, file_name)
    frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

    print(f"Animated GIF saved at: {output_path}")

# Example usage
output_dir = './tmp/'
file_name = 'animated_concentric_circles.gif'
width, height = 300, 300  # Size of each frame
num_frames = 30  # Number of frames in the animation
generate_concentric_circles_gif(output_dir, file_name, width, height, num_frames)