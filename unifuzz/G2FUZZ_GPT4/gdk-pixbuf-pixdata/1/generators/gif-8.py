from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a GIF demonstrating fixed spatial resolution
def create_gif(filename, scale=1):
    width, height = 200, 100  # Original dimensions
    frames = []  # List to hold frames for the GIF

    # Adjust width and height based on scale
    scaled_width = int(width * scale)
    scaled_height = int(height * scale)

    # Generate 10 frames with changing text to show as a simple animation
    for i in range(10):
        # Create a new frame with the specified dimensions and white background
        frame = Image.new('RGB', (scaled_width, scaled_height), 'white')
        draw = ImageDraw.Draw(frame)
        
        # Add text to the frame
        text = f'Frame {i+1}'
        # Use a default font instead of arial.ttf
        font = ImageFont.load_default()
        textwidth, textheight = draw.textsize(text, font=font)
        textx = (scaled_width - textwidth) / 2
        texty = (scaled_height - textheight) / 2
        draw.text((textx, texty), text, fill='black', font=font)
        
        # Draw a simple shape
        shape = [(20 * scale, 20 * scale), (180 * scale, 80 * scale)]
        draw.ellipse(shape, outline ="red")
        
        # Resize frame if scaled
        if scale != 1:
            frame = frame.resize((scaled_width, scaled_height), Image.ANTIALIAS)
        
        frames.append(frame)

    # Save the frames as a GIF
    frames[0].save(f'./tmp/{filename}.gif', save_all=True, append_images=frames[1:], optimize=False, duration=200, loop=0)

# Create an original size GIF
create_gif('original_resolution')

# Create a scaled version of the GIF to demonstrate loss of clarity upon scaling
create_gif('scaled_resolution', scale=2)  # Scale by 2x