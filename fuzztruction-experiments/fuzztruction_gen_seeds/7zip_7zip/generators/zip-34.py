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

def create_zip_with_volume_label_preservation():
    # Content to be zipped
    file_content = b"Sample content for a ZIP file with Volume Label Preservation."
    file_name = "sample.txt"
    volume_label = "VOLUME_LABEL"

    # File name for the zip with Volume Label Preservation
    zip_file_name = "./tmp/zip_with_volume_label.zip"
    
    # Open the ZIP file in write mode
    with zipfile.ZipFile(zip_file_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5) as zipf:
        # Writing the file
        zip_info = zipfile.ZipInfo(file_name)
        zip_info.compress_type = zipfile.ZIP_DEFLATED
        zipf.writestr(zip_info, file_content)
        
        # Volume Label Preservation
        # Note: The zipfile library doesn't support adding a volume label directly.
        # As an alternative, we can add a file that acts as a placeholder for the volume label.
        # This workaround doesn't truly preserve the volume label in the ZIP metadata,
        # but allows us to include the label information in a recognizable way within the ZIP.
        volume_label_info = zipfile.ZipInfo(volume_label)
        zipf.writestr(volume_label_info, b"")  # Writing an empty file as a placeholder for the volume label
    
    print(f"Zip file created with Volume Label Preservation: {zip_file_name}")

create_zip_with_compression_levels()
create_zip_with_volume_label_preservation()