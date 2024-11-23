import zipfile
from datetime import datetime
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/metadata_storage.zip'

# Create a zip file with metadata
with zipfile.ZipFile(zip_path, 'w') as zipf:
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
    
    # Adding a comment to the file
    zipf.comment = b"This is a ZIP file containing metadata."

    # Write the file with the specified info and metadata
    zipf.writestr(info, sample_content)

print("ZIP file with metadata has been created.")