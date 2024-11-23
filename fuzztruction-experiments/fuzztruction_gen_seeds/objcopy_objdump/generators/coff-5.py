import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the file path
file_path = './tmp/debug_info.coff'

# Debugging information to be included
debug_info = """
Debugging Information:
- Filename: example.c
- Line Numbers: 23, 42, 56
- Symbols: main, computeValue, displayResult
"""

# Write the debugging information to the file
with open(file_path, 'w') as file:
    file.write(debug_info)

print(f'Debugging information written to {file_path}')