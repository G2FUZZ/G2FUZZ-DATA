import os

class JPGFileGenerator:
    def __init__(self, file_path, metadata, image_data, width, height, color_depth, thumbnail_data):
        self.file_path = file_path
        self.metadata = metadata
        self.image_data = image_data
        self.width = width
        self.height = height
        self.color_depth = color_depth
        self.thumbnail_data = thumbnail_data

    def generate_file(self):
        with open(self.file_path, 'wb') as file:
            file.write(self.image_data)
            file.write(b'\n\nMetadata:\n')
            for key, value in self.metadata.items():
                file.write(f'{key}: {value}\n'.encode())
            file.write(f'Image Dimensions: {self.width}x{self.height}\n'.encode())
            file.write(f'Color Depth: {self.color_depth} bits\n'.encode())
            file.write(b'\nThumbnail Preview:\n')
            file.write(self.thumbnail_data)

        print(f'Generated JPG file with metadata and additional features: {self.file_path}')


# Sample data for extended JPG file generation
file_path = './tmp/extended_sample.jpg'
metadata = {
    'Camera Model': 'Nikon D850',
    'Exposure Time': '1/100 sec',
    'Aperture': 'f/4.5',
    'ISO': 400
}
image_data = b'Extended JPG file content'
width = 1920
height = 1080
color_depth = 24
thumbnail_data = b'Thumbnail data goes here'

# Create an instance of JPGFileGenerator and generate the extended JPG file
jpg_generator = JPGFileGenerator(file_path, metadata, image_data, width, height, color_depth, thumbnail_data)
jpg_generator.generate_file()