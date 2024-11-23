import os

def create_pbm_pattern(filename, width, height, pattern):
    """Create a PBM image with a specified pattern."""
    header = f"P1\n# This is a PBM file\n{width} {height}\n"
    data = ""
    for y in range(height):
        for x in range(width):
            data += f"{pattern(x, y)} "
        data += "\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def create_pgm_gradient(filename, width, height):
    """Create a PGM image with a gradient."""
    header = f"P2\n# This is a PGM file\n{width} {height}\n255\n"
    data = ""
    for y in range(height):
        for x in range(width):
            value = int(x / width * 255)
            data += f"{value} "
        data += "\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def create_ppm_color_gradient(filename, width, height):
    """Create a PPM image with a color gradient."""
    header = f"P3\n# This is a PPM file\n{width} {height}\n255\n"
    data = ""
    for y in range(height):
        for x in range(width):
            red = int(x / width * 255)
            green = int(y / height * 255)
            blue = 255 - red
            data += f"{red} {green} {blue}  "
        data += "\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def create_pattern(x, y):
    """A simple checkerboard pattern for PBM files."""
    return (x + y) % 2

def main():
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Dimensions for the images
    width, height = 50, 50
    
    # Create PBM, PGM, and PPM images with more complex features
    create_pbm_pattern(os.path.join(output_dir, 'pattern.pbm'), width, height, create_pattern)
    create_pgm_gradient(os.path.join(output_dir, 'gradient.pgm'), width, height)
    create_ppm_color_gradient(os.path.join(output_dir, 'color_gradient.ppm'), width, height)

if __name__ == "__main__":
    main()