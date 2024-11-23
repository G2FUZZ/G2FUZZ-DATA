import subprocess
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# C++ source code as a string
cpp_code = """
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""

# Write the C++ code to a source file
source_file_path = './tmp/hello_world.cpp'
with open(source_file_path, 'w') as source_file:
    source_file.write(cpp_code)

# Compile the source code into an executable
executable_path = './tmp/hello_world.exe'
subprocess.run(['g++', source_file_path, '-o', executable_path], check=True)

print(f'Executable has been created at: {executable_path}')