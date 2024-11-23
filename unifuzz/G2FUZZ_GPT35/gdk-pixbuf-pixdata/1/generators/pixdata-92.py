import os

class PixdataFile:
    def __init__(self, filename, version='1.0', metadata=None, pixel_data=None):
        self.filename = filename
        self.version = version
        self.metadata = metadata if metadata else {}
        self.pixel_data = pixel_data if pixel_data else []

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def add_pixel_data(self, pixel_values):
        self.pixel_data.append(pixel_values)

    def save_file(self):
        file_header = f"""
        File Format: pixdata
        Version: {self.version}
        Metadata: {self.metadata}
        """

        with open(self.filename, 'w') as file:
            file.write(file_header)
            for pixel_values in self.pixel_data:
                file.write(','.join(map(str, pixel_values)) + '\n')

        print("Pixdata file generated and saved successfully.")

# Create an instance of PixdataFile and add metadata and pixel data
pixdata = PixdataFile('./tmp/extended_pixdata_file.txt')
pixdata.add_metadata('author', 'John Doe')
pixdata.add_metadata('created_date', '2022-01-01')
pixdata.add_pixel_data([255, 0, 0])
pixdata.add_pixel_data([0, 255, 0])
pixdata.add_pixel_data([0, 0, 255])

# Save the extended pixdata file
pixdata.save_file()