import os

# Function to generate TGA file with compression method
def generate_tga_with_compression(compression_method, output_filename):
    tga_header = bytearray([0] * 18)
    tga_header[2] = 10  # Image type (RLE compressed true-color image)
    
    with open(output_filename, 'wb') as f:
        f.write(tga_header)
        
        # Simulate image data (dummy data)
        image_data = bytearray([255, 0, 0, 255, 255, 255] * 50)
        
        if compression_method == 'RLE':
            compressed_data = bytearray()
            i = 0
            while i < len(image_data):
                if i+2 < len(image_data) and i+5 < len(image_data) and image_data[i] == image_data[i+3] == image_data[i+6]:
                    count = 0
                    while i+count+3 < len(image_data) and image_data[i+count] == image_data[i+count+3] and count < 127:
                        count += 3
                    compressed_data.append(count | 0b10000000)
                    compressed_data.extend(image_data[i:i+3])
                    i += count
                else:
                    count = 0
                    while i+count+2 < len(image_data) and count < 127:
                        count += 3
                    compressed_data.append(count - 1)
                    compressed_data.extend(image_data[i:i+count])
                    i += count
            f.write(compressed_data)
        else:
            f.write(image_data)

# Create a directory to save the TGA files
os.makedirs('./tmp/', exist_ok=True)

# Generate TGA files with compression methods
generate_tga_with_compression('RLE', './tmp/compressed_image.tga')
generate_tga_with_compression(None, './tmp/uncompressed_image.tga')