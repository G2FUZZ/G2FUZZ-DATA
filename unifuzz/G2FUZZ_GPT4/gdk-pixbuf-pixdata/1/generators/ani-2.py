import os

def create_ani_file(filepath, frame_durations):
    # ANI header structure: RIFF header, then ANI header
    # This is a very simplified version and might not work for all viewers
    # as real .ani files require specific chunks like 'anih', 'rate', 'seq ', and 'icon' frames.

    # RIFF header
    riff = b'RIFF'
    list_type = b'ACON'

    # ANIH chunk (header)
    anih_chunk_id = b'anih'
    anih_chunk_size = 36  # The size of the ANI header chunk
    anih_header_data = b'\x28\x00\x00\x00'  # Header size
    anih_header_data += b'\x02\x00\x00\x00'  # Number of frames (hardcoded for simplicity)
    anih_header_data += b'\x02\x00\x00\x00'  # Number of steps (hardcoded for simplicity)
    anih_header_data += b'\x00\x00\x00\x00' * 5  # Other header data, filled with zeros for simplicity

    # RATE chunk (how long each frame should be displayed, in milliseconds)
    rate_chunk_id = b'rate'
    rate_chunk_data = bytearray()
    for duration in frame_durations:
        rate_chunk_data += duration.to_bytes(4, byteorder='little')

    rate_chunk_size = len(rate_chunk_data)

    # SEQ chunk (the sequence in which frames should be displayed)
    # For simplicity, we'll just display frames in the order they appear
    seq_chunk_id = b'seq '
    seq_chunk_size = 8  # For 2 frames, each frame index is 4 bytes
    seq_chunk_data = b'\x00\x00\x00\x00\x01\x00\x00\x00'

    # Calculate total size for the RIFF chunk
    riff_size = 4 + (4 + 4 + anih_chunk_size) + (4 + 4 + rate_chunk_size) + (4 + 4 + seq_chunk_size)

    # Open file and write the binary data
    with open(filepath, 'wb') as f:
        f.write(riff)
        f.write(riff_size.to_bytes(4, byteorder='little'))
        f.write(list_type)
        f.write(anih_chunk_id)
        f.write(anih_chunk_size.to_bytes(4, byteorder='little'))
        f.write(anih_header_data)
        f.write(rate_chunk_id)
        f.write(rate_chunk_size.to_bytes(4, byteorder='little'))
        f.write(rate_chunk_data)
        f.write(seq_chunk_id)
        f.write(seq_chunk_size.to_bytes(4, byteorder='little'))
        f.write(seq_chunk_data)  # Corrected to use the defined variable

# Example usage
# Make sure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)
# Define frame durations in milliseconds
frame_durations = [1000, 500]  # Example: First frame 1000ms, second frame 500ms
create_ani_file('./tmp/example.ani', frame_durations)