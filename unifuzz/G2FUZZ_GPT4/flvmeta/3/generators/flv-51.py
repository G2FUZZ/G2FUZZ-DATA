import os
import struct

def create_flv_header():
    return bytes([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # TypeFlags (audio + video)
        0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
        0x00, 0x00, 0x00, 0x00  # PreviousTagSize0 (Placeholder)
    ])

def create_video_tag(timestamp, data_size, codec_id=0x04, frame_type=0x01):
    # Frame type (1 = key frame, 2 = inter frame) | Codec ID
    frametype_codec = (frame_type << 4) | codec_id
    return bytes([
        0x09,  # Tag type video
    ]) + struct.pack('>I', data_size)[1:] + struct.pack('>I', timestamp)[:3] + b'\x00' + bytes([
        0x00, 0x00, 0x00,  # StreamID
        frametype_codec,  # FrameType and CodecID
        # Video data would follow here; using a placeholder for demonstration
    ]) + b'\x00'*data_size

def create_audio_tag(timestamp, data_size):
    return bytes([
        0x08,  # Tag type audio
    ]) + struct.pack('>I', data_size)[1:] + struct.pack('>I', timestamp)[:3] + b'\x00' + bytes([
        0x00, 0x00, 0x00,  # StreamID
        # Audio data would follow here; using a placeholder for demonstration
    ]) + b'\x00'*data_size

def write_flv_file(output_path, video_frames, audio_frames):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(create_flv_header())
        previous_tag_size = 0
        for timestamp, data_size in video_frames:
            tag = create_video_tag(timestamp, data_size)
            f.write(tag)
            previous_tag_size = len(tag)
            f.write(struct.pack('>I', previous_tag_size))
        for timestamp, data_size in audio_frames:
            tag = create_audio_tag(timestamp, data_size)
            f.write(tag)
            previous_tag_size = len(tag)
            f.write(struct.pack('>I', previous_tag_size))

output_dir = "./tmp/"
output_path = os.path.join(output_dir, "complex_example.flv")

# Example data: list of tuples (timestamp in milliseconds, data size)
video_frames = [(0, 100), (1000, 150), (2000, 100)]
audio_frames = [(500, 50), (1500, 50)]

write_flv_file(output_path, video_frames, audio_frames)

print(f"Generated complex FLV file at: {output_path}")