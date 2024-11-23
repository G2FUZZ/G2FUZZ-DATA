import os

# Create a directory for storing the ras files
os.makedirs('./tmp/', exist_ok=True)

class RASFile:
    def __init__(self, filename, header_info, metadata, pixel_data, additional_layers=None, timestamp=None):
        self.filename = filename
        self.header_info = header_info
        self.metadata = metadata
        self.pixel_data = pixel_data
        self.additional_layers = additional_layers
        self.timestamp = timestamp

    def create_file(self):
        with open(self.filename, 'w') as file:
            file.write(self.header_info)
            file.write("\nMetadata:\n")
            for key, value in self.metadata.items():
                file.write(f"{key}: {value}\n")
            if self.additional_layers:
                file.write("\nAdditional Layers:\n")
                for layer_name, layer_data in self.additional_layers.items():
                    file.write(f"{layer_name}:\n")
                    for row in layer_data:
                        file.write(' '.join(map(str, row)) + '\n')
            file.write("\nPixel Data:\n")
            for row in self.pixel_data:
                file.write(' '.join(map(str, row)) + '\n')
            if self.timestamp:
                file.write(f"\nTimestamp: {self.timestamp}\n")

# Generate ras files with more complex structures
complex_ras_file = RASFile('./tmp/complex_file_3.ras',
                            "Image dimensions: 2560x1440\nColor space: RGBA\nOther parameters: Compression: Lossless",
                            {'Author': 'Alice Johnson', 'Creation Date': '2022-10-17'},
                            [[255, 0, 0, 128], [0, 255, 0, 128], [0, 0, 255, 128]],
                            additional_layers={'Layer 1': [[128, 128, 0, 128], [128, 0, 128, 128], [0, 128, 128, 128]],
                                               'Layer 2': [[64, 64, 64, 128], [192, 192, 192, 128], [0, 0, 0, 128]]},
                            timestamp='2022-10-18')

complex_ras_file.create_file()

print("Complex RAS file with additional layers and timestamp generated successfully.")