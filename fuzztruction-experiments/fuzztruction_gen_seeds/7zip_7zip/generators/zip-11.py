import os
import zipfile

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a zip file with various compression levels
def create_zip_with_compression_levels():
    # Content to be zipped
    file_content = b"Sample content for compression in ZIP file. This content will be compressed at various levels."
    file_name = "sample.txt"

    # Compression levels range from 0 (no compression) to 9 (maximum compression)
    for compression_level in range(10):
        zip_file_name = f"./tmp/compression_level_{compression_level}.zip"
        
        # Open the ZIP file in write mode
        with zipfile.ZipFile(zip_file_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
            # Writing the file with the specific compression level
            zip_info = zipfile.ZipInfo(file_name)
            zip_info.compress_type = zipfile.ZIP_DEFLATED
            zip_info.compress_size = compression_level
            zipf.writestr(zip_info, file_content)
        
        print(f"Zip file created with compression level {compression_level}: {zip_file_name}")

create_zip_with_compression_levels()