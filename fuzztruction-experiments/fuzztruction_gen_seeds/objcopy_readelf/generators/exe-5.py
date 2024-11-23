import os
from cffi import FFI

# Prepare the directory for the output
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the C source code
c_source = """
#include <stdio.h>

void say_hello() {
    printf("Hello, World!\\n");
}
"""

# Create an instance of FFI to handle our C code
ffi = FFI()

# Adding the C function we want to compile
ffi.cdef("""
void say_hello();
""")

# Set compiler and linker flags to include debugging information
# For GCC/Clang, `-g` adds debug information
extra_compile_args = ['-g']
extra_link_args = ['-g']

# Compile and generate the shared library, including debug symbols
lib = ffi.verify(c_source, extra_compile_args=extra_compile_args, extra_link_args=extra_link_args, modulename='debug_info_exe')

# Generate the executable name
exe_name = os.path.join(output_dir, "debug_info_exe")

# Generate a small wrapper in C to create an executable
wrapper_source = """
#include <stdio.h>

extern void say_hello();

int main() {
    say_hello();
    return 0;
}
"""

# Write the wrapper source to a temporary file
wrapper_file_name = os.path.join(output_dir, "wrapper.c")
with open(wrapper_file_name, "w") as wrapper_file:
    wrapper_file.write(wrapper_source)

# Compile the wrapper and the library together to create an executable
# Note: This step requires `gcc` or a compatible compiler to be installed
os.system(f"gcc -g {wrapper_file_name} -o {exe_name} -L{output_dir} -ldebug_info_exe")

print(f"Executable with debugging information created: {exe_name}")