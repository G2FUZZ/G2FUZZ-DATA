import os
from struct import pack

def create_complex_ani_file(file_path, icon_paths, rates=None, play_count=0):
    """
    Create a more complex .ani file with actual frame data from .ico files, custom frame rates for each frame,
    and specific playback behavior.

    :param file_path: Path to save the .ani file.
    :param icon_paths: List of paths to .ico files to be used as frames in the animation.
    :param rates: List of frame rates in milliseconds for each frame. If None, a default rate is used for all frames.
    :param play_count: Number of times the animation should play. 0 for infinite loop. Default is 0.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    if rates is None:
        rates = [60] * len(icon_paths)  # Default rate of 60ms for each frame if rates not provided
    
    # Calculate total size of RATE chunk and SEQ chunk
    rate_chunk_size = 4 + (4 * len(rates))  # 4 bytes for each rate plus 4 bytes for the chunk size field
    seq_chunk_size = 4 + (4 * len(icon_paths))  # Assuming sequence numbers are incremental
    
    # ANI Header components
    riff_header = b'RIFF'
    acon_chunk = b'ACON'
    list_chunk = b'LIST' + pack('<I', 12 + len(file_path))  # Adjust size for INAM chunk content
    inam_chunk = b'INAM' + pack('<I', len(file_path)) + file_path.encode('utf-8')
    
    # RATE and SEQ chunks
    rate_chunk = b'RATE' + pack('<I', rate_chunk_size) + b''.join([pack('<I', rate) for rate in rates])
    seq_chunk = b'SEQ ' + pack('<I', seq_chunk_size) + b''.join([pack('<I', i) for i in range(len(icon_paths))])
    
    # Frame data
    frames_data = b''
    for icon_path in icon_paths:
        if not os.path.exists(icon_path):
            print(f"Error: Icon file not found: {icon_path}")
            return  # Exit the function if a file is missing
        with open(icon_path, 'rb') as icon_file:
            frames_data += icon_file.read()
    
    # Calculating file and chunk sizes
    acon_chunk_size = 4 + (12 + len(file_path)) + rate_chunk_size + seq_chunk_size + len(frames_data)
    total_size = 4 + acon_chunk_size
    
    # Final assembly of the ANI file
    header = riff_header + pack('<I', total_size) + acon_chunk + list_chunk + inam_chunk + rate_chunk + seq_chunk
    
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(frames_data)
    
    print(f"Complex ANI file created at: {file_path}")

# Example usage
file_path = './tmp/complex_example.ani'
icon_paths = ['./frame1.ico', './frame2.ico']
create_complex_ani_file(file_path, icon_paths)