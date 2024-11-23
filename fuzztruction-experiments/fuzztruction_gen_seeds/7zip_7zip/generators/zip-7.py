import zipfile
from pathlib import Path

# Ensure the ./tmp/ directory exists
Path("./tmp/").mkdir(parents=True, exist_ok=True)

# Define the path for the new ZIP file
zip_path = "./tmp/unicode_support示例.zip"

# Create a new ZIP file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # A file name with Unicode characters
    unicode_filename = "示例文档.txt"
    # Content for the file inside the ZIP
    content = "This is a demonstration of ZIP's Unicode support."
    # Writing the content to a file inside the ZIP
    zipf.writestr(unicode_filename, content)

print(f"ZIP file created at: {zip_path}")