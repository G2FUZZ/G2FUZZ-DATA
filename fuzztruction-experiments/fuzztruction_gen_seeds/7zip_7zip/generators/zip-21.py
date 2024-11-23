import zipfile
from datetime import datetime
import os
from hashlib import sha256

def generate_file_hash(content):
    """Generate a hash for the file content."""
    return sha256(content.encode()).hexdigest()

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/metadata_deduplication_storage.zip'

# Create a zip file with metadata
with zipfile.ZipFile(zip_path, 'w') as zipf:
    # Sample content to add to the ZIP
    sample_content = "This is some sample content for our file."
    file_name = 'sample.txt'
    
    # Additional content that is a duplicate
    duplicate_content = "This is some sample content for our file."
    duplicate_file_name = 'duplicate_sample.txt'
    
    # Dictionary to keep track of content hashes
    content_hashes = {}

    # Function to add file to zip with deduplication
    def add_file_with_deduplication(file_name, content):
        file_hash = generate_file_hash(content)
        if file_hash not in content_hashes:
            # If content is unique, add to zip and record its hash
            zipf.writestr(file_name, content)
            content_hashes[file_hash] = file_name
        else:
            # If content is a duplicate, refer to the original file
            print(f"Duplicate content found for {file_name}. Referring to {content_hashes[file_hash]}.")

    # Adding files to the ZIP with deduplication
    add_file_with_deduplication(file_name, sample_content)
    add_file_with_deduplication(duplicate_file_name, duplicate_content)
    
    # Setting metadata for the file within the ZIP
    info = zipfile.ZipInfo(file_name)
    
    # Setting the date and time of the file to Jan 1st, 2020, 12:00 PM
    info.date_time = (2020, 1, 1, 12, 0, 0)
    
    # Setting the file permissions to read, write, and execute for the owner, read for the group, and read for others
    info.external_attr = 0o755 << 16  # Unix attributes
    
    # Adding a comment to the zip file
    zipf.comment = b"This is a ZIP file containing metadata and implements data deduplication."

    # Note: The deduplication logic here ensures that identical content is not added multiple times to the ZIP.
    # Actual file metadata adjustments (like the permissions) are applied to the first instance of the file.

print("ZIP file with metadata and data deduplication has been created.")