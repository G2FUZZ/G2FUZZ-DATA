import os

def create_pbm(filename):
    """Create a PBM file with a checkerboard pattern."""
    width, height = 10, 10
    data = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y) % 2 == 0:
                row.append("1")
            else:
                row.append("0")
        data.append(" ".join(row))
    
    with open(filename, "w") as f:
        f.write(f"P1\n{width} {height}\n")
        f.write("\n".join(data))

def create_ppm(filename):
    """Create a PPM file with a horizontal gradient."""
    width, height = 256, 10
    with open(filename, "w") as f:
        f.write(f"P3\n{width} {height}\n255\n")
        for y in range(height):
            for x in range(width):
                f.write(f"{x} {x} {255 - x} ")
            f.write("\n")

# Ensure the tmp directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate PBM and PPM files
create_pbm("./tmp/checkerboard.pbm")
create_ppm("./tmp/gradient.ppm")