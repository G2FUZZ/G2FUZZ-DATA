import os
import struct
import random
from cryptography.fernet import Fernet

def write_flv_header(f):
    # FLV file header format:
    # Signature: 3 bytes ('FLV')
    # Version: 1 byte
    # Flags: 1 byte (audio and video tags present)
    # Header length: 4 bytes
    f.write(b'FLV\x01\x05\x00\x00\x00\x09')

def write_script_tag(f, data):
    # Data should be a serialized string representing metadata or other information
    # Script tag format can be complex, depending on how you serialize the data.
    # Here, we'll keep it simple and just write the length and the data as is.
    tag_header = b'\x12'  # Script data tag type
    data_length = struct.pack('>I', len(data))[:3]  # 24-bit data length
    timestamp = b'\x00\x00\x00'  # 3 bytes of timestamp + 1 byte of extended timestamp
    stream_id = b'\x00\x00\x00'  # Stream ID is always 0
    f.write(tag_header + data_length + timestamp + stream_id + data)
    # Write previous tag size (data length + tag header length (11 bytes))
    f.write(struct.pack('>I', len(data) + 11))

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

def create_complex_flv(output_path, video_tracks, audio_tracks, metadata, encryption_keys):
    print("Initializing FLV file with more complex structures including audio and encrypted tags.")

    # Step 1: Create a new FLV file and write the header
    with open(output_path, 'wb') as f:
        write_flv_header(f)

        # Step 2: Encode and write custom metadata as a script tag
        # For simplicity, metadata is just converted to a string and written as is.
        # In a real application, this would be serialized in AMF format.
        metadata_str = str(metadata).encode()
        write_script_tag(f, metadata_str)

        # Step 3: Add video and audio tracks
        for track in video_tracks:
            print(f"Encoding and adding video track {track['id']} with bitrate {track['bitrate']} kbps.")
            # Dummy video data for example purposes
            video_data = f"Video track {track['id']} data...".encode()
            if track['id'] in encryption_keys:
                video_data = encrypt_data(video_data, encryption_keys[track['id']])
            write_script_tag(f, video_data)

        for track in audio_tracks:
            print(f"Encoding and adding audio track {track['id']} with bitrate {track['bitrate']} kbps.")
            # Dummy audio data for example purposes
            audio_data = f"Audio track {track['id']} data...".encode()
            if track['id'] in encryption_keys:
                audio_data = encrypt_data(audio_data, encryption_keys[track['id']])
            write_script_tag(f, audio_data)

        print(f"FLV file created and saved to {output_path}")

# Example usage
output_path = './tmp/complex_example_with_audio.flv'
video_tracks = [
    {"id": 1, "bitrate": 500, "resolution": "480p"},
    {"id": 2, "bitrate": 1000, "resolution": "720p"},
    {"id": 3, "bitrate": 1500, "resolution": "1080p"}
]
audio_tracks = [
    {"id": 1, "bitrate": 128, "sample_rate": "44.1kHz"},
    {"id": 2, "bitrate": 256, "sample_rate": "48kHz"}
]
metadata = {
    "creation_date": "2023-10-05",
    "encoder": "AdvancedFLVEncoder v2.0",
    "description": "Sample FLV file with complex structures and audio support for testing."
}
encryption_keys = {
    1: Fernet.generate_key(),  # Each track could have its own encryption key
    2: Fernet.generate_key()
}

# Ensure the ./tmp/ directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Create a complex FLV file with the above specifications
create_complex_flv(output_path, video_tracks, audio_tracks, metadata, encryption_keys)