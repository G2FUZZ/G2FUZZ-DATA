import os

class FLVFile:
    def __init__(self, filename):
        self.filename = filename
        self.audio_streams = []
        self.video_streams = []

    def add_audio_stream(self, codec, data):
        self.audio_streams.append({'codec': codec, 'data': data})

    def add_video_stream(self, codec, data):
        self.video_streams.append({'codec': codec, 'data': data})

    def save(self):
        with open(self.filename, 'wb') as file:
            # Write audio streams
            for stream in self.audio_streams:
                file.write(f'Audio Codec: {stream["codec"]}\n'.encode())
                file.write(stream['data'] + b'\n')

            # Write video streams
            for stream in self.video_streams:
                file.write(f'Video Codec: {stream["codec"]}\n'.encode())
                file.write(stream['data'] + b'\n')

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio and video streams
flv_file = FLVFile('./tmp/complex_features.flv')

# Add audio streams with different codecs
flv_file.add_audio_stream('MP3', b'MP3 audio data 1')
flv_file.add_audio_stream('AAC', b'AAC audio data 1')

# Add video streams with different codecs
flv_file.add_video_stream('H.264', b'H.264 video data 1')
flv_file.add_video_stream('VP9', b'VP9 video data 1')

# Save the FLV file with complex features
flv_file.save()