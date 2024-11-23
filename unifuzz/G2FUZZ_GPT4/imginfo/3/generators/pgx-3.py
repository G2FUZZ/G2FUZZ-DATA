import numpy as np
import os

def create_pgx_file(filename, width, height, bitdepth):
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    # Create a simple vertical gradient
    # Note: For demonstration, we scale the gradient 
    # to utilize the full range of the selected bitdepth.
    max_val = 2**bitdepth - 1
    image = np.tile(np.linspace(0, max_val, height, dtype=np.uint16), (width, 1)).T

    # PGX format details:
    # - Little endian format
    # - No compression
    # Header format: PG + \n + Width + \n + Height + \n + Depth + \n
    # Data format: raw pixel values
    with open(filepath, 'wb') as f:
        header = f"PG\n{width}\n{height}\n{bitdepth}\n".encode()
        f.write(header)
        # Write the image data
        for row in image:
            f.write(row.tobytes())

# Example usage
create_pgx_file('hdr_image.pgx', 256, 256, 16)