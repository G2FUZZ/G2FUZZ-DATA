from PIL import Image, ImageDraw

# Create a list to store frames
frames = []

# Set up the dimensions and background color
width, height = 200, 200
bg_color = (255, 255, 255)

# Create 10 frames with different colors
for i in range(10):
    # Create a new image and drawing context
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Draw a rectangle with a different color in each frame
    rect_start = (i*10, i*10)
    rect_end = (width - i*10, height - i*10)
    rect_color = (255 - i*20, 0, 0)
    draw.rectangle([rect_start, rect_end], fill=rect_color)
    
    # Append the frame to the list
    frames.append(image)

# Save the frames as a gif file
save_path = './tmp/looping_gif.gif'
frames[0].save(save_path, save_all=True, append_images=frames[1:], loop=0, duration=200)