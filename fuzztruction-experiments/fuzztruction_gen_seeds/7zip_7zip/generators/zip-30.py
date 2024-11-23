import zipfile
from datetime import datetime
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/advanced_metadata_storage.zip'

# Function to add or update files in the ZIP
def add_or_update_zip(zip_path, file_name, content, date_time, permissions):
    with zipfile.ZipFile(zip_path, 'a', compression=zipfile.ZIP_DEFLATED) as zipf:
        # Check if the file exists in the zip file
        if file_name in zipf.namelist():
            # Remove the existing file
            new_zip_content = {name: zipf.read(name) for name in zipf.namelist() if name != file_name}
            os.remove(zip_path)
            with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_zipf:
                for name, data in new_zip_content.items():
                    new_zipf.writestr(name, data)
        
        # After ensuring the file doesn't exist, or it's been deleted, add/update it
        info = zipfile.ZipInfo(file_name)
        # Setting the date and time of the file
        info.date_time = date_time
        # Setting the file permissions
        info.external_attr = permissions << 16  # Unix attributes
        zipf.writestr(info, content)

# Create or update the zip file with initial content
sample_content = "This is some sample content for our file."
file_name = 'sample.txt'
add_or_update_zip(zip_path, file_name, sample_content, (2020, 1, 1, 12, 0, 0), 0o755)

# Implementing Archive Update Mechanisms
# Scenario: We want to update 'sample.txt' with new content
new_content = "This content has been updated."
add_or_update_zip(zip_path, file_name, new_content, datetime.now().timetuple()[:6], 0o755)

# Adding a comment to the file
with zipfile.ZipFile(zip_path, 'a') as zipf:
    zipf.comment = b"This ZIP file contains advanced metadata including custom compression algorithms, and supports archive update mechanisms."

print("ZIP file with advanced metadata, custom compression, and archive update mechanisms has been created.")