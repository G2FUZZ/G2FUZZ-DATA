import zlib

# Generate data to store in the 'ani' file
data = b"Example data to be stored in the 'ani' file with compression."

# Compress the data using zlib compression
compressed_data = zlib.compress(data)

# Save the compressed data into a file with a '.ani' extension in the './tmp/' directory
file_path = "./tmp/example.ani"
with open(file_path, "wb") as file:
    file.write(compressed_data)

print(f"File saved at: {file_path}")