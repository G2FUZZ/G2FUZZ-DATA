from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Function to generate a single frame with a specific color
def generate_frame(size, color):
    # Create an RGB image instead
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, size[0], size[1]], fill=color)
    return image

# Define the size of the GIF
size = (100, 100)

# Define a palette of 256 colors (8-bit, 3 channels RGB but reduced to 256 colors)
palette = [((i*3) % 256, (i*5) % 256, (i*7) % 256) for i in range(256)]

# Generate frames using the colors from the palette
frames = [generate_frame(size, palette[i % len(palette)]) for i in range(len(palette))]

# Convert frames to use the same palette
frames_converted = []
for i, frame in enumerate(frames):
    # Quantize without specifying a palette, allowing PIL to create an optimal one
    frame_converted = frame.quantize(colors=256)
    frames_converted.append(frame_converted)

# Save the frames as a GIF
frames_converted[0].save('./tmp/indexed_color_palette_demo.gif',
                         save_all=True, append_images=frames_converted[1:], optimize=False, duration=100, loop=0)