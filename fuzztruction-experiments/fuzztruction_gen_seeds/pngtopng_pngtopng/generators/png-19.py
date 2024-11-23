from PIL import Image, PngImagePlugin, ImageDraw, ImageSequence
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create multiple frames for the APNG
frames = []

# Frame generation loop
for i in range(10):  # Generate 10 frames for demonstration
    # Create a new image with palette mode for binary transparency
    image = Image.new('P', (640, 480), color='white')

    # Create a palette with 256 colors, where the first color (index 0) is transparent
    palette = []
    for j in range(256):
        if j == 0:
            palette.extend((255, 255, 255, 0))  # Making the first color fully transparent (RGBA)
        else:
            palette.extend((j, j, j))  # Grayscale for the rest

    # Ensure the palette is the correct size (768 for RGB)
    palette = palette[:768]

    image.putpalette(palette)
    image.info['transparency'] = 0  # Setting index 0 as the transparent color

    # Draw a simple shape to demonstrate transparency, moving with the frame number
    draw = ImageDraw.Draw(image)
    draw.rectangle([10+i*10, 10+i*10, 200+i*10, 200+i*10], fill=1)  # Filling with index 1, which is not transparent

    frames.append(image)

# Prepare metadata for the first frame
meta_info = PngImagePlugin.PngInfo()
meta_info.add_text('Copyright', 'Copyright 2023 by Example')
meta_info.add_text('Comment', 'Generated for demonstrating binary transparency, Adam7 interlacing, and APNG animation.')
meta_info.add_text('Creation Time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Adding Custom Chunks to the first frame
custom_chunk_key = "zTXt"
custom_chunk_data = "This is a custom chunk for demonstration.".encode("utf-8")
meta_info.add_text(custom_chunk_key, custom_chunk_data.decode("iso-8859-1"))  # Encoding and decoding to bypass PIL's handling

# Save the APNG
frames[0].save('./tmp/binary_transparency_adam7_custom_chunk_animation_example.png',
               save_all=True,
               append_images=frames[1:],
               loop=0,
               duration=100,  # Duration of each frame in milliseconds
               pnginfo=meta_info,
               interlace=1)

print('APNG with binary transparency, Adam7 interlacing, custom chunk, and animation saved to ./tmp/binary_transparency_adam7_custom_chunk_animation_example.png')