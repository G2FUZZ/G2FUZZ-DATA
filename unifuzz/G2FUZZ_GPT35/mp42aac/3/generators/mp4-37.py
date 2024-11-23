import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

class MP4File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tracks = []
        self.metadata = {}
        self.encrypted = False

    def add_track(self, track_data):
        self.tracks.append(track_data)

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def encrypt(self):
        self.encrypted = True

    def save(self):
        with open(self.file_path, 'wb') as file:
            file.write(b'MP4 file content')
            # Write tracks data
            for track_data in self.tracks:
                file.write(track_data)
            # Write metadata
            for key, value in self.metadata.items():
                file.write(f'{key}: {value}\n'.encode('utf-8'))
            # Write encryption info
            if self.encrypted:
                file.write(b'Encrypted: True\n')

# Create an instance of MP4File
file_path = './tmp/complex_video_file.mp4'
mp4_file = MP4File(file_path)

# Add tracks data
mp4_file.add_track(b'Track 1 data')
mp4_file.add_track(b'Track 2 data')

# Add metadata
mp4_file.add_metadata('Author', 'John Doe')
mp4_file.add_metadata('Creation Date', '2022-01-01')

# Encrypt the file
mp4_file.encrypt()

# Save the file
mp4_file.save()

print(f'Generated MP4 file with complex file structures: {file_path}')