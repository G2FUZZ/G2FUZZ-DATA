import os
import pyminizip

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filenames and password
zip_base_filename = './tmp/protected_zip'
password = 'secure_password'

# Create sample files to include in the zip
sample_filenames = ['./tmp/sample1.txt', './tmp/sample2.txt']
for idx, sample_filename in enumerate(sample_filenames, start=1):
    with open(sample_filename, 'w') as sample_file:
        sample_file.write(f'This is sample file {idx} to be zipped and password protected.')

# Using pyminizip to create password-protected zip files with Archive Slicing
compression_level = 5  # Compression level: 1-9

# Define the maximum size for each zip file part (in MB)
# For demonstration, we'll use a small size to ensure splitting
max_part_size = 1

# Calculate the total size of files to be compressed to determine the number of parts
total_size = sum(os.path.getsize(f) for f in sample_filenames)
approx_zip_size = total_size * 1.1  # Approximate zip size (considering compression)
num_parts = max(1, int(approx_zip_size / (max_part_size * 1024 * 1024)))

# Archive slicing: Splitting the archive if there are multiple parts
if num_parts > 1:
    for i, sample_filename in enumerate(sample_filenames):
        part_zip_filename = f"{zip_base_filename}_part_{i+1}.zip"
        pyminizip.compress(sample_filename, None, part_zip_filename, password, compression_level)
        print(f"Password-protected zip part created at: {part_zip_filename}")
else:
    # If only one part, just compress all files together
    zip_filename = f"{zip_base_filename}.zip"
    pyminizip.compress_multiple(sample_filenames, [], zip_filename, password, compression_level)
    print(f"Password-protected zip file created at: {zip_filename}")

# Cleanup the sample files
for sample_filename in sample_filenames:
    os.remove(sample_filename)