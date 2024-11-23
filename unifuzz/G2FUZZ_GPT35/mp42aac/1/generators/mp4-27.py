import os
import random
import string

class MP4FileGenerator:
    def __init__(self):
        self.file_path = './tmp/sample_complex_mp4.mp4'
        
    def generate_random_data(self, size):
        return bytes(''.join(random.choices(string.ascii_letters + string.digits, k=size)), 'utf-8')

    def add_metadata(self, data, metadata):
        return data + bytes(f'\nMetadata: {metadata}', 'utf-8')

    def encrypt_data(self, data):
        # Simulating encryption process
        encrypted_data = data[::-1]  # Reverse the data as a simple encryption demo
        return encrypted_data

    def generate_complex_mp4(self):
        sample_data = self.generate_random_data(1000)
        sample_data_with_metadata = self.add_metadata(sample_data, 'Sample metadata')
        encrypted_data = self.encrypt_data(sample_data_with_metadata)
        
        with open(self.file_path, 'wb') as file:
            file.write(encrypted_data)
        
        print(f"Generated complex MP4 file with metadata and encryption: {self.file_path}")

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample complex mp4 file with metadata and encryption
mp4_generator = MP4FileGenerator()
mp4_generator.generate_complex_mp4()