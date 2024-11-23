import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_ppm_image(filename, width, height):
    """
    Generate a simple PPM image with a horizontal gradient and save it.
    
    Args:
    - filename: String, the name of the file to save the image as.
    - width: Integer, the width of the image.
    - height: Integer, the height of the image.
    """
    with open(filename, 'w') as f:
        # PPM header: P3 indicates the file is a PPM image.
        # '3' means it is encoded in ASCII.
        # Following the header is the width and height of the image, and the maximum color value.
        f.write(f"P3\n{width} {height}\n255\n")
        
        # Generate image data
        for y in range(height):
            for x in range(width):
                # Simple gradient from black to red
                red = int((x / width) * 255)
                green = 0
                blue = 0
                f.write(f"{red} {green} {blue} ")
            f.write("\n")

# Example usage
generate_ppm_image('./tmp/gradient.ppm', 256, 256)