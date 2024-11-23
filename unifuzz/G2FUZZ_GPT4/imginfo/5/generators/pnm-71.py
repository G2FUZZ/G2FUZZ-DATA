import os

def create_colored_checkerboard_ppm(width, height, cell_size, color1, color2):
    """
    Creates a colored checkerboard pattern PPM file.
    
    :param width: Width of the image in pixels
    :param height: Height of the image in pixels
    :param cell_size: Size of each cell in the checkerboard
    :param color1: Color of the first cell (r, g, b)
    :param color2: Color of the second cell (r, g, b)
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    with open('./tmp/colored_checkerboard.ppm', 'w') as f:
        # PPM file header
        f.write("P3\n")  # P3 means this is a RGB color image in ASCII
        f.write(f"{width} {height}\n")
        f.write("255\n")  # Max color value
        
        # Generate checkerboard pattern
        for y in range(height):
            for x in range(width):
                if (x // cell_size + y // cell_size) % 2 == 0:
                    f.write(f"{color1[0]} {color1[1]} {color1[2]} ")
                else:
                    f.write(f"{color2[0]} {color2[1]} {color2[2]} ")
            f.write("\n")

# Adjust the parameters as needed
create_colored_checkerboard_ppm(100, 100, 10, (255, 0, 0), (0, 0, 255))