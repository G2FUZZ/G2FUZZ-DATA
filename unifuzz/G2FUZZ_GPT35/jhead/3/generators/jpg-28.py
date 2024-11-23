# Example code to save a file into the ./tmp/ directory
import os

# Define the content of the file
file_content = "This is the content of the file."

# Specify the file path within the ./tmp/ directory
file_path = "./tmp/generated_file.txt"

# Create the ./tmp/ directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Write the file with the content to the specified path
with open(file_path, "w") as file:
    file.write(file_content)

print("File saved successfully at:", file_path)