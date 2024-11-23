import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate frames for the ANI file
frames = []
for i in range(5):  # Generate 5 frames for demonstration
    frame = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
    draw = ImageDraw.Draw(frame)
    # Draw a simple shape that changes over frames
    draw.ellipse((i*4, i*4, i*4 + 20, i*4 + 20), fill='blue')
    frames.append(frame)

# Save frames as an animated GIF first (Pillow doesn't support saving as .ani)
ani_path = './tmp/animated_cursor.gif'
frames[0].save(
    ani_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,  # duration for each frame in ms
    loop=0,  # loop forever
    transparency=0,
    disposal=2  # Restore to background color.
)

# ANI files are essentially a Microsoft-specific format not natively supported by PIL or common Python libraries.
# To create an actual .ani file, additional steps involving a direct conversion or using specialized software would be needed.
# For simplicity and demonstration purposes, this example uses a GIF file to simulate the animation.
# If you need to work with real .ANI files, consider using software that can convert GIFs to ANI format or work with the .ani format directly.