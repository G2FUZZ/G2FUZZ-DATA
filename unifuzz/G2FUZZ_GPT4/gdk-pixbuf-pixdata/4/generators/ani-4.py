import os

def create_ani_file(filepath, hotspot=(0, 0)):
    # ANI Header (RIFF, ACON - Animation Content)
    header = b'RIFF\x9a\x00\x00\x00ACONanih(\x00\x00\x00\x24\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00'
    header += (hotspot[0].to_bytes(4, byteorder='little') + hotspot[1].to_bytes(4, byteorder='little'))
    header += b'\x00\x00\x00\x00\x01\x00\x00\x00rate\x04\x00\x00\x00\x00\x00\x00\x00seq \x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00'
    
    # Frame Icons (LIST, INAM - Icon Name, IART - Artist)
    frame_data = b'LISTl\x00\x00\x00framicon\xd2\x00\x00\x00INAM\x0e\x00\x00\x00Example Frame\x00IART\x12\x00\x00\x00Example Artist\x00'
    
    # Icon Image Data (Contains a minimal ICONDIR and ICONDIRENTRY)
    # This part should be replaced with actual icon image data for real usage
    icon_data = b'\x00\x00\x01\x00\x01\x00\x20\x20\x10\x00\x00\x00\x00\x00\x68\x01\x00\x00\x16\x00\x00\x00\x28\x00\x00\x00\x20\x00\x00\x00@\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x01\x00\x00D\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00'
    
    # Combine all parts
    ani_data = header + frame_data + icon_data
    
    # Write the data to an .ani file
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        f.write(ani_data)

create_ani_file('./tmp/example.ani', hotspot=(10, 10))