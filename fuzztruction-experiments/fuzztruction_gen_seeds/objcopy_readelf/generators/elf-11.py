import os
import subprocess

def create_elf_with_versioning(output_path):
    c_program = """
    #include <stdio.h>

    __asm__(".symver original_puts, puts@");
    __asm__(".symver new_puts, puts@@VERS_2");

    void original_puts() {
        puts("Original puts");
    }

    void new_puts() {
        puts("New puts");
    }

    int main() {
        original_puts();  // Call the original version
        new_puts();  // Call the new version
        return 0;
    }
    """
    c_filename = os.path.join(output_path, "versioned.c")
    elf_filename = os.path.join(output_path, "versioned_elf")
    version_map_file = os.path.join(output_path, "version.map")

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Write the C program to a file
    with open(c_filename, "w") as f:
        f.write(c_program)

    # Write the version map content to a file
    version_map_content = """
    VERS_1 {
        global: original_puts;
        local: *;
    };

    VERS_2 {
        global: new_puts;
    } VERS_1;
    """
    with open(version_map_file, "w") as f:
        f.write(version_map_content)

    # Ensure the version.map file exists before attempting to compile
    if not os.path.exists(version_map_file):
        raise FileNotFoundError(f"The version.map file does not exist at {version_map_file}")

    # Compile the C program into an ELF file with versioning information
    compile_command = f"gcc -o {elf_filename} {c_filename} -Wl,--version-script={version_map_file}"
    try:
        subprocess.run(compile_command, shell=True, check=True)
        print(f"ELF file '{elf_filename}' successfully created with versioning information.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile the C program: {e}")

# Usage
output_path = './tmp/'
create_elf_with_versioning(output_path)