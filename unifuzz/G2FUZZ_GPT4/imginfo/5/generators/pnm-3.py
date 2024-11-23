import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a PBM file (Portable Bitmap, binary)
def generate_pbm(filename, width, height, pattern):
    with open(filename, 'w') as f:
        # P1 is the magic number for PBM ASCII encoding
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        for row in range(height):
            for col in range(width):
                f.write(f"{pattern(row, col)} ")
            f.write("\n")

# Generate a PGM file (Portable GrayMap, binary)
def generate_pgm(filename, width, height, maxval, pattern):
    with open(filename, 'w') as f:
        # P2 is the magic number for PGM ASCII encoding
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for row in range(height):
            for col in range(width):
                f.write(f"{pattern(row, col, maxval)} ")
            f.write("\n")

# Generate a PPM file (Portable PixMap, binary)
def generate_ppm(filename, width, height, maxval, pattern):
    with open(filename, 'w') as f:
        # P3 is the magic number for PPM ASCII encoding
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for row in range(height):
            for col in range(width):
                r, g, b = pattern(row, col, maxval)
                f.write(f"{r} {g} {b} ")
            f.write("\n")

# Example patterns
def pbm_pattern(row, col):
    return (row + col) % 2  # Checkerboard pattern

def pgm_pattern(row, col, maxval):
    return (row + col) % maxval  # Gradient pattern

def ppm_pattern(row, col, maxval):
    return ((row % maxval), (col % maxval), (maxval // 2))  # RGB pattern

# Generate files
generate_pbm('./tmp/sample.pbm', 10, 10, pbm_pattern)
generate_pgm('./tmp/sample.pgm', 10, 10, 15, pgm_pattern)
generate_ppm('./tmp/sample.ppm', 10, 10, 15, ppm_pattern)