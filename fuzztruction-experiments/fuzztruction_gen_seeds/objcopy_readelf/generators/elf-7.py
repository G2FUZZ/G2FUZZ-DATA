import subprocess
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# C source code that uses the math library dynamically
c_code = """
#include <stdio.h>
#include <math.h>

int main() {
    printf("Cosine of 0 is %f\\n", cos(0.0));
    return 0;
}
"""

# Save the C source to a file
source_file_path = './tmp/sample_program.c'
with open(source_file_path, 'w') as f:
    f.write(c_code)

# Compile the C program to an ELF file using gcc, linking dynamically to the math library
compiled_program_path = './tmp/sample_program'
subprocess.run(['gcc', source_file_path, '-o', compiled_program_path, '-lm'], check=True)

print(f"Compiled ELF file saved to: {compiled_program_path}")

# Note: This script does not modify the ELF file to add dynamic linking features,
# as they are inherently part of the compilation process when using shared libraries.