import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Path to the new ANI file
ani_file_path = './tmp/sample.ani'

# ANI file structure components
riff_header = b'RIFF'
list_header = b'ACON'
anih_chunk_id = b'anih'
anih_chunk_data = b'\x00' * 36  # Placeholder for ANI header structure (36 bytes for minimal example)
rate_chunk_id = b'rate'
rate_chunk_data = b'\x00\x00\x00\x00'  # Placeholder for frame display rate (4 bytes for one frame, as an example)
seq_chunk_id = b'seq '
seq_chunk_data = b'\x00\x00\x00\x00'  # Placeholder for sequence data (4 bytes for one frame, as an example)

# Calculate chunk sizes
anih_chunk_size = len(anih_chunk_data).to_bytes(4, byteorder='little')
rate_chunk_size = len(rate_chunk_data).to_bytes(4, byteorder='little')
seq_chunk_size = len(seq_chunk_data).to_bytes(4, byteorder='little')

# Calculate the overall file size (4 bytes for 'RIFF', 4 bytes for the size, rest is the data)
file_size = (4 + len(list_header) + 
             4 + len(anih_chunk_id) + len(anih_chunk_size) + len(anih_chunk_data) + 
             4 + len(rate_chunk_id) + len(rate_chunk_size) + len(rate_chunk_data) + 
             4 + len(seq_chunk_id) + len(seq_chunk_size) + len(seq_chunk_data)).to_bytes(4, byteorder='little')

# Write the ANI file
with open(ani_file_path, 'wb') as ani_file:
    ani_file.write(riff_header)
    ani_file.write(file_size)
    ani_file.write(list_header)
    ani_file.write(anih_chunk_id)
    ani_file.write(anih_chunk_size)
    ani_file.write(anih_chunk_data)
    ani_file.write(rate_chunk_id)
    ani_file.write(rate_chunk_size)
    ani_file.write(rate_chunk_data)
    ani_file.write(seq_chunk_id)
    ani_file.write(seq_chunk_size)
    ani_file.write(seq_chunk_data)

print(f"ANI file created at {ani_file_path}")