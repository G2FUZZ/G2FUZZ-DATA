import os
import struct

def create_ani_file(filename, author="Author Name", copyright="Copyright Info", description="Cursor Description"):
    # Create the directory if it doesn't exist
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    with open(filepath, 'wb') as f:
        # ANI Header
        # RIFF header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 0))  # Placeholder for file size
        f.write(b'ACON')

        # ANI Header chunk
        f.write(b'anih')
        f.write(struct.pack('<I', 36))  # Chunk size
        f.write(struct.pack('<I', 36))  # Header size
        f.write(struct.pack('<I', 0))   # Number of frames
        f.write(struct.pack('<I', 0))   # Number of steps
        f.write(struct.pack('<I', 0))   # Width
        f.write(struct.pack('<I', 0))   # Height
        # ... Other header fields (bit count, planes, display rate, flags)
        f.write(struct.pack('<I', 0) * 4)

        # Extended metadata chunk (LIST chunk containing INFO subchunks)
        # LIST chunk header
        f.write(b'LIST')
        list_chunk_start = f.tell()
        f.write(struct.pack('<I', 0))  # Placeholder for chunk size
        f.write(b'INFO')

        # Writing author metadata
        # INAM chunk for description
        f.write(b'INAM')
        description_bytes = description.encode('utf-8')
        f.write(struct.pack('<I', len(description_bytes)))
        f.write(description_bytes)

        # IART chunk for author
        f.write(b'IART')
        author_bytes = author.encode('utf-8')
        f.write(struct.pack('<I', len(author_bytes)))
        f.write(author_bytes)

        # ICOP chunk for copyright
        f.write(b'ICOP')
        copyright_bytes = copyright.encode('utf-8')
        f.write(struct.pack('<I', len(copyright_bytes)))
        f.write(copyright_bytes)

        # Update LIST chunk size
        list_chunk_size = f.tell() - list_chunk_start - 4
        f.seek(list_chunk_start)
        f.write(struct.pack('<I', list_chunk_size))
        f.seek(0, os.SEEK_END)

        # Update RIFF chunk size
        file_size = f.tell()
        f.seek(4)
        f.write(struct.pack('<I', file_size - 8))

    print(f"ANI file '{filename}' with extended metadata created in ./tmp/")

# Example usage
create_ani_file('example.ani', author="John Doe", copyright="© 2023", description="Sample ANI Cursor")