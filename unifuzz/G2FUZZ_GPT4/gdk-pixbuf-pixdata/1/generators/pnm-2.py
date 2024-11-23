import os

def generate_ascii_pbm(filename, width, height, pattern):
    with open(filename, 'w') as f:
        # PBM header for ASCII format
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        
        for y in range(height):
            for x in range(width):
                pixel = pattern[y % len(pattern)][x % len(pattern[0])]
                f.write(f"{pixel} ")
            f.write("\n")

def generate_binary_pbm(filename, width, height, pattern):
    with open(filename, 'wb') as f:
        # PBM header for Binary format
        f.write(b"P4\n")
        f.write(f"{width} {height}\n".encode())
        
        for y in range(height):
            byte = 0
            for x in range(width):
                pixel = pattern[y % len(pattern)][x % len(pattern[0])]
                byte = (byte << 1) | pixel
                if (x + 1) % 8 == 0 or x == width - 1:
                    f.write(bytes([byte]))
                    byte = 0

if __name__ == "__main__":
    os.makedirs("./tmp/", exist_ok=True)
    
    # Checkerboard pattern for a 5x5 image
    pattern = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    
    # Generate ASCII PBM
    generate_ascii_pbm("./tmp/ascii_checkerboard.pbm", 5, 5, pattern)
    
    # Generate Binary PBM
    generate_binary_pbm("./tmp/binary_checkerboard.pbm", 5, 5, pattern)