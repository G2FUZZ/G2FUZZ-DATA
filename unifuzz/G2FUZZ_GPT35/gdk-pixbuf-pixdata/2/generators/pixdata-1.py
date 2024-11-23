import os

# Define file header information
file_headers = {
    "pixdata1.dat": {
        "file_format_version": "1.0",
        "data_type": "image",
        "dimensions": (128, 128)
    },
    "pixdata2.dat": {
        "file_format_version": "2.0",
        "data_type": "text",
        "dimensions": (256, 256)
    }
}

# Create a directory to store the files
os.makedirs("tmp", exist_ok=True)

# Generate pixdata files with file headers
for filename, header_info in file_headers.items():
    with open(f"tmp/{filename}", "w") as file:
        file.write(f"File Format Version: {header_info['file_format_version']}\n")
        file.write(f"Data Type: {header_info['data_type']}\n")
        file.write(f"Dimensions: {header_info['dimensions']}\n")

print("pixdata files generated and saved in ./tmp/")