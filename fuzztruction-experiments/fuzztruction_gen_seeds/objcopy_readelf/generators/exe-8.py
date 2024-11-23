import os
from subprocess import Popen, PIPE

# Directory to store the generated exe
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Python code to be converted into an exe
python_code = """
import sys
def main():
    print("Hello, World!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
"""

# Save the Python code to a temporary file
tmp_python_file = os.path.join(output_dir, "temp_python_script.py")
with open(tmp_python_file, "w") as file:
    file.write(python_code)

# Manifest content
manifest_content = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="1.0.0.0"
    processorArchitecture="*"
    name="MyApplication"
    type="win32"/>
<description>My Application</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"/>
    </dependentAssembly>
</dependency>
</assembly>
'''

# Save the manifest content to a file
manifest_file_path = os.path.join(output_dir, "application.manifest")
with open(manifest_file_path, "w") as manifest_file:
    manifest_file.write(manifest_content)

# Compile the Python script to an exe, including the manifest for dependencies
compile_command = f'pyinstaller --onefile --windowed --icon=NONE --name MyApp --add-data "{manifest_file_path};." "{tmp_python_file}"'

# Execute the compilation command
process = Popen(compile_command, shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

if process.returncode == 0:
    print("Compilation succeeded. Exe and manifest are in the ./tmp/ directory.")
else:
    print("Compilation failed.")
    print("STDOUT:", stdout.decode())
    print("STDERR:", stderr.decode())