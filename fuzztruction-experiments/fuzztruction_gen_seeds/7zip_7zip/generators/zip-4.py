import os
import zipfile

def create_split_zip(output_dir, base_name, max_size):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a large dummy file to demonstrate splitting
    dummy_file_path = os.path.join(output_dir, "large_dummy_file.txt")
    with open(dummy_file_path, "w") as dummy_file:
        dummy_file.write("0" * 50000000)  # Adjust size to demonstrate splitting

    # Define the zip file path
    zip_file_path = os.path.join(output_dir, base_name + ".zip")

    # Create a zip file and enable splitting by specifying the max size
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
        zipf.write(dummy_file_path, arcname="large_dummy_file.txt")

    # Split the zip file into parts
    part_number = 1
    with open(zip_file_path, 'rb') as zip_source:
        chunk = zip_source.read(max_size)
        while chunk:
            with open(f"{zip_file_path}.part{part_number:03d}", 'wb') as zip_part:
                zip_part.write(chunk)
            part_number += 1
            chunk = zip_source.read(max_size)

    # Cleanup: remove the original zip and dummy file
    os.remove(zip_file_path)
    os.remove(dummy_file_path)

create_split_zip('./tmp/', 'split_archive', 1024 * 1024 * 10)  # 10MB max size for each part