import os

def create_tga_file(filename, width, height, color_depth):
    header = bytearray(18)
    
    # Set image type to uncompressed true-color image
    header[2] = 2
    header[12:14] = width.to_bytes(2, byteorder='little')
    header[14:16] = height.to_bytes(2, byteorder='little')
    header[16] = color_depth
    header[17] = 0
    
    data = bytearray()
    if color_depth == 8:  # Grayscale
        for y in range(height):
            for x in range(width):
                data.append(x % 256)
    elif color_depth == 16:  # 5 bits for blue, 5 bits for green, 5 bits for red, 1 bit for unused
        for y in range(height):
            for x in range(width):
                data.extend(((x % 32) << 10 | (y % 32) << 5 | (x % 32)).to_bytes(2, byteorder='little'))
    elif color_depth == 24:  # Truecolor
        for y in range(height):
            for x in range(width):
                data.extend([x % 256, y % 256, (x+y) % 256])
    elif color_depth == 32:  # Truecolor with alpha
        for y in range(height):
            for x in range(width):
                data.extend([x % 256, y % 256, (x+y) % 256, (x*y) % 256])
    
    with open(filename, 'wb') as file:
        file.write(header + data)

def main():
    os.makedirs('./tmp/', exist_ok=True)
    widths, heights = 100, 100  # Example dimensions
    
    for depth in [8, 16, 24, 32]:
        filename = f'./tmp/example_{depth}bit.tga'
        create_tga_file(filename, widths, heights, depth)
        print(f"File {filename} created.")

if __name__ == "__main__":
    main()