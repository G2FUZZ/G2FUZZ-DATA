import os

def create_pbm(filename, width, height):
    """Create a simple PBM image."""
    header = f"P1\n{width} {height}\n"
    data = []
    # Generate checkerboard pattern
    for i in range(height):
        row = []
        for j in range(width):
            row.append('0' if (i+j) % 2 == 0 else '1')
        data.append(' '.join(row))
    with open(filename, 'w') as f:
        f.write(header + '\n'.join(data))

def create_pgm(filename, width, height):
    """Create a simple PGM image."""
    max_val = 255
    header = f"P2\n{width} {height}\n{max_val}\n"
    data = []
    # Gradient from black to white
    for i in range(height):
        row = [str((i * max_val) // height)] * width
        data.append(' '.join(row))
    with open(filename, 'w') as f:
        f.write(header + '\n'.join(data))

def create_ppm(filename, width, height):
    """Create a simple PPM image."""
    max_val = 255
    header = f"P3\n{width} {height}\n{max_val}\n"
    data = []
    # Generate image with red, green, blue vertical stripes
    stripe_width = width // 3
    for i in range(height):
        row = []
        for j in range(stripe_width):
            row.append("255 0 0")  # Red
        for j in range(stripe_width, 2 * stripe_width):
            row.append("0 255 0")  # Green
        for j in range(2 * stripe_width, width):
            row.append("0 0 255")  # Blue
        data.append(' '.join(row))
    with open(filename, 'w') as f:
        f.write(header + '\n'.join(data))

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create PBM file
create_pbm('./tmp/test_image.pbm', 10, 10)
# Create PGM file
create_pgm('./tmp/test_image.pgm', 10, 10)
# Create PPM file
create_ppm('./tmp/test_image.ppm', 30, 10)