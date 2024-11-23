import os

# Function to generate PNM files
def generate_pnm_files():
    # Ensure the tmp directory exists
    os.makedirs('./tmp', exist_ok=True)
    
    # Generate PBM file
    with open('./tmp/example.pbm', 'w') as f:
        f.write("P1\n")
        f.write("# This is an example PBM file\n")
        f.write("4 4\n")
        f.write("0 1 0 1\n")
    
    # Generate PGM file
    with open('./tmp/example.pgm', 'w') as f:
        f.write("P2\n")
        f.write("# This is an example PGM file\n")
        f.write("4 4\n")
        f.write("255\n")
        f.write("0 64 128 255\n")
    
    # Generate PPM file
    with open('./tmp/example.ppm', 'w') as f:
        f.write("P3\n")
        f.write("# This is an example PPM file\n")
        f.write("4 4\n")
        f.write("255\n")
        f.write("255 0 0 0 255 0 0 0 255\n")
        f.write("0 0 255 0 0 255 0 0 255\n")
        f.write("255 255 255 128 128 128 64 64 64\n")

# Generate PNM files
generate_pnm_files()