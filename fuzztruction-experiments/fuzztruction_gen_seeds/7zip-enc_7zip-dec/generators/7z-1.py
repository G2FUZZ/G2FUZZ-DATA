import py7zr
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 7z archive path
archive_path = './tmp/high_compression.7z'

# Create an empty 7z archive with high compression settings
with py7zr.SevenZipFile(archive_path, 'w', filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9}]) as archive:
    # Normally, you would add files to the archive here using archive.writeall() or similar methods.
    # However, since we are not adding any files, we simply close the archive.
    pass

print(f"Created an empty 7z archive with high compression at {archive_path}")