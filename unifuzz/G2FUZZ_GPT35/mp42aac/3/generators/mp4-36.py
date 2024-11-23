import os

class MP4File:
    def __init__(self, file_name, duration, resolution, audio_channels, video_codec, frame_rate, subtitles):
        self.file_name = file_name
        self.duration = duration
        self.resolution = resolution
        self.audio_channels = audio_channels
        self.video_codec = video_codec
        self.frame_rate = frame_rate
        self.subtitles = subtitles

    def generate_file(self):
        file_path = os.path.join('./tmp/', self.file_name + '.mp4')
        video_data = f'Sample MP4 file: Duration - {self.duration}, Resolution - {self.resolution}, Audio Channels - {self.audio_channels}, Video Codec - {self.video_codec}, Frame Rate - {self.frame_rate}, Subtitles - {self.subtitles}'

        with open(file_path, 'wb') as f:
            f.write(video_data.encode())

        print(f"MP4 file '{self.file_name}' generated with Duration: {self.duration}, Resolution: {self.resolution}, Audio Channels: {self.audio_channels}, Video Codec: {self.video_codec}, Frame Rate: {self.frame_rate}, Subtitles: {self.subtitles} at {file_path}")

# Generate a sample MP4 file with extended features
file3 = MP4File('complex_video', '15 mins', '4K', 'Surround Sound', 'H.264', '30 fps', 'English Subtitles')
file3.generate_file()