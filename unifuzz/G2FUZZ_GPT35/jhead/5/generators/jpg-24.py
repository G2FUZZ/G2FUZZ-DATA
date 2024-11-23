import os

class ComplexJPGFileGenerator:
    def __init__(self, file_path, metadata, image_layers, width, height, color_depth, thumbnail_data, icc_profile):
        self.file_path = file_path
        self.metadata = metadata
        self.image_layers = image_layers
        self.width = width
        self.height = height
        self.color_depth = color_depth
        self.thumbnail_data = thumbnail_data
        self.icc_profile = icc_profile

    def generate_file(self):
        with open(self.file_path, 'wb') as file:
            for layer_name, layer_data in self.image_layers.items():
                file.write(layer_data)
                file.write(f'\n\nLayer: {layer_name}\n'.encode())
            file.write(b'\n\nMetadata:\n')
            for key, value in self.metadata.items():
                file.write(f'{key}: {value}\n'.encode())
            file.write(f'Image Dimensions: {self.width}x{self.height}\n'.encode())
            file.write(f'Color Depth: {self.color_depth} bits\n'.encode())
            file.write(b'\nThumbnail Preview:\n')
            file.write(self.thumbnail_data)
            file.write(b'\n\nICC Profile:\n')
            file.write(self.icc_profile)

        print(f'Generated complex JPG file with metadata, multiple image layers, and embedded ICC profile: {self.file_path}')


# Sample data for complex JPG file generation
file_path = './tmp/complex_sample.jpg'
metadata = {
    'Camera Model': 'Canon EOS R5',
    'Exposure Time': '1/60 sec',
    'Aperture': 'f/2.8',
    'ISO': 800
}
image_layers = {
    'Layer 1': b'Layer 1 data',
    'Layer 2': b'Layer 2 data'
}
width = 2560
height = 1440
color_depth = 32
thumbnail_data = b'Complex Thumbnail data goes here'
icc_profile = b'Embedded ICC profile data'

# Create an instance of ComplexJPGFileGenerator and generate the complex JPG file
complex_jpg_generator = ComplexJPGFileGenerator(file_path, metadata, image_layers, width, height, color_depth, thumbnail_data, icc_profile)
complex_jpg_generator.generate_file()