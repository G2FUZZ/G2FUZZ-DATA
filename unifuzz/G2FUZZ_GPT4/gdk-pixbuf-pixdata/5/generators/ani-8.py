import os
from struct import pack

def create_ani_file(file_path, frame_rate=60):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # ANI Header structure: RIFF, LIST, anih (with header data), rate, seq, and LIST of frames (icon)
    # This is a simplified version focusing on embedding rate control
    riff_header = b'RIFF'
    list_header = b'LIST'
    ani_header = b'ACON'
    anih_chunk = b'anih'
    rate_chunk = b'rate'
    seq_chunk = b'seq '
    list_frames = b'fram'
    
    # anih_chunk data: cbSize, nNumFrames, nNumSteps, iWidth, iHeight, iBitCount, nNumPlanes, iDisplayRate, flags
    anih_data = pack('<Iiiiiiiii', 36, 2, 2, 32, 32, 8, 1, 1000//frame_rate, 1)
    
    # rate_chunk data: Assuming 2 frames, setting the same rate for simplicity
    rate_data = pack('<ii', 1000//frame_rate, 1000//frame_rate)
    
    # seq_chunk data: Assuming 2 frames, simple sequence
    seq_data = pack('<ii', 0, 1)

    # Simulated frame data for demonstration, normally you'd include actual icon data here
    frame_data = b'icon' + pack('<I', 8) + b'\x01\x02\x03\x04\x05\x06\x07\x08'

    # Calculate sizes for LIST chunks
    list_chunk_size = 4 + 4 + 4 + len(anih_data) + 4 + 4 + len(rate_data) + 4 + 4 + len(seq_data) + 4 + len(frame_data) * 2
    file_size = 4 + (4 + 4 + list_chunk_size)

    # Construct the ANI file content
    ani_content = (
        riff_header + pack('<I', file_size) + ani_header +
        list_header + pack('<I', list_chunk_size) + b'info' +
        anih_chunk + pack('<I', len(anih_data)) + anih_data +
        rate_chunk + pack('<I', len(rate_data)) + rate_data +
        seq_chunk + pack('<I', len(seq_data)) + seq_data +
        list_header + pack('<I', 8 + len(frame_data) * 2) + list_frames +
        frame_data + frame_data  # Including the same frame data twice for simplicity
    )

    # Write the ANI content to the specified file
    with open(file_path, 'wb') as f:
        f.write(ani_content)

# Example usage
create_ani_file('./tmp/example_rate_control.ani', frame_rate=60)