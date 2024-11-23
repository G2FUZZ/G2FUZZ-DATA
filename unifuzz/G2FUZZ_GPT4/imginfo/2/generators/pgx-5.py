import os

def write_pgx_file(content, file_path):
    """
    Writes the given content to a PGX file.

    Args:
    - content: The text content to be written in the file.
    - file_path: The path to the file where the content will be written.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Writing the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Content to be written
content = """5. **Simplicity and Ease of Use**: Due to its straightforward, uncompressed nature, the PGX format is relatively simple and can be easily used in applications that require direct access to image data without the overhead of decoding complex compression algorithms."""

# Path to the file
file_path = './tmp/feature_pgx.txt'

# Writing the content to the PGX file
write_pgx_file(content, file_path)