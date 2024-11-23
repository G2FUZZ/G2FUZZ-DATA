import numpy as np
from PIL import Image

# Create a simple animation with a bouncing ball
num_frames = 20
height, width = 100, 100
ball_radius = 10
ball_color = (255, 0, 0)  # Red ball

frames = []
for i in range(num_frames):
    frame = Image.new('RGB', (width, height), color='black')
    ball_y = int(height / 2) - abs(i - num_frames // 2) * 5
    ball_x = int(width / 2)
    
    # Draw the ball on the frame
    for y in range(max(0, ball_y - ball_radius), min(height, ball_y + ball_radius + 1)):
        for x in range(max(0, ball_x - ball_radius), min(width, ball_x + ball_radius + 1)):
            if (x - ball_x) ** 2 + (y - ball_y) ** 2 <= ball_radius ** 2:
                frame.putpixel((x, y), ball_color)
    
    frames.append(frame)

# Save the frames as an animated PNG file
frames[0].save('./tmp/bouncing_ball_animation.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)