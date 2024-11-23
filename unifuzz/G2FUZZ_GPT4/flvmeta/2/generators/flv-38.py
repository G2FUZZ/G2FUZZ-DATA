import os
import struct

def create_complex_flv(output_path):
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # Type flags (audio and video tags present)
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    def create_metadata_tag(properties):
        """
        Create a script data tag for FLV metadata.
        """
        script_tag = bytearray([0x12])  # Tag type 18 for script data
        metadata = ''.join([f"{k}={v}\x00" for k, v in properties.items()]) + "\x09"
        script_data = bytearray([0x02]) + metadata.encode('utf-8')
        data_length = len(script_data)
        data_length_bytes = struct.pack('>I', data_length)[-3:]
        timestamp = bytearray([0x00, 0x00, 0x00])  # Always 0 for script tags
        stream_id = bytearray([0x00, 0x00, 0x00])  # Always 0
        return script_tag + data_length_bytes + timestamp + stream_id + script_data

    def create_video_tag(frame_data, timestamp):
        """
        Create a video tag.
        """
        tag_type = bytearray([0x09])  # Tag type 9 for video
        frame_tag = tag_type + _tag_body(frame_data, timestamp)
        return frame_tag

    def create_audio_tag(audio_data, timestamp):
        """
        Create an audio tag.
        """
        tag_type = bytearray([0x08])  # Tag type 8 for audio
        audio_tag = tag_type + _tag_body(audio_data, timestamp)
        return audio_tag

    def _tag_body(data, timestamp):
        """
        Helper function to construct the body of a tag.
        """
        data_length = len(data)
        data_length_bytes = struct.pack('>I', data_length)[-3:]
        timestamp_bytes = struct.pack('>I', timestamp)[1:] + struct.pack('>I', timestamp)[:1]  # Extended timestamp
        stream_id = bytearray([0x00, 0x00, 0x00])  # Always 0
        return data_length_bytes + timestamp_bytes + stream_id + data

    def create_keyframe():
        """
        Define a simple video frame (keyframe).
        """
        return bytearray([0x17, 0x01, 0x00, 0x00, 0x00]) + b'KEYFRAME'

    def create_inter_frame():
        """
        Define a simple video inter frame.
        """
        return bytearray([0x27, 0x02, 0x00, 0x00, 0x00]) + b'INTERFRAME'

    def create_audio_frame():
        """
        Define a simple audio frame.
        """
        return bytearray([0xAF, 0x01]) + b'AUDIOFRAME'

    flv_body = bytearray()
    metadata_properties = {
        "duration": 100,
        "width": 320,
        "height": 240,
        "framerate": 24,
        "videocodecid": "avc1",
        "audiocodecid": "mp3"
    }
    flv_body += create_metadata_tag(metadata_properties)
    flv_body += create_video_tag(create_keyframe(), 0)
    for timestamp in range(1000, 5000, 1000):
        flv_body += create_video_tag(create_inter_frame(), timestamp)
        flv_body += create_audio_tag(create_audio_frame(), timestamp)

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    file_path = os.path.join(output_path, "complex_example.flv")
    with open(file_path, "wb") as flv_file:
        flv_file.write(flv_header)
        prev_tag_size = 0
        for i in range(0, len(flv_body), 11):
            data_length_buffer = b'\x00' + flv_body[i+1:i+4]
            tag_size = struct.unpack_from('>I', data_length_buffer)[0] + 11
            flv_file.write(struct.pack('>I', prev_tag_size))
            flv_file.write(flv_body[i:i+tag_size])
            prev_tag_size = tag_size
        flv_file.write(struct.pack('>I', prev_tag_size))
        # Write an EOF tag to properly signal completion
        eof_tag = struct.pack('>I', 0)  # EOF tag is a zero-size previous tag
        flv_file.write(eof_tag)

create_complex_flv('./tmp/')