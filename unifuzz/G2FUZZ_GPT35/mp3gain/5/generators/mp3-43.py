# Save the generated files into the ./tmp/ directory
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Your code to generate and save files goes here
# For example:
with open('./tmp/generated_file.txt', 'w') as file:
    file.write('This is a generated file.')

print('Files saved successfully in ./tmp/ directory.')