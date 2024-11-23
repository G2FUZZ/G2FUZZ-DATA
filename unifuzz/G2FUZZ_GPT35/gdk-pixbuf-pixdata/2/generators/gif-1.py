from PIL import Image, ImageDraw

# Set the dimensions and background color of the image
width, height = 200, 200
bg_color = (255, 255, 255)

# Create a new image with the specified background color
image = Image.new('RGB', (width, height), bg_color)

# Create a sequence of frames for the GIF
frames = []
for i in range(10):
    # Create a new image for each frame
    frame = image.copy()
    
    # Draw a rectangle on the frame with a different color for each frame
    draw = ImageDraw.Draw(frame)
    rect_start = i * 20
    rect_end = (i + 1) * 20
    rect_coords = [(rect_start, rect_start), (rect_end, rect_end)]
    rect_color = (i * 25, 0, 0)
    draw.rectangle(rect_coords, fill=rect_color)
    
    # Append the frame to the frames list
    frames.append(frame)

# Save the frames as a GIF file
frames[0].save('./tmp/animated.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)