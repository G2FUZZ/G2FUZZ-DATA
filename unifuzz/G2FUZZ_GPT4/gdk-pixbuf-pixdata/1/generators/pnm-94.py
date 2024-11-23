import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_pbm_image(filename, width, height):
    """
    Generate a simple PBM image with a checkerboard pattern and save it.
    """
    with open(filename, 'w') as f:
        # PBM header: P1 indicates the file is a PBM image.
        # '1' means it is encoded in ASCII.
        f.write(f"P1\n{width} {height}\n")
        # Generate checkerboard pattern
        for y in range(height):
            for x in range(width):
                # Checkerboard pattern
                if (x // 10) % 2 == (y // 10) % 2:
                    f.write("1 ")
                else:
                    f.write("0 ")
            f.write("\n")

def generate_pgm_image(filename, width, height):
    """
    Generate a simple PGM image with a vertical gradient and save it.
    """
    with open(filename, 'w') as f:
        # PGM header: P2 indicates the file is a PGM image.
        # '2' means it is encoded in ASCII.
        f.write(f"P2\n{width} {height}\n255\n")
        # Generate vertical gradient
        for y in range(height):
            gray = int((y / height) * 255)
            for x in range(width):
                f.write(f"{gray} ")
            f.write("\n")

def generate_ppm_image(filename, width, height):
    """
    Generate a simple PPM image with a diagonal gradient and save it.
    """
    with open(filename, 'w') as f:
        # PPM header: P3 indicates the file is a PPM image.
        # '3' means it is encoded in ASCII.
        f.write(f"P3\n{width} {height}\n255\n")
        # Generate diagonal gradient
        for y in range(height):
            for x in range(width):
                red = int(((x + y) / (width + height)) * 255)
                green = 0
                blue = 255 - red
                f.write(f"{red} {green} {blue} ")
            f.write("\n")

def generate_pnm_image(image_type, filename, width, height):
    """
    Generate a PNM image based on the specified type (PBM, PGM, PPM).

    Args:
    - image_type: String, the type of the PNM image ('PBM', 'PGM', 'PPM').
    - filename: String, the name of the file to save the image as.
    - width: Integer, the width of the image.
    - height: Integer, the height of the image.
    """
    if image_type.upper() == 'PBM':
        generate_pbm_image(filename, width, height)
    elif image_type.upper() == 'PGM':
        generate_pgm_image(filename, width, height)
    elif image_type.upper() == 'PPM':
        generate_ppm_image(filename, width, height)
    else:
        raise ValueError(f"Unsupported image type: {image_type}. Choose 'PBM', 'PGM', or 'PPM'.")

# Example usage
generate_pnm_image('PPM', './tmp/diagonal_gradient.ppm', 256, 256)
generate_pnm_image('PGM', './tmp/vertical_gradient.pgm', 256, 256)
generate_pnm_image('PBM', './tmp/checkerboard.pbm', 256, 256)