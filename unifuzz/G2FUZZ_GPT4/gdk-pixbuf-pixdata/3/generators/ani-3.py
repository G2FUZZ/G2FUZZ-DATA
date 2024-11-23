import os
import struct

def create_ani_file(file_path, frame_rate):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # RIFF header
    riff = b'RIFF'
    # Placeholder for file size, will be updated later
    size = struct.pack('<I', 0)
    acn_type = b'ACON'
    
    # ANI header (anih)
    anih_chunk_id = b'anih'
    anih_chunk_size = struct.pack('<I', 36)  # Size of anih chunk
    header_length = struct.pack('<I', 36)  # Header length
    num_frames = struct.pack('<I', 1)  # Number of frames
    num_steps = struct.pack('<I', 1)  # Number of steps (for cycling)
    width = struct.pack('<I', 32)  # Width of frame (pixels)
    height = struct.pack('<I', 32)  # Height of frame (pixels)
    bit_count = struct.pack('<I', 0)  # Color depth (0 for default)
    num_planes = struct.pack('<I', 1)  # Number of color planes
    display_rate = struct.pack('<I', frame_rate)  # Frame display rate (jiffies)
    flags = struct.pack('<I', 1)  # ANI flag (1 for icon sequence)
    
    # Construct the ANI header chunk
    anih_chunk = anih_chunk_id + anih_chunk_size + header_length + num_frames + num_steps + width + height + bit_count + num_planes + display_rate + flags
    
    # For simplicity, this example does not include actual frame data.
    # Normally, you would include LIST chunks with icon data here.

    # Calculate the total file size and update the size field
    total_size = 4 + len(anih_chunk)  # RIFF type and anih chunk
    size = struct.pack('<I', total_size - 8)  # Exclude RIFF header size itself
    
    # Write the file
    with open(file_path, 'wb') as f:
        f.write(riff + size + acn_type + anih_chunk)

# Usage example
create_ani_file('./tmp/example.ani', frame_rate=10)