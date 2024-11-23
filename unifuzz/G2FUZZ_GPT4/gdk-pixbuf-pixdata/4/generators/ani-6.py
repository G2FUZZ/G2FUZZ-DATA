import os
from struct import pack

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def create_ani_file(file_path, sizes):
    """
    Creates an ANI file with cursors of variable sizes.
    
    :param file_path: The path to save the ANI file.
    :param sizes: A list of (width, height) tuples for each cursor size.
    """
    # ANI Header structure
    RIFF = b'RIFF'
    ACON = b'ACON'
    anih = b'anih'
    rate = b'rate'
    seq = b'seq '
    LIST = b'LIST'
    fram = b'fram'
    
    # Create a basic anih (ANI header) chunk
    # header size, frames, steps, width, height, bit count, planes, jif rate, flags
    anih_chunk = pack('<Iiiiiiiii', 36, len(sizes), len(sizes), 32, 32, 24, 1, 60, 1)
    
    # Create rate and seq chunks
    rate_chunk = pack('<' + 'i' * len(sizes), *[60]*len(sizes))  # 60 jiffies (1 second) for each frame
    seq_chunk = pack('<' + 'i' * len(sizes), *range(len(sizes)))  # Sequence of frames
    
    # Dummy cursor data for each size
    cursor_data = []
    for width, height in sizes:
        # For simplicity, generate a dummy cursor for each size
        cursor_data.append(b'CUR ' + pack('<I', width*height*3) + b'\x00'*width*height*3)
    
    # Calculate the total size of the LIST chunk
    list_chunk_size = sum(len(data) for data in cursor_data) + 4
    
    # Open the file and write the chunks
    with open(file_path, 'wb') as f:
        f.write(RIFF)
        f.write(pack('<I', 4 + 4 + 4 + len(anih_chunk) + 4 + len(rate_chunk) + 4 + len(seq_chunk) + 4 + 4 + list_chunk_size))
        f.write(ACON)
        f.write(anih)
        f.write(pack('<I', len(anih_chunk)))
        f.write(anih_chunk)
        f.write(rate)
        f.write(pack('<I', len(rate_chunk)))
        f.write(rate_chunk)
        f.write(seq)
        f.write(pack('<I', len(seq_chunk)))
        f.write(seq_chunk)
        f.write(LIST)
        f.write(pack('<I', list_chunk_size))
        f.write(fram)
        for data in cursor_data:
            f.write(data)

# Define sizes (width, height) for variable size cursors
sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64)]

# Create an ANI file with variable size cursors
create_ani_file('./tmp/variable_size_cursors.ani', sizes)