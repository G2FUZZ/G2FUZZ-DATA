import os

def generate_pbm_checkerboard(file_path, width, height, cell_size):
    """
    Generates a PBM file with a checkerboard pattern.
    
    Args:
    - file_path: Path to save the PBM file.
    - width: Width of the image in pixels.
    - height: Height of the image in pixels.
    - cell_size: Size of each cell in the checkerboard.
    """
    header = "P1\n# Checkerboard PBM\n{} {}\n".format(width, height)
    pattern = []

    for y in range(height):
        row = []
        for x in range(width):
            if (x // cell_size % 2) == (y // cell_size % 2):
                row.append("0")
            else:
                row.append("1")
        pattern.append(" ".join(row))
    
    with open(file_path, 'w') as f:
        f.write(header + "\n".join(pattern))

def generate_ppm_gradient(file_path, width, height):
    """
    Generates a PPM file with a vertical gradient.
    
    Args:
    - file_path: Path to save the PPM file.
    - width: Width of the image in pixels.
    - height: Height of the image in pixels.
    """
    header = "P3\n# Vertical Gradient PPM\n{} {}\n255\n".format(width, height)
    pattern = []

    for y in range(height):
        row = []
        r, g, b = (y * 255 // height, 128, 255 - y * 255 // height)
        for x in range(width):
            row.append("{} {} {}".format(r, g, b))
        pattern.append(" ".join(row))
    
    with open(file_path, 'w') as f:
        f.write(header + "\n".join(pattern))

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a checkerboard PBM
generate_pbm_checkerboard('./tmp/complex_checkerboard.pbm', 100, 100, 10)

# Generate a vertical gradient PPM
generate_ppm_gradient('./tmp/vertical_gradient.ppm', 100, 100)

print("Complex PNM files have been generated and saved in './tmp/'.")