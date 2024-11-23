import subprocess
import os

# Define the directory where the exe will be saved
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# C program source code as a string
c_program = """
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
"""

# Save the C program to a file
c_program_filename = os.path.join(output_dir, "program.c")
with open(c_program_filename, "w") as file:
    file.write(c_program)

# Compile the C program to an exe
exe_filename = os.path.join(output_dir, "program.exe")
compile_command = f"gcc {c_program_filename} -o {exe_filename}"

try:
    # Execute the compilation command
    subprocess.run(compile_command, shell=True, check=True)
    print(f"Successfully created {exe_filename}.")
except subprocess.CalledProcessError as e:
    print(f"Failed to compile the program. Error: {e}")