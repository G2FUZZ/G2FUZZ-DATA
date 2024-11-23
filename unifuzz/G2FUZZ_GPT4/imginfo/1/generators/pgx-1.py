from PIL import Image
import os

def create_grayscale_pgx(width, height, output_path):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create a new grayscale image with a gradient
    image = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            # Example gradient: horizontal gradient from black to white
            color = int((x / width) * 255)
            image.putpixel((x, y), color)

    # Convert the image data to the PGX format
    # PGX format header for endianess, width, height, and bit depth
    pgx_header = "PG ML " + str(width) + " " + str(height) + " 255\n"
    pgx_data = pgx_header.encode('utf-8')

    # Add the image data
    pixels = list(image.getdata())
    for pixel in pixels:
        pgx_data += pixel.to_bytes(1, byteorder='big')

    # Save the PGX file
    with open(output_path, 'wb') as file:
        file.write(pgx_data)

# Example usage
create_grayscale_pgx(256, 256, './tmp/example.pgx')