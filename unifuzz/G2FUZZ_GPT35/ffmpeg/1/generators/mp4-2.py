import os

# Create a directory to store the generated files
os.makedirs("./tmp", exist_ok=True)

# Generate an empty mp4 file
file_path = "./tmp/generated_file.mp4"
open(file_path, 'a').close()

print(f"Generated mp4 file at: {file_path}")