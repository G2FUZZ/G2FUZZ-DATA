import os

def ensure_directory(directory="./tmp/"):
    """Ensure the directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_data_to_file(data, file_path):
    """Write data to a file."""
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Data has been successfully saved to {file_path}")

def combine_files(*file_paths, combined_file_path="./tmp/combined_file.txt"):
    """Combine data from multiple files into one file."""
    combined_data = ""
    for path in file_paths:
        with open(path, 'r') as file:
            combined_data += file.read() + "\n"
    write_data_to_file(combined_data, combined_file_path)

def generate_and_combine_data():
    """Generate data, write to multiple files, then combine them into one file."""
    ensure_directory()
    data1 = "This is some data for file 1."
    data2 = "This is additional data for file 2."
    
    file_path1 = './tmp/file1.txt'
    file_path2 = './tmp/file2.txt'
    combined_file_path = './tmp/combined_data.txt'
    
    # Write data to individual files
    write_data_to_file(data1, file_path1)
    write_data_to_file(data2, file_path2)
    
    # Combine files
    combine_files(file_path1, file_path2, combined_file_path=combined_file_path)

# Example usage
generate_and_combine_data()

print("Files have been generated and combined successfully.")