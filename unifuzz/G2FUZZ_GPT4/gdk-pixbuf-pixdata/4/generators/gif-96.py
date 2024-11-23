from PIL import Image, ImageDraw, ImagePalette
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a GIF with a moving circle that changes color
def create_moving_circle_gif(output_path):
    width, height = 200, 200
    palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
               (255, 255, 0), (255, 0, 255), (0, 255, 255),
               (255, 255, 255), (0, 0, 0)]
    num_frames = 20

    # Generate a series of frames
    frames = []
    for i in range(num_frames):
        # Create a new image with a black background
        img = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Calculate the circle's position and color
        position = (width * i / num_frames, height / 2)
        radius = 20
        color = palette[i % len(palette)]

        # Draw the circle
        draw.ellipse([position[0] - radius, position[1] - radius,
                      position[0] + radius, position[1] + radius], fill=color)
        
        frames.append(img)

    # Save the frames as a GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

# Create and save the GIF
output_path = os.path.join(output_dir, "moving_circle.gif")
create_moving_circle_gif(output_path)

print(f"GIF saved to {output_path}")