import os

def ensure_dir(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)

def generate_pbm(file_path, width, height):
    """Generate a simple PBM file with an alternating pattern."""
    header = "P1\n# This is a complex PBM file\n{} {}\n".format(width, height)
    pattern = [(0, 1) if (x + y) % 2 == 0 else (1, 0) for y in range(height) for x in range(width)]
    data = "\n".join([" ".join([str(bit) for bit in row]) for row in zip(*[iter(pattern)]*width)])
    with open(file_path, 'w') as file:
        file.write(header + data)

def generate_pgm(file_path, width, height):
    """Generate a PGM file with a vertical gradient."""
    header = "P2\n# This is a complex PGM file\n{} {}\n255\n".format(width, height)
    data = "\n".join([" ".join([str(int(255 * y / height)) for x in range(width)]) for y in range(height)])
    with open(file_path, 'w') as file:
        file.write(header + data)

def generate_ppm(file_path, width, height):
    """Generate a PPM file with a diagonal gradient."""
    header = "P3\n# This is a complex PPM file\n{} {}\n255\n".format(width, height)
    data = "\n".join([" ".join(["{} 0 {}".format(int(255 * (x + y) / (width + height - 2)), int(255 * x / width)) for x in range(width)]) for y in range(height)])
    with open(file_path, 'w') as file:
        file.write(header + data)

# Directory for generated files
directory = './tmp/'
ensure_dir(directory)

# Generate files
generate_pbm(directory + 'complex_example.pbm', 8, 8)
generate_pgm(directory + 'complex_example.pgm', 256, 256)
generate_ppm(directory + 'complex_example.ppm', 256, 256)