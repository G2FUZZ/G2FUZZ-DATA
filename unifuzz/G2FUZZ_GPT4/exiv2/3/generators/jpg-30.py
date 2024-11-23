from PIL import Image, ImageDraw
import os
import random
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 256, 256

# Size of each block
block_size = 32

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Initialize maze grid, 0 for wall, 1 for path
maze_size = int(width / block_size)
maze = np.zeros((maze_size, maze_size), dtype=np.int8)

# Function to create a maze using Depth-First Search algorithm
def make_maze(x, y):
    dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    random.shuffle(dir)
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze_size and 0 <= ny < maze_size and maze[ny][nx] == 0:
            if (x, y) == (nx, ny) or np.sum(maze[max(0, ny-1):min(maze_size, ny+2), max(0, nx-1):min(maze_size, nx+2)]) == 0:
                maze[y][x] = 1
                maze[ny][nx] = 1
                make_maze(nx, ny)

# Function to create a grid image with a maze overlay
def create_grid_maze_image():
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw grid
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            draw.rectangle([x, y, x+block_size, y+block_size], fill=random_color(), outline=None)
    
    # Generate and draw maze
    make_maze(random.randint(0, maze_size-1), random.randint(0, maze_size-1))
    for y in range(maze_size):
        for x in range(maze_size):
            if maze[y][x] == 1:
                mx, my = x * block_size, y * block_size
                draw.rectangle([mx, my, mx+block_size, my+block_size], fill=(255, 255, 255), outline=None)
    
    return image

# Create and save images
for i in range(3):  # Example: Creating and saving 3 images
    image_path = f'./tmp/maze_overlay_example_{i}.jpg'
    img = create_grid_maze_image()
    img.save(image_path)
    print(f"Image {i} saved to {image_path}")