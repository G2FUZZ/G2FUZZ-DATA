import os
import math

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def draw_circle(data, cx, cy, radius, value):
    """Draws a circle on the provided data matrix."""
    for x in range(cx - radius, cx + radius + 1):
        for y in range(cy - radius, cy + radius + 1):
            if (x - cx)**2 + (y - cy)**2 <= radius**2:
                data[y][x] = value

def draw_square(data, top_left_x, top_left_y, side_length, value):
    """Draws a square on the provided data matrix."""
    for x in range(top_left_x, top_left_x + side_length):
        for y in range(top_left_y, top_left_y + side_length):
            data[y][x] = value

def create_pbm(filename, width, height, shapes):
    """Creates a PBM file with specified shapes."""
    data = [['0' for _ in range(width)] for _ in range(height)]
    for shape in shapes:
        if shape['type'] == 'circle':
            draw_circle(data, shape['x'], shape['y'], shape['radius'], '1')
        elif shape['type'] == 'square':
            draw_square(data, shape['x'], shape['y'], shape['side'], '1')

    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        for row in data:
            f.write(" ".join(row) + "\n")

def create_pgm(filename, width, height, gradient=False):
    """Creates a PGM file with optional gradient."""
    data = [['0' for _ in range(width)] for _ in range(height)]
    if gradient:
        for y in range(height):
            for x in range(width):
                data[y][x] = str(int((x / width) * 255))

    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for row in data:
            f.write(" ".join(row) + "\n")

def create_ppm(filename, width, height, pattern=False):
    """Creates a PPM file with optional color pattern."""
    data = [['0 0 0' for _ in range(width)] for _ in range(height)]
    if pattern:
        for y in range(height):
            for x in range(width):
                r = int((x / width) * 255)
                g = int((y / height) * 255)
                b = int(((x + y) / (width + height)) * 255)
                data[y][x] = f"{r} {g} {b}"

    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for row in data:
            f.write(" ".join(row) + "\n")

# Example usage
create_pbm('./tmp/complex_example.pbm', 100, 100, [
    {'type': 'circle', 'x': 50, 'y': 50, 'radius': 30},
    {'type': 'square', 'x': 20, 'y': 70, 'side': 20}
])
create_pgm('./tmp/complex_example.pgm', 100, 100, gradient=True)
create_ppm('./tmp/complex_example.ppm', 100, 100, pattern=True)

print("Complex PNM files generated successfully.")