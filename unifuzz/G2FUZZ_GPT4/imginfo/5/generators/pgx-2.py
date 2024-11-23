import os

def create_and_save_pgx(width, height, depth=8, filename="example.pgx"):
    # Ensure the tmp directory exists
    os.makedirs("tmp", exist_ok=True)
    filepath = os.path.join("tmp", filename)
    
    # Open the file to write binary content
    with open(filepath, "wb") as file:
        # Write a simple header for demonstration (not an actual PGX header)
        header = f"P5\n{width} {height}\n{depth}\n".encode()
        file.write(header)
        
        # Generate and write image data (simple gradient)
        for y in range(height):
            for x in range(width):
                # Generate a gradient from left (black) to right (white)
                value = int((x / width) * 255)
                file.write(value.to_bytes(1, byteorder='little'))

    print(f"PGX file '{filename}' created and saved in './tmp/' directory.")

# Generate a PGX file
create_and_save_pgx(256, 256)