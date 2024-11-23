import os

# Create a directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Generate 'ras' files with metadata
metadata = {
    "resolution": "1024x768",
    "creation_date": "2022-10-12",
    "author": "John Doe"
}

for i in range(3):
    filename = f"./tmp/file{i+1}.ras"
    with open(filename, 'w') as file:
        file.write("Metadata:\n")
        for key, value in metadata.items():
            file.write(f"{key}: {value}\n")