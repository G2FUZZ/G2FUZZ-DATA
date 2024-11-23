import os
import random

class MP4File:
    def __init__(self, file_name, duration, resolution, audio_channels):
        self.file_name = file_name
        self.duration = duration
        self.resolution = resolution
        self.audio_channels = audio_channels

    def generate_file(self):
        file_path = os.path.join('./tmp/', self.file_name + '.mp4')
        video_data = f'Sample MP4 file: Duration - {self.duration}, Resolution - {self.resolution}, Audio Channels - {self.audio_channels}'

        with open(file_path, 'wb') as f:
            f.write(video_data.encode())

        print(f"MP4 file '{self.file_name}' generated with Duration: {self.duration}, Resolution: {self.resolution}, Audio Channels: {self.audio_channels} at {file_path}")

# Generate a sample MP4 file with extended features
file1 = MP4File('extended_features_video', '10 mins', '1080p', 'Stereo')
file1.generate_file()

file2 = MP4File('another_video', '5 mins', '720p', '5.1 Surround Sound')
file2.generate_file()