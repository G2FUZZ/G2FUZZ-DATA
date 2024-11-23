import os
from subprocess import check_call

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Step 1: Create a simple C program
c_program = """
#include <stdio.h>

void my_function() {
    printf("Hello from my_function\\n");
}

int main() {
    my_function();
    return 0;
}
"""

# Save the C program to a file
with open('./tmp/simple_program.c', 'w') as f:
    f.write(c_program)

# Step 2: Compile the C program into an ELF file
# This requires gcc to be installed and accessible from the current environment
check_call(['gcc', './tmp/simple_program.c', '-o', './tmp/simple_program.elf'])

# Note: This step actually generates the ELF file with a symbol table
# For demonstration purposes, we're not directly manipulating the ELF file to add a symbol table
# because that's complex and requires in-depth knowledge of the ELF format.

# Step 3: Here you can use pyelftools or similar to read/manipulate ELF files
# For example, to analyze the ELF file or its symbol table (not shown here due to complexity)
# from elftools.elf.elffile import ELFFile

# with open('./tmp/simple_program.elf', 'rb') as f:
#     elffile = ELFFile(f)
#     # Do something with elffile, e.g., print the symbol table
#     # This is a placeholder for ELF manipulation/analysis

print("ELF file with symbol table generated at ./tmp/simple_program.elf")