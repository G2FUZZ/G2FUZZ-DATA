from PIL import Image, ImageSequence

# Create a list of frames for the gif
frames = []
for i in range(10):
    frame = Image.new('RGB', (100, 100), color=(i*25, 0, 0))
    frames.append(frame)

# Save the frames as a gif with optimized palette and duration for each frame
frames[0].save('./tmp/complex.gif', save_all=True, append_images=frames[1:], format='GIF', optimize=True, duration=100, loop=0)