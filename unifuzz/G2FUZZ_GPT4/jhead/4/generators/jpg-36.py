def save_to_file(filename, data):
    # Ensure the ./tmp/ directory exists
    import os
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Define the file path
    file_path = os.path.join('./tmp', filename)
    
    # Write data to file
    with open(file_path, 'w') as file:
        file.write(data)

# Example usage
save_to_file('example.txt', 'This is a test.')