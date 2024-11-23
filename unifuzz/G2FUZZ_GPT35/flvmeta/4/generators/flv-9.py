import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample FLV file with encryption feature
sample_data = b'FLV File with Encryption Feature'
file_path = './tmp/sample_file.flv'

with open(file_path, 'wb') as file:
    # Simulate encryption by writing the sample data as it is
    file.write(sample_data)

print(f"FLV file with encryption feature generated and saved at: {file_path}")