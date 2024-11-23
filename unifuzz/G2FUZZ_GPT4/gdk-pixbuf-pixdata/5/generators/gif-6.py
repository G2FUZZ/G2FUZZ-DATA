from PIL import Image, ImageDraw

# Define the size of the image
width, height = 200, 200

# Define the colors to be used (global color table)
colors = {
    "background": (0, 0, 0),
    "square": (255, 0, 0)  # Red square
}

# Function to create a frame
def create_frame(position):
    # Create a new image with a black background
    img = Image.new("RGB", (width, height), colors["background"])
    draw = ImageDraw.Draw(img)
    
    # Draw a red square at the specified position
    square_size = 50
    top_left = (position, position)
    bottom_right = (position + square_size, position + square_size)
    draw.rectangle([top_left, bottom_right], fill=colors["square"])
    
    return img

# Generate frames
frames = []
for i in range(0, width, 10):
    frame = create_frame(i)
    frames.append(frame)

# Save the frames as a GIF
output_path = './tmp/moving_square.gif'
frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0, palette=[0, 0, 0, 255, 0, 0])

print(f"GIF saved at {output_path}")