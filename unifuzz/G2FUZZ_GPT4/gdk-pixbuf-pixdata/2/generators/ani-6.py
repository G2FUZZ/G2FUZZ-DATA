import os
import struct

def create_ani_file(filename):
    # ANI header structure: RIFF, list, aniheader, rate, seq, and then the actual icon images (as Ico files in bytes)
    # For simplicity, this example uses a minimal approach and does not include actual icon images.
    # It focuses on the structure needed to loop through a sequence of frames.

    # Header for an empty ani file with sequence cycling
    header = b'RIFF' + struct.pack('<I', 36) + b'ACONLIST' + struct.pack('<I', 16) + b'anih' + struct.pack('<I', 36)
    anih_header = struct.pack('<IIIIIIII', 36, 36, 0, 0, 2, 2, 0, 0)  # ANIHeader: cbSize, nFrames, nSteps, etc.
    rate_chunk = b'rate' + struct.pack('<I', 8) + struct.pack('<II', 60, 60)  # Rate for each frame (60/60ths of a second)
    seq_chunk = b'seq ' + struct.pack('<I', 8) + struct.pack('<II', 0, 1)  # Sequence of frames (cycling two frames)

    # Concatenate parts
    ani_file_content = header + anih_header + rate_chunk + seq_chunk

    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Write the ani file
    with open(f'./tmp/{filename}.ani', 'wb') as f:
        f.write(ani_file_content)

create_ani_file('animated_cursor')