import zipfile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path for the ZIP file to create
zip_path = './tmp/advanced_error_detection_and_correction.zip'

# Function to decide compression method based on file name or type
def select_compression(file_name):
    if file_name.endswith('.txt'):
        # High compression for text files
        return zipfile.ZIP_DEFLATED
    elif file_name.endswith('.jpg') or file_name.endswith('.png'):
        # No compression for image files, as they are already compressed
        return zipfile.ZIP_STORED
    else:
        # Default compression for other types
        return zipfile.ZIP_DEFLATED

# Create a ZIP file
with zipfile.ZipFile(zip_path, 'w') as zipf:
    # For demonstration, let's create a text file and an image file to add to the ZIP
    # This simulates adding files with selective compression
    
    # Text file
    text_file_content = "This is a text file to demonstrate selective compression in ZIP."
    text_file_name = 'test.txt'
    with open(text_file_name, 'w') as f:
        f.write(text_file_content)
    
    # Image file (dummy content, as an example)
    image_file_content = b"This is a pseudo-image file."
    image_file_name = 'image.jpg'
    with open(image_file_name, 'wb') as f:
        f.write(image_file_content)
    
    # Add files to the ZIP with selective compression
    zipf.write(text_file_name, arcname=text_file_name, compress_type=select_compression(text_file_name))
    zipf.write(image_file_name, arcname=image_file_name, compress_type=select_compression(image_file_name))
    
    # After adding, the checksums are automatically calculated and stored by the ZIP library

# Clean up the files used for demonstration
os.remove(text_file_name)
os.remove(image_file_name)

print(f"ZIP file created at {zip_path}")