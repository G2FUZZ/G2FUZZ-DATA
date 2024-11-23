import os
import numpy as np

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a checkerboard pattern
def generate_checkerboard(size=10, cell_size=5):
    """
    Generates a checkerboard pattern.
    
    Parameters:
    - size: The size of the checkerboard (size x size)
    - cell_size: The size of each cell in the checkerboard
    
    Returns:
    - A numpy array representing the checkerboard pattern
    """
    rows = size * cell_size
    cols = size * cell_size
    board = np.zeros((rows, cols))
    for x in range(size):
        for y in range(size):
            if (x + y) % 2:
                board[x*cell_size:(x+1)*cell_size, y*cell_size:(y+1)*cell_size] = 1
    return board

# Extended function to generate PBM, PGM, and PPM files with more options
def generate_pnm(filename, filetype='P1', pattern=None, size=10, cell_size=5, maxval=255, binary=False):
    """
    Generates a PNM file given the specifications.

    Parameters:
    - filename: The name of the file to save.
    - filetype: The type of the PNM file. Options: P1, P2, P3 for ASCII formats and P4, P5, P6 for binary formats.
    - pattern: Function to generate the pattern. If None, a checkerboard pattern is used.
    - size: The size parameter for the pattern.
    - cell_size: The cell size parameter for the pattern.
    - maxval: The maximum value for PGM and PPM files.
    - binary: Whether to generate binary files (P4, P5, P6). If False, ASCII files are generated (P1, P2, P3).
    """
    if pattern is None:
        pattern = generate_checkerboard
    
    data = pattern(size, cell_size)
    
    header = f"{filetype}\n# Generated {filetype} file\n{data.shape[1]} {data.shape[0]}\n"
    if filetype in ['P2', 'P3', 'P5', 'P6'] and not filetype in ['P1', 'P4']:
        header += f"{maxval}\n"
    
    if binary and filetype in ['P4', 'P5', 'P6']:
        with open(filename, 'wb') as f:
            f.write(header.encode())
            if filetype == 'P5':
                f.write(data.astype(np.uint8).tobytes())
            elif filetype == 'P6':
                f.write(np.repeat(data[:, :, np.newaxis], 3, axis=2).astype(np.uint8).tobytes())
            # P4 (binary PBM) is more complex due to bit-packing and is not directly covered here.
    else:
        with open(filename, 'w') as f:
            f.write(header)
            if filetype in ['P1', 'P2']:
                for row in data:
                    f.write(' '.join(str(int(val)) for val in row) + '\n')
            elif filetype == 'P3':
                for row in data:
                    f.write(' '.join(f"{int(val)} {int(val)} {int(val)}" for val in row) + '\n')

# Example usage
generate_pnm('./tmp/complex_checkerboard.pbm', 'P1', size=8, cell_size=2)
generate_pnm('./tmp/complex_checkerboard.pgm', 'P2', size=8, cell_size=2, maxval=255)
generate_pnm('./tmp/complex_checkerboard.ppm', 'P3', size=8, cell_size=2, maxval=255)

print("Complex PNM files generated successfully.")