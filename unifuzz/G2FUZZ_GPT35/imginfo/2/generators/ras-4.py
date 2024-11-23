import os

# Function to perform Run-Length Encoding compression
def rle_compress(input_string):
    compressed_string = ""
    i = 0
    while i < len(input_string):
        count = 1
        while i + count < len(input_string) and input_string[i] == input_string[i + count]:
            count += 1
        compressed_string += input_string[i] + str(count)
        i += count
    return compressed_string

# Generate content for the 'ras' file
content = "4. Compression: Can be compressed using RLE (Run-Length Encoding) compression."

# Compress the content using RLE compression
compressed_content = rle_compress(content)

# Create a directory if it doesn't exist
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the compressed content into a 'ras' file
file_path = os.path.join(directory, "generated_file.ras")
with open(file_path, "w") as file:
    file.write(compressed_content)

print("Generated 'ras' file saved at:", file_path)