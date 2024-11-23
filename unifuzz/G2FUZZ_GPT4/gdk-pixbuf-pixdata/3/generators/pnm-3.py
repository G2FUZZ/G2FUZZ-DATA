import os

def create_pbm_image(filename):
    """Create a simple PBM image."""
    header = "P1\n# This is a PBM file\n3 3\n"
    data = "0 1 0\n1 0 1\n0 1 0\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def create_pgm_image(filename):
    """Create a simple PGM image."""
    header = "P2\n# This is a PGM file\n3 3\n255\n"
    data = "255 0 255\n0 255 0\n255 0 255\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def create_ppm_image(filename):
    """Create a simple PPM image."""
    header = "P3\n# This is a PPM file\n3 3\n255\n"
    data = "255 0 0  0 255 0  0 0 255\n" \
           "0 255 0  255 0 0  0 0 255\n" \
           "0 0 255  0 255 0  255 0 0\n"
    with open(filename, 'w') as file:
        file.write(header + data)

def main():
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Create PBM, PGM, and PPM images
    create_pbm_image(os.path.join(output_dir, 'image.pbm'))
    create_pgm_image(os.path.join(output_dir, 'image.pgm'))
    create_ppm_image(os.path.join(output_dir, 'image.ppm'))

if __name__ == "__main__":
    main()