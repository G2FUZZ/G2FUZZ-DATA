import os
import json
import numpy as np

def generate_simulated_image_data(width, height):
    """
    Generates simulated binary image data for demonstration purposes.
    
    :param width: The width of the simulated image.
    :param height: The height of the simulated image.
    :return: A bytes object representing the simulated image data.
    """
    # Simulate a grayscale image as a 2D numpy array
    image = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    # Convert the numpy array to bytes
    image_bytes = image.tobytes()
    return image_bytes

def write_pgx_file_with_metadata(file_path, metadata, image_data):
    """
    Writes a PGX file that includes metadata and binary image data.
    
    :param file_path: The path to the PGX file to be written.
    :param metadata: A dictionary containing metadata to be included in the file.
    :param image_data: Binary image data to be included in the file.
    """
    with open(file_path, 'wb') as file:
        # Convert metadata dictionary to a JSON string and then to bytes
        metadata_json = json.dumps(metadata)
        metadata_bytes = metadata_json.encode('utf-8')
        
        # Write the metadata and image data to the file
        file.write(metadata_bytes)
        file.write(b'\n')  # Newline as a simple separator
        file.write(image_data)

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Metadata for the PGX file
metadata = {
    "description": "Simulated binary image with metadata",
    "width": 256,
    "height": 256,
    "encoding": "grayscale"
}

# Generate simulated binary image data
width, height = metadata["width"], metadata["height"]
image_data = generate_simulated_image_data(width, height)

# Filename for the PGX file
pgx_filename = 'simulated_image_with_metadata.pgx'

# Full path to save the file
pgx_file_path = os.path.join(output_dir, pgx_filename)

# Writing the metadata and image data to the PGX file
write_pgx_file_with_metadata(pgx_file_path, metadata, image_data)

print(f"PGX file '{pgx_filename}' with metadata and simulated image data has been saved to '{output_dir}'.")