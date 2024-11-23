import subprocess
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# The C source code as a string
c_source_code = """
#include <stdio.h>

int main() {
    printf("Hello, Debug World!\\n");
    return 0;
}
"""

# Save the C source code to a file
source_file_path = './tmp/hello_debug.c'
with open(source_file_path, 'w') as source_file:
    source_file.write(c_source_code)

# Compile the C source code with debug information
# -g flag is used to include debug information
compile_command = ['gcc', source_file_path, '-g', '-o', './tmp/hello_debug.elf']

# Execute the compile command
subprocess.run(compile_command, check=True)

print("ELF file with debug information generated at './tmp/hello_debug.elf'")