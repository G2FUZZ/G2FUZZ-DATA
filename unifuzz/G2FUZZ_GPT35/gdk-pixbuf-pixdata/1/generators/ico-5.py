import struct

def create_ico_file():
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, 1)
    
    # ICO Directory Entry
    ico_entry = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 0, 0, 22)
    
    # ICO Image Data (dummy data for demonstration)
    ico_data = b'\x00' * 22
    
    # Create ICO file
    with open('./tmp/compressed_icon.ico', 'wb') as f:
        f.write(ico_header)
        f.write(ico_entry)
        f.write(ico_data)

create_ico_file()