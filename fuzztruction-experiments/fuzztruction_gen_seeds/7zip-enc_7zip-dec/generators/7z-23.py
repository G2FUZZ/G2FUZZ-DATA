import py7zr
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 7z archive path
archive_path = './tmp/high_compression_multithreading.7z'

# Configure filters with multi-threading support. The 'preset' parameter controls the compression level,
# and 'threads' parameter enables multi-threading. If 'threads' is set to 0, py7zr will use the number of
# CPU cores.
compression_filters = [
    {'id': py7zr.FILTER_LZMA2, 'preset': 9, 'threads': 0}
]

# Create a 7z archive with high compression settings and multi-threading support
with py7zr.SevenZipFile(archive_path, 'w', filters=compression_filters) as archive:
    # Normally, you would add files to the archive here using archive.writeall() or similar methods.
    # However, since we are not adding any files, we simply close the archive.
    pass

print(f"Created a 7z archive with high compression and multi-threading support at {archive_path}")