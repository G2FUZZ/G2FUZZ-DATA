import os

def create_streamable_pnm(width, height, content):
    """
    Generate a simple PNM file (P1 format, for ASCII representation of a bitmap)
    representing basic content, demonstrating the streamable nature of PNM files.
    This function directly writes to a file in the ./tmp/ directory.
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the file path
    file_path = './tmp/streamable.pbm'
    
    # Open the file and write the header and content
    with open(file_path, 'w') as f:
        # P1 header for a PBM file (ASCII variant)
        f.write(f'P1\n')
        # Image dimensions
        f.write(f'{width} {height}\n')
        # Image data (streaming the content row by row)
        for row in content:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

# Example content for demonstration (3x3 checkerboard pattern)
content = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

# Generate the PNM file
create_streamable_pnm(3, 3, content)