import os
from struct import pack

def create_ani_file(filename):
    header = b'RIFF'
    list_type = b'ACON'
    anih = b'anih'
    rate = b'rate'
    seq = b'seq '
    fram = b'fram'
    
    # ANI header
    # DWORD cbSizeOf = 36; DWORD nFrames = 1; DWORD nSteps = 1; DWORD iWidth = 32; DWORD iHeight = 32;
    # DWORD iBitCount = 8; DWORD nPlanes = 1; DWORD iDispRate = 60; DWORD bfAttributes = 1;
    ani_header_data = pack('<I', 36) + pack('<I', 1) + pack('<I', 1) + pack('<I', 32) + pack('<I', 32) + pack('<I', 8) + pack('<I', 1) + pack('<I', 60) + pack('<I', 1)

    # RATE chunk
    # setting rate for 1 frame
    rate_data = pack('<I', 60)  # display rate in jiffies (1/60th of a second)
    
    # SEQ chunk
    # sequence for 1 frame
    seq_data = pack('<I', 0)  # sequence of frames, just one frame
    
    # FRAM chunk
    # a listicon or fram chunk can be used here, representing a single frame
    # for simplicity, using a dummy icon
    icon_data = b'\x00' * 100  # dummy icon data, replace with actual icon data

    # calculating chunk sizes
    anih_size = len(ani_header_data) + 4
    rate_size = len(rate_data) + 4
    seq_size = len(seq_data) + 4
    icon_list_size = len(icon_data) + 4
    list_size = 4 + (8 + anih_size) + (8 + rate_size) + (8 + seq_size) + (8 + icon_list_size)
    riff_size = 4 + (4 + list_size)
    
    with open(os.path.join('./tmp/', filename), 'wb') as f:
        # RIFF chunk
        f.write(header)
        f.write(pack('<I', riff_size))
        f.write(list_type)
        
        # LIST chunk
        f.write(b'LIST')
        f.write(pack('<I', list_size))
        
        # ANIH chunk
        f.write(anih)
        f.write(pack('<I', anih_size - 8))
        f.write(ani_header_data)
        
        # RATE chunk
        f.write(rate)
        f.write(pack('<I', rate_size - 8))
        f.write(rate_data)
        
        # SEQ chunk
        f.write(seq)
        f.write(pack('<I', seq_size - 8))
        f.write(seq_data)
        
        # FRAM chunk, simplistically using a dummy icon
        f.write(fram)
        f.write(pack('<I', icon_list_size - 8))
        f.write(icon_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create the ANI file
create_ani_file('example.ani')