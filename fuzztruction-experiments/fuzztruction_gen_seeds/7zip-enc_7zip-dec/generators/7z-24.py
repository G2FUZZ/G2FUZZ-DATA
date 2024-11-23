import os
from py7zr import SevenZipFile

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the 7z file
output_file_path = './tmp/extended_features.7z'

# Prepare the content to be written into the 7z file
content = {
    "feature.txt": "11. Error recovery: The format supports error recovery, which can be useful for restoring data from partially damaged archives.",
    "customizable_compression_levels.txt": "2. Customizable compression levels: Users can choose from several predefined compression levels ranging from fast compression with lower compression ratios to maximum compression with higher ratios, allowing for a tailored approach based on user needs."
}

# Create a 7z file with default compression settings
with SevenZipFile(output_file_path, 'w') as archive:
    for file_name, file_content in content.items():
        archive.writestr(file_name, file_content)