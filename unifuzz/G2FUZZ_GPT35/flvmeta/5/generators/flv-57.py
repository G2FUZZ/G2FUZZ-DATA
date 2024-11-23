import os

class FLVFileGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.audio_tracks = []
        self.video_tracks = []
        self.metadata = {}

    def add_audio_track(self, codec, data):
        self.audio_tracks.append((codec, data))

    def add_video_track(self, codec, data):
        self.video_tracks.append((codec, data))

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def generate_flv_file(self):
        with open(self.filename, 'wb') as file:
            # Write metadata
            file.write(b'FLVM')  # FLV signature
            # Write metadata tags
            for key, value in self.metadata.items():
                tag = f'<{key}>{value}</{key}>'.encode()
                file.write(tag)

            # Write audio tracks
            for codec, data in self.audio_tracks:
                audio_tag = f'<audio>{codec}</audio>'.encode() + data
                file.write(audio_tag)

            # Write video tracks
            for codec, data in self.video_tracks:
                video_tag = f'<video>{codec}</video>'.encode() + data
                file.write(video_tag)

            # Write end of file tag
            file.write(b'<EOF>')

# Create a FLV file with multiple audio and video tracks, and metadata
flv_generator = FLVFileGenerator('./tmp/complex_file.flv')
flv_generator.add_metadata('title', 'Complex FLV File')
flv_generator.add_audio_track('MP3', b'MP3 audio data track 1')
flv_generator.add_audio_track('AAC', b'AAC audio data track 2')
flv_generator.add_video_track('H.264', b'H.264 video data track')
flv_generator.generate_flv_file()