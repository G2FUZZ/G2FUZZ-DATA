import os

# Generate metadata information
metadata_info = {
    "dimensions": (1024, 768),
    "color_space": "RGB",
    "compression_method": "lossless"
}

# Save metadata to pixdata file
file_path = "./tmp/pixdata_metadata.txt"
with open(file_path, "w") as file:
    for key, value in metadata_info.items():
        file.write(f"{key}: {value}\n")

print(f"Metadata information saved to {file_path}")