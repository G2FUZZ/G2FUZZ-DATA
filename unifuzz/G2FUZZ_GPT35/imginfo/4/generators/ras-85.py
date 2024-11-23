import os

# Create a directory for storing the ras files
os.makedirs('./tmp/', exist_ok=True)

class RASFile:
    def __init__(self, filename, header_info, metadata, pixel_data):
        self.filename = filename
        self.header_info = header_info
        self.metadata = metadata
        self.pixel_data = pixel_data

    def create_file(self):
        with open(self.filename, 'w') as file:
            file.write(self.header_info)
            file.write("\nMetadata:\n")
            for key, value in self.metadata.items():
                file.write(f"{key}: {value}\n")
            file.write("\nPixel Data:\n")
            for row in self.pixel_data:
                file.write(' '.join(map(str, row)) + '\n')

# Generate ras files with complex structures
ras_files = [
    RASFile('./tmp/complex_file_1.ras',
            "Image dimensions: 1920x1080\nColor space: RGB\nOther parameters: None",
            {'Author': 'John Doe', 'Creation Date': '2022-10-15'},
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]]),
    
    RASFile('./tmp/complex_file_2.ras',
            "Image dimensions: 1280x720\nColor space: CMYK\nOther parameters: Compression: None",
            {'Author': 'Jane Smith', 'Creation Date': '2022-10-16'},
            [[128, 0, 0, 128], [0, 128, 0, 128], [0, 0, 128, 128]])
]

for ras_file in ras_files:
    ras_file.create_file()

print("Complex RAS files generated successfully.")