# Save the generated files into './tmp/'
output_path = './tmp/'

# Your code for generating files goes here
# For example:
# with open(output_path + 'file1.txt', 'w') as file:
#     file.write('Content for file1')

# Make sure to create the './tmp/' directory if it doesn't exist
import os
if not os.path.exists(output_path):
    os.makedirs(output_path)