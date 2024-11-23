import os
import struct

def write_flv_header(file):
    file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')

def write_previous_tag_size(file, size):
    file.write(struct.pack('>I', size))

def write_video_tag(file, data, timestamp):
    tag_size = len(data) + 11
    file.write(b'\x09')  # Tag type (Video)
    file.write(struct.pack('>I', len(data)))  # Data Size
    file.write(struct.pack('>I', timestamp))  # Timestamp
    file.write(b'\x00\x00\x00')  # Timestamp Extended
    file.write(struct.pack('>I', tag_size))  # Tag Size
    file.write(data)

def write_audio_tag(file, data, timestamp):
    tag_size = len(data) + 11
    file.write(b'\x08')  # Tag type (Audio)
    file.write(struct.pack('>I', len(data)))  # Data Size
    file.write(struct.pack('>I', timestamp))  # Timestamp
    file.write(b'\x00\x00\x00')  # Timestamp Extended
    file.write(struct.pack('>I', tag_size))  # Tag Size
    file.write(data)

def write_metadata_tag(file, data, timestamp):
    tag_size = len(data) + 11
    file.write(b'\x12')  # Tag type (Metadata)
    file.write(struct.pack('>I', len(data)))  # Data Size
    file.write(struct.pack('>I', timestamp))  # Timestamp
    file.write(b'\x00\x00\x00')  # Timestamp Extended
    file.write(struct.pack('>I', tag_size))  # Tag Size
    file.write(data)

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple video, audio, and metadata tags
with open('./tmp/extended_flv_file.flv', 'wb') as f:
    write_flv_header(f)

    video_data = b'\x00\x00\x00\x01VIDEOFRAME1'  # Example video data
    audio_data = b'\x00\x00\x00\x01AUDIOFRAME1'  # Example audio data
    metadata = b'\x00\x00\x00\x01METADATA'  # Example metadata

    for i in range(5):
        write_video_tag(f, video_data * (i+1), i*1000)
        write_previous_tag_size(f, len(video_data) * (i+1) + 11)

        write_audio_tag(f, audio_data * (i+1), i*1000)
        write_previous_tag_size(f, len(audio_data) * (i+1) + 11)

        write_metadata_tag(f, metadata * (i+1), i*1000)
        write_previous_tag_size(f, len(metadata) * (i+1) + 11)

print("FLV file with multiple video, audio, and metadata tags generated successfully.")