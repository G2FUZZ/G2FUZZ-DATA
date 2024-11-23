import os
from struct import pack

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# ANI header constants
anih_header = pack('I', 36)  # cbSize of the ANIHeader structure
anih_frames = pack('I', 10)  # cFrames
anih_steps = pack('I', 10)  # cSteps
anih_width = pack('I', 32)  # cx, icon width
anih_height = pack('I', 32)  # cy, icon height
anih_bit_count = pack('I', 0)  # cBitCount, 0 indicates it's the same as the icon it's displaying
anih_planes = pack('I', 0)  # cPlanes, 0 indicates it's the same as the icon it's displaying
anih_display_rate = pack('I', 60)  # JifRate, display rate in jiffies (1/60th of a second)
anih_flags = pack('I', 1)  # Flags, 1 indicates the ANI is sequenced

# Create a simple ANI file
def create_ani_file(filename):
    with open(f'./tmp/{filename}.ani', 'wb') as f:
        # Write RIFF header
        f.write(b'RIFF')
        f.write(pack('I', 0))  # Placeholder for file size
        f.write(b'ACON')

        # Write ANI header chunk
        f.write(b'anih')
        f.write(anih_header)
        f.write(anih_frames)
        f.write(anih_steps)
        f.write(anih_width)
        f.write(anih_height)
        f.write(anih_bit_count)
        f.write(anih_planes)
        f.write(anih_display_rate)
        f.write(anih_flags)

        # Placeholder for list and icon chunks, for simplicity, we're not including actual image data
        # In a complete implementation, LIST chunks with icon data would follow here

        # Go back and update the file size in the RIFF header
        f.seek(4)
        file_size = f.tell()
        f.seek(0, os.SEEK_END)
        file_size = f.tell() - 8  # Subtract the RIFF header size
        f.seek(4)
        f.write(pack('I', file_size))

# Example: Create an ANI file
create_ani_file('example_cursor')