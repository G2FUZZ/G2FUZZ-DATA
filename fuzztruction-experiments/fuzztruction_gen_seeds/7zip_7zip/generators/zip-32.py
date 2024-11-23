import zipfile
from pathlib import Path

# Ensure the ./tmp/ directory exists
Path("./tmp/").mkdir(parents=True, exist_ok=True)

# Define the path for the new ZIP file
zip_path = "./tmp/unicode_support示例_with_zip64.zip"

# Create a new ZIP file with Zip64 extension enabled
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
    # A file name with Unicode characters
    unicode_filename = "示例文档.txt"
    # Content for the file inside the ZIP
    content = "This is a demonstration of ZIP's Unicode support."
    # Writing the content to a file inside the ZIP
    zipf.writestr(unicode_filename, content)
    
    # Adding Zip64 demonstration (This is a conceptual demonstration. Actual Zip64 benefits kick in with large files or numerous entries)
    # For a real-world scenario, one would add files that exceed 4GB in size or add more than 65,535 files to see Zip64 in action.
    zipf.writestr("zip64_demo.txt", "This file serves as a placeholder to demonstrate Zip64 support.")

print(f"ZIP file created at: {zip_path}")