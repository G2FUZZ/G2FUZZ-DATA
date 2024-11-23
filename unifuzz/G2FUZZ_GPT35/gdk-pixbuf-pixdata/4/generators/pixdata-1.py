import os

# Define the file header metadata
file_header = {
    "version": "1.0",
    "data_type": "image",
    "compression": "gzip"
}

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the file header into a pixdata file
with open('./tmp/pixdata.txt', 'w') as file:
    file.write("File Header:\n")
    for key, value in file_header.items():
        file.write(f"{key}: {value}\n")

print("pixdata file generated and saved successfully.")