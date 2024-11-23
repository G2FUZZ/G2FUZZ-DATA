import os
import random
import struct
import json

def create_advanced_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Path to the FLV file to be created
    flv_file_path = './tmp/advanced_video.flv'

    # FLV file header for a video file with audio (TypeFlagsAudio is 1 and TypeFlagsVideo is 1)
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')

    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')

    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)

        # Add an onMetaData tag with detailed information
        metadata = {
            "duration": 0.0,  # Duration will be updated after generating video frames
            "width": 1280,
            "height": 720,
            "videodatarate": 0,
            "framerate": 24,
            "videocodecid": 7,  # AVC
            "audiodatarate": 0,
            "audiosamplerate": 44100,
            "audiosamplesize": 16,
            "stereo": True,
            "audiocodecid": 10,  # AAC
            "filesize": 0  # Filesize will be updated later
        }

        metadata_content = json.dumps(metadata)
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))

        # Simulate the addition of video frames with keyframe intervals
        keyframe_interval = 5
        for i in range(1, 61):  # Generate 60 frames for 2 seconds of video at 30 fps
            frame_data = os.urandom(4096)  # Randomly generated frame data
            frame_length = len(frame_data)
            timestamp = int((i / 30) * 1000)  # Convert frame count to milliseconds

            # Video tag: Frame Type(1 byte) + CodecID(1 byte) + Frame Data
            is_keyframe = i % keyframe_interval == 1
            frame_info = bytes([0x17 if is_keyframe else 0x27]) + bytes([0x01])  # Key frame or inter frame + AVC NALU
            video_data = frame_info + frame_data
            video_tag = bytes([9]) + frame_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(3, byteorder='big') + (0).to_bytes(1, byteorder='big') + (0).to_bytes(3, byteorder='big') + video_data
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))

        # Update the metadata with the correct duration and file size
        flv_file.seek(0, os.SEEK_END)
        file_size = flv_file.tell()
        metadata['filesize'] = file_size
        metadata['duration'] = 2.0  # Assuming 2 seconds for this example

        # Go back and rewrite the metadata with updated information
        flv_file.seek(len(flv_header) + len(previous_tag_size_0))
        metadata_content = json.dumps(metadata)
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)

        print(f"Advanced FLV file created at {flv_file_path}")

create_advanced_flv_file()