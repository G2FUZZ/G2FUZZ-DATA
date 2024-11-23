import os

# Function to generate a sample 'ras' file with compression features
def generate_ras_file(filename):
    # Sample data to write into the 'ras' file
    data = "Sample data for compression using RLE (Run-Length Encoding)."

    # Applying compression using RLE
    compressed_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data += str(count) + data[i - 1]
            count = 1
    compressed_data += str(count) + data[-1]

    # Writing the compressed data to the 'ras' file
    with open(filename, 'w') as file:
        file.write(compressed_data)

# Create a directory to store the generated 'ras' files
output_directory = './tmp/'
os.makedirs(output_directory, exist_ok=True)

# Generate 'ras' files with compression features
for i in range(5):  # Generate 5 'ras' files
    filename = os.path.join(output_directory, f'file_{i+1}.ras')
    generate_ras_file(filename)
    print(f"Generated file: {filename}")