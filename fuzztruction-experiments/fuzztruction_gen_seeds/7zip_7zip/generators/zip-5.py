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

# Note: PPMd compression is not directly supported by the Python's zipfile module as of the last update.
# Additional libraries or a different approach might be required for PPMd.