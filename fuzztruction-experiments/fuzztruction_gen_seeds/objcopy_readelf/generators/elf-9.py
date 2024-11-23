import os
import subprocess

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# C source code as a string
c_code = """
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
"""

# Save the C code to a file
with open('./tmp/hello.c', 'w') as file:
    file.write(c_code)

# Compile the C code to an unstripped ELF binary
subprocess.run(['gcc', './tmp/hello.c', '-o', './tmp/hello_unstripped'], check=True)

# Compile the C code again to create a binary, then attempt to strip it
subprocess.run(['gcc', './tmp/hello.c', '-o', './tmp/hello_stripped'], check=True)

try:
    subprocess.run(['strip', '--strip-all', './tmp/hello_stripped'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error stripping binary: {e}")
    if os.path.exists('./tmp/hello_stripped'):
        print("The file exists, there might be an issue with the 'strip' command or the file itself.")
    else:
        print("The file does not exist. The compilation might have failed or the path is incorrect.")

print("Unstripped and stripped binaries have been generated in ./tmp/")