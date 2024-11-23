import zipfile
from pathlib import Path

def create_multipart_zip(base_zip_path, file_contents, max_size_in_bytes):
    """
    Creates multipart ZIP archives based on the specified maximum size for each part.

    Args:
    - base_zip_path: The base path for the ZIP file without an extension.
    - file_contents: A dictionary where each key is a filename and each value is the content for that file.
    - max_size_in_bytes: The maximum size in bytes for each ZIP part.
    """
    part = 1
    current_zip_path = f"{base_zip_path}_part{part}.zip"
    zipf = zipfile.ZipFile(current_zip_path, 'w', zipfile.ZIP_DEFLATED)
    current_size = 0

    for filename, content in file_contents.items():
        # Calculate the size of adding this file
        content_bytes = content.encode()  # Assuming the content is a string that needs to be encoded to bytes
        temp_size = len(content_bytes)
        
        # Check if adding this file would exceed the max size for the current part
        if current_size + temp_size > max_size_in_bytes and current_size > 0:
            # Close the current part and start a new one
            zipf.close()
            part += 1
            current_zip_path = f"{base_zip_path}_part{part}.zip"
            zipf = zipfile.ZipFile(current_zip_path, 'w', zipfile.ZIP_DEFLATED)
            current_size = 0  # Reset current size for the new part

        # Add the file to the current part
        zipf.writestr(filename, content)
        current_size += temp_size

    # Close the last part
    zipf.close()
    print(f"Multipart ZIP archive created with {part} parts.")

# Ensure the ./tmp/ directory exists
Path("./tmp/").mkdir(parents=True, exist_ok=True)

# Base path for the new multipart ZIP file (without extension)
base_zip_path = "./tmp/unicode_support示例"

# Files to include in the ZIP with their content
file_contents = {
    "示例文档.txt": "This is a demonstration of ZIP's Unicode support.",
    "Multipart_Info.txt": "Demonstrates Multipart ZIP Archives feature."
}

# Maximum size for each ZIP part (in bytes)
max_size_in_bytes = 500  # Example size, adjust as needed

# Create a multipart ZIP archive
create_multipart_zip(base_zip_path, file_contents, max_size_in_bytes)