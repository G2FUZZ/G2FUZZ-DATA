import zipfile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path for the ZIP file to create
zip_path = './tmp/error_detection_and_correction.zip'

# Create a ZIP file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # For demonstration, let's create a text file to add to the ZIP
    # This simulates adding a file to the ZIP for which a checksum will be generated
    text_file_content = "This is a test file to demonstrate checksum in ZIP."
    text_file_name = 'test.txt'
    with open(text_file_name, 'w') as f:
        f.write(text_file_content)
    
    # Add the file to the ZIP
    zipf.write(text_file_name, arcname=text_file_name)
    
    # After adding, the checksum is automatically calculated and stored by the ZIP library

# Clean up the text file used for demonstration
os.remove(text_file_name)

print(f"ZIP file created at {zip_path}")