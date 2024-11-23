import struct

def create_tga_file(filename, width, height, data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, 24, 0])
    
    with open(filename, "wb") as f:
        f.write(header)
        
        for i in range(0, len(data), 3):
            f.write(bytes([data[i + 2], data[i + 1], data[i]]))

width = 100
height = 100
data = [255, 255, 255] * width * height  # White image data

filename = "./tmp/test.tga"
create_tga_file(filename, width, height, data)

print(f"TGA file '{filename}' has been created.")