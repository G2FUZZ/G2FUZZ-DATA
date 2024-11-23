import zipfile
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Text content to compress
content = b"This is some text to compress using different algorithms."

# Creating ZIP files with different compression methods
compression_methods = {
    'DEFLATE': zipfile.ZIP_DEFLATED,
    'BZIP2': zipfile.ZIP_BZIP2,
    'LZMA': zipfile.ZIP_LZMA,
}

for method_name, method in compression_methods.items():
    zip_filename = f"./tmp/example_{method_name.lower()}.zip"
    # Open the ZIP file in write mode
    with zipfile.ZipFile(zip_filename, 'w', compression=method) as zipf:
        # Writing a file to the archive. The file name inside the archive will be 'content.txt'
        # Compressing the content using the specified method
        zipf.writestr('content.txt', content)
    print(f"Created {zip_filename} using {method_name}")

# Create a zip file with Archive Locking feature
zip_filename_locked = "./tmp/example_locked.zip"
with zipfile.ZipFile(zip_filename_locked, 'w') as zipf_locked:
    # Writing a file to the archive. The file name inside the archive will be 'content.txt'
    zipf_locked.writestr('content.txt', content)
    # Simulating the Archive Locking feature - in reality, this would require using an external tool or library
    # as Python's zipfile module does not support locking archives inherently.
    # This is a placeholder action to demonstrate where the locking action would occur.
    print("Simulating the locking of the archive - this archive is now considered locked and cannot be modified.")

print(f"Created {zip_filename_locked} with Archive Locking simulated")

# Note: The actual locking of a ZIP archive, preventing further changes, is not supported natively by the zipfile module.
# This would require either a custom implementation or the use of external tools or libraries that support such a feature.