import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with file size feature
for i in range(1, 6):
    file_name = f'pixdata_{i}.txt'
    file_path = os.path.join(directory, file_name)
    
    # Generate file content
    file_size = i * 1024  # Size in bytes
    file_content = f"File size: {file_size} bytes"
    
    # Write content to file
    with open(file_path, 'w') as file:
        file.write(file_content)

    print(f'Generated {file_name} with file size: {file_size} bytes')