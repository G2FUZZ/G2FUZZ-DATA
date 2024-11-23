import os
import struct

def create_rle_compressed_tga(data, width, height, filepath):
    """
    Create a TGA file with RLE compression.

    :param data: Pixel data in (R, G, B) format.
    :param width: Image width.
    :param height: Image height.
    :param filepath: Path to save the TGA file.
    """
    header = bytearray(18)
    
    # Set image dimensions
    header[12:14] = struct.pack('<H', width)
    header[14:16] = struct.pack('<H', height)
    header[2] = 10  # Image type: RLE Truecolor
    header[16] = 24  # Bits per pixel

    with open(filepath, 'wb') as f:
        f.write(header)  # Write the header
        
        i = 0
        while i < len(data):
            # Check how many consecutive pixels are the same
            count = 1
            while i + count < len(data) and data[i] == data[i + count] and count < 128:
                count += 1
            
            if count > 1:  # We have a run of the same pixel
                # Write packet header
                f.write(struct.pack('B', 0x80 | (count - 1)))
                # Write pixel data
                f.write(bytes(data[i]))
                i += count
            else:  # No run, write raw packet
                # Find run of unique pixels
                start = i
                i += 1
                while i < len(data) and (i + 1 >= len(data) or data[i] != data[i + 1]) and (i - start) < 127:
                    i += 1
                
                # Write packet header
                f.write(struct.pack('B', i - start - 1))
                # Write pixel data
                for j in range(start, i):
                    f.write(bytes(data[j]))

# Example usage
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Example data: A simple gradient
width, height = 100, 100
data = [(i % 256, i % 256, i % 256) for i in range(width * height)]

create_rle_compressed_tga(data, width, height, './tmp/example_rle.tga')