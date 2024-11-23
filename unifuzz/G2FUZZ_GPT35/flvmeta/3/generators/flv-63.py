import os

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save generated files into the ./tmp/ directory
# Example:
with open('./tmp/generated_file.txt', 'w') as file:
    file.write('This is a generated file.')

print('Files saved in ./tmp/ directory.')