import zipfile
from datetime import datetime
import os
import stat

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/metadata_extended_storage.zip'

# Create a zip file with extended metadata
with zipfile.ZipFile(zip_path, 'w') as zipf:
    # Sample content to add to the ZIP
    sample_content = "This is some enhanced sample content for our file."
    file_name = 'enhanced_sample.txt'
    
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
    zipf.comment = b"This is an enhanced ZIP file containing metadata and preserving file system attributes."

    # In order to preserve file system attributes, we simulate creating a temporary file with these attributes
    # and then adding it to the zip. This is a crude form of simulating the preservation as Python's zipfile
    # doesn't directly support extracting or setting specific file system attributes like NTFS ACLs.
    tmp_file_path = './tmp/' + file_name
    with open(tmp_file_path, 'w') as tmp_file:
        tmp_file.write(sample_content)
    
    # Here we simulate setting UNIX permissions on the temporary file
    os.chmod(tmp_file_path, 0o755)
    
    # Getting the stat information from the temporary file to retrieve file system attributes
    st = os.stat(tmp_file_path)
    
    # Simulating the preservation of some attributes (e.g., st_mode contains the Unix permissions)
    info.external_attr = st.st_mode << 16  # Unix attributes, including permissions
    
    # Write the file (with simulated preserved attributes) to the zip
    with open(tmp_file_path, 'rb') as file_data:
        zipf.writestr(info, file_data.read())

    # Clean up the temporary file
    os.remove(tmp_file_path)

print("ZIP file with extended metadata and simulated file system attributes preservation has been created.")