import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Example: Saving a text file to ./tmp/
file_path = os.path.join(output_dir, "example_file.txt")
with open(file_path, 'w') as file:
    file.write("This is an example file saved in ./tmp/")

print(f"File saved to {file_path}")