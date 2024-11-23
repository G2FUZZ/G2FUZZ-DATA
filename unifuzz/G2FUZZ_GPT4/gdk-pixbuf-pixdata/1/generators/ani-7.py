import os
from struct import pack

def create_ani_file(file_path, rate=60, play_count=0):
    """
    Create an .ani file with embedded rate information and playback behavior.

    :param file_path: Path to save the .ani file
    :param rate: Frame rate in milliseconds. Default is 60ms.
    :param play_count: Number of times the animation should play. 0 for infinite loop. Default is 0.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # ANI Header (Riff header, ACON chunk, LIST chunk for info header, INAM chunk, IART chunk, RATE chunk, SEQ chunk)
    # This is a simplified structure and might need adjustments for actual use.
    header = b'RIFF' + pack('<I', 36) + b'ACONLIST' + pack('<I', 4) + b'INFOINAM' + pack('<I', 10) + b'AnimationIART' + pack('<I', 12) + b'CreatedByPythonRATE' + pack('<I', 4) + pack('<I', rate) + b'SEQ ' + pack('<I', 4) + pack('<I', play_count)
    # Frame data (anih chunk) - this is a placeholder for the sake of example
    # An actual implementation would need valid frame data
    anih = b'anih' + pack('<I', 36) + pack('<I', 36) + pack('<I', rate) + pack('<I', play_count)
    
    with open(file_path, 'wb') as f:
        # Write the header and anih chunks
        f.write(header)
        f.write(anih)
        # Placeholder for frame data - in a real scenario, frame data would go here
        f.write(b'\x00' * 100)  # Placeholder for frame data

# Example usage
file_path = './tmp/example.ani'
create_ani_file(file_path)
print(f"ANI file created at: {file_path}")