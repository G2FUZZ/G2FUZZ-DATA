import os

def create_checkerboard_pbm(width, height, cell_size):
    """
    Creates a checkerboard pattern PBM file.
    
    :param width: Width of the image in pixels
    :param height: Height of the image in pixels
    :param cell_size: Size of each cell in the checkerboard
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Open the file in binary write mode
    with open('./tmp/checkerboard.pbm', 'w') as f:
        # PBM file header
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        
        # Generate checkerboard pattern
        for y in range(height):
            for x in range(width):
                if (x // cell_size + y // cell_size) % 2 == 0:
                    f.write("1 ")
                else:
                    f.write("0 ")
            f.write("\n")

# Adjust the parameters as needed
create_checkerboard_pbm(100, 100, 10)