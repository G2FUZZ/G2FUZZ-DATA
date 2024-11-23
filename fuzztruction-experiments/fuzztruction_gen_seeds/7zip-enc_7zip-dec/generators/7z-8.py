import os
from subprocess import Popen, PIPE

# Define the path to save the self-extracting archive
output_path = "./tmp/"
output_filename = "archive.exe"  # Naming it .exe to indicate self-extracting
full_output_path = os.path.join(output_path, output_filename)

# Ensure the output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Create a sample text file to include in the archive
sample_file_path = os.path.join(output_path, "sample.txt")
with open(sample_file_path, "w") as f:
    f.write("This is a sample file to include in the self-extracting archive.")

# Using 7z command line to create a self-extracting archive
# Note: This assumes 7-Zip is installed and the 7z command is available in the system's PATH
command = f"7z a -sfx {full_output_path} {sample_file_path}"

# Execute the command
process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print("Error creating self-extracting archive:", stderr.decode())
else:
    print(f"Self-extracting archive created successfully at '{full_output_path}'")

# Clean up sample file
os.remove(sample_file_path)