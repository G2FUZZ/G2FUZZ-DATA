import os

def create_pgx_file(filename, width, height):
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Corrected here
    
    # Open the file to write binary data
    with open(filename, 'wb') as file:
        # PGX header information
        # It is a simple format often starting with a magic number, 
        # followed by the width, height, and depth. This example assumes 
        # a depth of 8 bits per pixel and big endian format.
        header = f'PG ML {width} {height} 255\n'.encode()
        file.write(header)
        
        # Generate the image data: a simple gradient for demonstration
        for y in range(height):
            for x in range(width):
                # Compute pixel value as a gradient
                pixel_value = x % 256  # Ensures the value is within 0-255
                # Write the pixel value as a byte
                file.write(pixel_value.to_bytes(1, byteorder='big'))

# Example usage
create_pgx_file('./tmp/example.pgx', 256, 256)