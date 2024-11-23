import os

def create_pgx_file(filename, width, height, max_val, data):
    """
    Create a .pgx file with specified parameters.
    
    :param filename: Name of the file to save.
    :param width: Width of the image.
    :param height: Height of the image.
    :param max_val: Maximum pixel value (e.g., 255 for 8-bit).
    :param data: Nested list containing pixel values.
    """
    header = f"PG ML {width} {height} {max_val}\n"
    
    with open(filename, "w") as file:
        file.write(header)
        for row in data:
            line = " ".join(str(val) for val in row) + "\n"
            file.write(line)

def generate_image_data(width, height):
    """
    Generate a simple pattern for image data.
    
    :param width: Width of the image.
    :param height: Height of the image.
    :return: Nested list containing pixel values.
    """
    return [[(x + y) % 256 for x in range(width)] for y in range(height)]

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Image specifications
width, height = 10, 10
max_val = 255

# Generate image data
image_data = generate_image_data(width, height)

# Create a .pgx file
pgx_filename = "./tmp/sample_image.pgx"
create_pgx_file(pgx_filename, width, height, max_val, image_data)

print(f"Generated {pgx_filename}")