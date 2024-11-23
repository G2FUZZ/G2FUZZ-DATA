import zipfile
from pathlib import Path

# Ensure the ./tmp/ directory exists
Path("./tmp/").mkdir(parents=True, exist_ok=True)

# Define the path for the new ZIP file
zip_path = "./tmp/features_support示例.zip"

# Create a new ZIP file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # A file name with Unicode characters for the first file
    unicode_filename = "示例文档.txt"
    # Content for the first file inside the ZIP
    unicode_content = "This is a demonstration of ZIP's Unicode support."
    # Writing the content to the first file inside the ZIP
    zipf.writestr(unicode_filename, unicode_content)
    
    # A file name for the second file with the feature description
    feature_filename = "Streaming Support.txt"
    # Description for the `Streaming Support` feature
    feature_content = """2. **Streaming Support**: ZIP files can be created and extracted in a streaming mode, allowing them to be read and written sequentially without needing random access, useful for network transfers and low-memory situations."""
    # Writing the description to the second file inside the ZIP
    zipf.writestr(feature_filename, feature_content)

print(f"ZIP file created at: {zip_path}")