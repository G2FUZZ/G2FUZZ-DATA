import os
import struct

def create_ani_file(rate_of_change, filename="animated_cursor.ani"):
    # Ensure the ./tmp/ directory exists
    os.makedirs("./tmp/", exist_ok=True)
    filepath = os.path.join("./tmp/", filename)

    # ANI header structure: RIFF, ACON, LIST, INAM, IART, rate chunk, seq chunk
    # Simplified example, real .ani files require more detailed headers and actual image data

    # RIFF header
    riff = b'RIFF'
    list_type = b'ACON'

    # INAM chunk (name), IART chunk (author), just placeholders
    inam_chunk = b'INAM' + struct.pack('<I', 11) + b'Example Cursor'
    iart_chunk = b'IART' + struct.pack('<I', 12) + b'Example Author'

    # Rate chunk - setting the integrated rate of change
    rate_chunk = b'rate' + struct.pack('<I', 4 * 1)  # 1 frame in this example, adjust as necessary
    rate_data = struct.pack('<I', rate_of_change)  # Rate of change value

    # Seq chunk - sequence of frames (simplified)
    seq_chunk = b'seq ' + struct.pack('<I', 4 * 1)  # 1 frame in this example
    seq_data = struct.pack('<I', 0)  # Frame sequence, simplified

    # Calculating total size for the RIFF chunk
    total_size = 4 + (4 + 4) + len(inam_chunk) + len(iart_chunk) + len(rate_chunk) + 4 + len(seq_chunk) + 4 + len(rate_data) + len(seq_data)

    # Writing the .ani file
    with open(filepath, 'wb') as f:
        f.write(riff)
        f.write(struct.pack('<I', total_size))
        f.write(list_type)
        f.write(inam_chunk)
        f.write(iart_chunk)
        f.write(rate_chunk)
        f.write(rate_data)
        f.write(seq_chunk)
        f.write(seq_data)

    print(f"ANI file created at: {filepath}")

# Example usage: create an .ani file with a rate of change of 60 (you can adjust this value)
create_ani_file(60, "custom_rate_cursor.ani")