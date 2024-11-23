from PIL import Image, ImageDraw

# Create a list to store frames
frames = []

# Set the size of the image
img_width = 200
img_height = 200

# Create 10 frames for the GIF
for i in range(10):
    # Create a new image with a white background
    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw a rectangle that moves across the image
    rect_width = 20
    rect_height = 20
    rect_x = i * 20
    rect_y = img_height // 2 - rect_height // 2
    draw.rectangle([rect_x, rect_y, rect_x + rect_width, rect_y + rect_height], fill='black')
    
    # Append the frame to the list of frames
    frames.append(img)

# Save the frames as a GIF
frames[0].save('./tmp/looping.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)