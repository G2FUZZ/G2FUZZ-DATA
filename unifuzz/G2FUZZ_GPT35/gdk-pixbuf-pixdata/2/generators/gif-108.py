from PIL import Image, ImageDraw

# Define the size of the image and number of frames
width, height = 200, 200
num_frames = 10

# Create a list of colors for the frames
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), 
          (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 255, 255), 
          (128, 128, 128), (0, 0, 0)]

# Create a new image sequence with a smooth color transition
images = []
for i in range(num_frames):
    image = Image.new('RGB', (width, height), color=colors[i % len(colors)])
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (width, height)], outline=None)
    images.append(image)

# Save the image sequence as an animated GIF
images[0].save('./tmp/complex_animation.gif', save_all=True, append_images=images[1:], format='GIF', duration=200, loop=0)