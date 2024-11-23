import os
import struct

def create_ani_file(filename, loop_count=0):
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    with open(filepath, 'wb') as f:
        # ANI Header
        f.write(b'RIFF')  # Chunk ID
        f.write(struct.pack('<I', 0))  # Placeholder for file size
        f.write(b'ACON')

        # ANI LIST INFO
        f.write(b'LIST')  # List type
        f.write(struct.pack('<I', 4 + 4 + 4))  # Chunk size
        f.write(b'INFO')
        f.write(b'INAM')  # Chunk type: Title
        f.write(struct.pack('<I', 4))  # Chunk size
        f.write(b'ANIC')  # Animation name
        f.write(b'IART')  # Chunk type: Artist
        f.write(struct.pack('<I', 4))  # Chunk size
        f.write(b'NONE')  # Artist name

        # ANI LIST fram
        # This is a simplistic representation. Normally, you'd include actual frame data here.
        f.write(b'LIST')  # List type
        f.write(struct.pack('<I', 4))  # Placeholder for list size
        f.write(b'fram')

        # ANI frame data would go here

        # ANI ani header (a rate chunk and a seq chunk might also be included for a full implementation)
        f.write(b'anih')  # Chunk ID
        ani_header_size = 36  # The size of the ANI header
        f.write(struct.pack('<I', ani_header_size))
        f.write(struct.pack('<I', 36))  # Header size
        f.write(struct.pack('<I', 1))  # Number of frames
        f.write(struct.pack('<I', 1))  # Number of steps
        f.write(struct.pack('<I', 0))  # Width (0 if not set)
        f.write(struct.pack('<I', 0))  # Height (0 if not set)
        f.write(struct.pack('<I', 0))  # Bit count (0 if not set)
        f.write(struct.pack('<I', 1))  # Number of planes
        f.write(struct.pack('<I', 1))  # Display rate (jiffies)
        f.write(struct.pack('<I', loop_count))  # Total number of animation cycles

        # Calculate & update the file size
        f.seek(0, 2)  # Move to the end of the file
        file_size = f.tell() - 8  # Total file size minus RIFF header size
        f.seek(4)  # Move to file size position
        f.write(struct.pack('<I', file_size))

if __name__ == "__main__":
    create_ani_file('example.ani', loop_count=0)  # Change loop_count as needed