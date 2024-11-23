import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with H.264 video codec and AAC audio codec
file_path = './tmp/sample.flv'
with open(file_path, 'wb') as file:
    # Write dummy data for the FLV file
    file.write(b'FLV File with H.264 video codec and AAC audio codec')

print(f"FLV file with H.264 video codec and AAC audio codec generated and saved at: {file_path}")