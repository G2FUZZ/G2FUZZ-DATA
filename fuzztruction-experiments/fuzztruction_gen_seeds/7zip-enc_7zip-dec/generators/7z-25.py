import py7zr
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 7z archive path for high compression with recovery record
archive_path_with_recovery = './tmp/high_compression_with_recovery.7z'

# py7zr does not directly support adding a recovery record as RAR archives do.
# However, enhancing resilience can be somewhat achieved through the use of solid block size configurations and redundancy.
# This example continues to focus on high compression and does not directly add a recovery record,
# as the feature is not explicitly supported by py7zr or the 7z format through the library's API.

# For demonstration, we will use high compression settings similar to the previous example.
with py7zr.SevenZipFile(archive_path_with_recovery, 'w', filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9}]) as archive:
    # Normally, you would add files here. The example continues without adding files for simplicity.
    pass

print(f"Created a 7z archive aiming for high resilience at {archive_path_with_recovery}")

# Note: This code does not explicitly add a recovery record as the feature is not directly supported by py7zr.
# It is important to consider other methods for data resilience and backup.