import os
import time

def create_complex_flv(output_path):
    # FLV file header for a video file with audio
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # Type flags: Audio + Video
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    # Initialize the FLV body with the first previous tag size
    flv_body = bytearray([0x00, 0x00, 0x00, 0x00])

    # Function to add a video tag to the FLV body
    def add_video_tag(body, timestamp, frame_type, codec_id=0x07):
        # Tag type 9 = video
        tag_type = 0x09
        # Frame type and codec ID (AVC for H.264 video)
        frame_type_and_codec = (frame_type << 4) | codec_id
        # Example data size and data (simplified for demonstration)
        data_size = 0x2A  # Simplified data size
        timestamp_bytes = timestamp.to_bytes(3, byteorder='big') + (timestamp // 16777216).to_bytes(1, byteorder='big')
        stream_id = b'\x00\x00\x00'  # StreamID always 0

        video_data = bytearray([frame_type_and_codec, 0x01])  # AVC NALU
        video_data.extend(b'\x00\x00\x00')  # Composition time

        if frame_type == 1:  # Keyframe
            video_data.extend(b'KEYFRAME')  # Simplified keyframe data
        else:
            video_data.extend(b'interframe')  # Simplified interframe data

        # Assemble the tag
        data_length_bytes = len(video_data).to_bytes(3, byteorder='big')
        tag_header = bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id
        tag_data = video_data

        # Append the tag to the body
        body.extend(tag_header)
        body.extend(tag_data)

        # Append the previous tag size (tag header + data)
        previous_tag_size = (len(tag_header) + len(tag_data)).to_bytes(4, byteorder='big')
        body.extend(previous_tag_size)

    # Function to add an audio tag to the FLV body
    def add_audio_tag(body, timestamp, is_aac_sequence_header=False):
        # Tag type 8 = audio
        tag_type = 0x08
        # Sound format 10 = AAC
        sound_format = 0xA
        sound_rate = 0x3  # 44 kHz
        sound_size = 0x1  # 16-bit samples
        sound_type = 0x1  # Stereo sound
        sound_params = (sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type

        audio_data = bytearray([sound_params])
        if is_aac_sequence_header:
            audio_data.append(0x00)  # AAC sequence header
            audio_data.extend(b'AAC')  # Simplified AAC config (sequence header)
        else:
            audio_data.append(0x01)  # AAC raw
            audio_data.extend(b'audioframe')  # Simplified audio frame data

        timestamp_bytes = timestamp.to_bytes(3, byteorder='big') + (timestamp // 16777216).to_bytes(1, byteorder='big')
        stream_id = b'\x00\x00\x00'
        data_length_bytes = len(audio_data).to_bytes(3, byteorder='big')
        tag_header = bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id
        tag_data = audio_data

        body.extend(tag_header)
        body.extend(tag_data)

        previous_tag_size = (len(tag_header) + len(tag_data)).to_bytes(4, byteorder='big')
        body.extend(previous_tag_size)

    # Add a sequence header for video and audio at the beginning
    add_video_tag(flv_body, 0, frame_type=1)  # AVC sequence header (simplified)
    add_audio_tag(flv_body, 0, is_aac_sequence_header=True)

    # Simulate 30fps video for 2 seconds (60 frames total) and audio tags
    for frame_number in range(60):
        timestamp = int((frame_number / 30) * 1000)  # Convert frame number to milliseconds
        frame_type = 1 if frame_number % 30 == 0 else 2  # Keyframe or interframe
        add_video_tag(flv_body, timestamp, frame_type)
        add_audio_tag(flv_body, timestamp)  # Adding audio tag with the same timestamp as video

    output_file = os.path.join(output_path, "complex_example.flv")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(output_file, "wb") as flv_file:
        flv_file.write(flv_header)
        flv_file.write(flv_body)

    print(f"FLV file created at {output_file}")

# Use the function to create a more complex FLV file
create_complex_flv('./tmp/')