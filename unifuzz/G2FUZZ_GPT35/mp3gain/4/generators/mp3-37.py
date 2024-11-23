# Example code to save a generated file into the ./tmp/ directory
import os

# Generate some content for the file
content = "This is the content of the generated file."

# Specify the file path in the ./tmp/ directory
file_path = "./tmp/generated_file.txt"

# Check if the ./tmp/ directory exists, if not create it
if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

# Save the generated content into the file
with open(file_path, "w") as file:
    file.write(content)

print("File saved successfully at:", file_path)