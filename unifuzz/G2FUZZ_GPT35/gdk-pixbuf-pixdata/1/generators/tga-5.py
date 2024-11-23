import struct
import os

def write_tga_file(file_path, width, height, data):
    header = bytearray([0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, (width % 256), (width // 256), (height % 256), (height // 256), 24, 32])
    
    with open(file_path, 'wb') as file:
        file.write(header)
        
        for y in range(height):
            row = bytearray()
            count = 1
            prev_color = data[y * width]
            
            for x in range(1, width):
                color = data[y * width + x]
                if color == prev_color and count < 127:
                    count += 1
                else:
                    if count > 1:
                        row.extend([128 + count, prev_color[2], prev_color[1], prev_color[0]])
                    else:
                        row.extend([count, prev_color[2], prev_color[1], prev_color[0]])  # Fixed the missing closing square bracket ']'
                    count = 1
                    prev_color = color
            
            if count > 1:
                row.extend([128 + count, prev_color[2], prev_color[1], prev_color[0]])
            else:
                row.extend([count, prev_color[2], prev_color[1], prev_color[0]])  # Fixed the missing closing square bracket ']'
                
            file.write(row)

# Generate example data (RGB pixels)
width = 100
height = 100
data = [(255, 0, 0) for _ in range(width * height)]  # Red pixels

# Create directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Write TGA file
file_path = os.path.join(directory, 'compressed_image.tga')
write_tga_file(file_path, width, height, data)