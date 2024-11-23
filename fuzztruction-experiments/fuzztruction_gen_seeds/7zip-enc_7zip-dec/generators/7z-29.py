import os
from py7zr import SevenZipFile

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Creating a sample file
sample_file_path = os.path.join(output_dir, 'sample.txt')
with open(sample_file_path, 'wb') as f:
    f.write(b"This is a sample content to demonstrate 7z archives." * 100)  # Adjust content size as needed

# Creating an additional feature description file for Command-line interface
cli_feature_path = os.path.join(output_dir, 'cli_feature.txt')
with open(cli_feature_path, 'w') as f:
    f.write("3. Command-line interface: In addition to GUI-based applications, 7z also offers a command-line interface, "
            "allowing users to perform operations on archives through scripts or batch files, offering greater control and automation.")

# Creating an additional feature description file for Archive updating
archive_updating_feature_path = os.path.join(output_dir, 'archive_updating_feature.txt')
with open(archive_updating_feature_path, 'w') as f:
    f.write("7. Archive updating: 7z supports updating files within an archive, allowing users to modify or replace files without needing to create a new archive.")

# Archive name
archive_name = os.path.join(output_dir, "archive_with_cli_and_updating_feature.7z")

# Creating the archive with additional CLI and Archive Updating feature files
with SevenZipFile(archive_name, 'w') as archive:
    archive.writeall(output_dir, "base_dir")

print(f"7z archive with CLI and Archive Updating features created at {archive_name}.")