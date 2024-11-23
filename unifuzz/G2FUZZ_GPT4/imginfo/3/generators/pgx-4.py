import os

def create_pgx_file(filename, width, height, max_val, pixel_values):
    """
    Creates a .pgx file with the given parameters.

    Parameters:
    - filename: The name of the file to create.
    - width: The width of the image.
    - height: The height of the image.
    - max_val: The maximum pixel value (usually 255 for 8-bit images).
    - pixel_values: A list of lists containing pixel values for each row.
    """
    header = f"PG ML {width} {height} {max_val}\n"
    body = "".join(["".join([f"{val} " for val in row]) + "\n" for row in pixel_values])

    # Ensure the ./tmp/ directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        file.write(header)
        file.write(body)

# Example usage
filename = "./tmp/sample.pgx"
width = 5
height = 5
max_val = 255
# Create a simple pattern: a 5x5 image with a cross pattern
pixel_values = [
    [255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [255, 0, 0, 0, 255],
]

create_pgx_file(filename, width, height, max_val, pixel_values)