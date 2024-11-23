import os

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a flv file with complex file structure including metadata
def generate_flv_file(file_name, metadata):
    file_path = f'./tmp/{file_name}.flv'

    # Generate the flv file with metadata
    with open(file_path, 'wb') as file:
        # Write metadata to the flv file
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        file.write(metadata.encode())

    print(f'Generated {file_name}.flv with metadata')

# Example metadata for the flv file
metadata = 'Title: My Generated FLV File\nAuthor: John Doe\nDate: 2022-01-01'

# Generate a flv file with metadata
generate_flv_file('complex_flv', metadata)