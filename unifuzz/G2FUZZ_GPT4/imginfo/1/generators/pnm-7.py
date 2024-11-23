import os

def create_pbm_image(width, height, filename):
    """
    Creates a simple PBM image with alternating black and white pixels
    and saves it to the specified filename.

    Parameters:
    - width: int, the width of the image
    - height: int, the height of the image
    - filename: str, the path and filename where to save the image
    """
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Open the file in write mode
    with open(filename, 'w') as f:
        # Write the header
        f.write("P1\n")  # Magic number for PBM file format
        f.write(f"{width} {height}\n")  # Image dimensions
        
        # Generate and write image data
        for y in range(height):
            for x in range(width):
                # Simple pattern: alternate between 0 and 1 in each pixel
                f.write(f"{'1' if (x+y) % 2 == 0 else '0'} ")
            f.write("\n")

# Example usage
width, height = 100, 100  # Arbitrary dimensions
filename = "./tmp/arbitrary_pbm_image.pbm"
create_pbm_image(width, height, filename)

print(f"PBM image created with dimensions {width}x{height} at {filename}")