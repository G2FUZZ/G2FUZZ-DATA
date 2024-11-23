from PIL import Image, ImageDraw

# Function to create frames for the GIF
def create_frame(frame_number, width, height, colors):
    # Create a new blank image
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    # Calculate the position of our moving square for this frame
    square_size = 50
    x_position = (frame_number * 10) % width
    y_position = (height - square_size) // 2

    # Draw a colored square that moves across the frame
    color = colors[frame_number % len(colors)]
    draw.rectangle([x_position, y_position, x_position + square_size, y_position + square_size], fill=color)

    return image

# Settings for the GIF
width, height = 400, 200
frames = 30  # Number of frames in the GIF
colors = ["red", "green", "blue", "yellow", "purple"]  # Colors for the squares

# Generate the frames
images = [create_frame(frame_number, width, height, colors) for frame_number in range(frames)]

# Save the frames as an animated GIF
output_path = './tmp/animated_loop.gif'
images[0].save(output_path, save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)

print(f"GIF saved to {output_path}")