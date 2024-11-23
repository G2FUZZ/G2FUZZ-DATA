import os

def create_pgx_file(directory, filename):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    
    # PGX file header and dummy data for demonstration
    # Simple header format: PG + newline, Width Height + newline, Depth + newline, then data
    header = "PG\n512 512\n255\n"
    data = bytearray([0, 255] * (512 * 512 // 2))  # Example alternating pixel data
    
    with open(filepath, "wb") as file:
        file.write(header.encode())  # Writing the header
        file.write(data)  # Writing the dummy image data

# Filename for the PGX file
filename = "example.pgx"

# Call the function to create a PGX file
create_pgx_file("./tmp/", filename)

print(f"PGX file '{filename}' has been created in './tmp/'.")