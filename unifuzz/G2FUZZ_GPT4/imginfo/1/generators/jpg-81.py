import os

def save_file_in_tmp(filename, content):
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the full path for the file to be saved
    file_path = os.path.join('./tmp/', filename)
    
    # Open the file and write the content
    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"File '{filename}' has been saved in ./tmp/")

# Example usage
save_file_in_tmp('example.txt', 'This is a test file.')