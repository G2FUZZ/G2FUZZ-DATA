import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save generated files into the ./tmp/ directory
# Example:
with open('./tmp/generated_file.txt', 'w') as file:
    file.write('This is a generated file content.')