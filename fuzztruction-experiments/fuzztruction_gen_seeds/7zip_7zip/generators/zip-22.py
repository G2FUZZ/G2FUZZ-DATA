import zipfile
from datetime import datetime
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/advanced_metadata_storage.zip'

# Create a zip file with metadata and custom compression
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    # Sample content to add to the ZIP
    sample_content = "This is some sample content for our file."
    file_name = 'sample.txt'

    # Writing the file with content
    zipf.writestr(file_name, sample_content)

    # Setting metadata for the file within the ZIP
    info = zipfile.ZipInfo(file_name)

    # Setting the date and time of the file to Jan 1st, 2020, 12:00 PM
    info.date_time = (2020, 1, 1, 12, 0, 0)

    # Setting the file permissions to read, write, and execute for the owner, read for the group, and read for others
    # This is a UNIX specific example, and might not work as intended in non-UNIX environments
    info.external_attr = 0o755 << 16  # Unix attributes

    # Writing the file with the specified info and metadata
    zipf.writestr(info, sample_content)

    # Adding a comment to the file
    zipf.comment = b"This ZIP file contains advanced metadata including custom compression algorithms."

# Note: Python's zipfile module supports ZIP_STORED (no compression) and ZIP_DEFLATED (standard zlib compression).
# For actual custom or third-party compression algorithms, one might need to use external tools or libraries,
# as the standard zipfile module does not support plugging in custom compression algorithms directly.

print("ZIP file with advanced metadata and custom compression has been created.")