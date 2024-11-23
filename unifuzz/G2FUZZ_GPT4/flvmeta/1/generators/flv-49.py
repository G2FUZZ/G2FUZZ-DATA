import os
import random
import struct

def create_complex_flv_file(output_path, num_video_frames=30, num_audio_frames=60):
    # FLV file header for a video file with audio and video support
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    # PreviousTagSize0 always follows the FLV header, which is 0 for the first tag
    previous_tag_size0 = bytearray([0x00, 0x00, 0x00, 0x00])

    # Preparing the file content with the FLV header and the first PreviousTagSize0
    flv_content = flv_header + previous_tag_size0

    # Placeholder for the metadata tag, updated later with the correct duration
    metadata_tag_placeholder = create_metadata_tag({
        "duration": 0,  # Updated later
        "width": 1280,
        "height": 720,
        "videocodecid": 7,  # AVC
        "audiocodecid": 10  # AAC
    })
    flv_content += metadata_tag_placeholder

    # Placeholder for the size of the metadata tag, to calculate the correct PreviousTagSize
    previous_tag_size = calculate_previous_tag_size(metadata_tag_placeholder)
    flv_content += previous_tag_size

    video_frame_interval = 2  # Assuming 30fps video and 15fps for this example
    audio_frame_interval = 1  # Assuming audio frames are sent more frequently

    # Generate video and audio frames
    for i in range(1, max(num_video_frames, num_audio_frames) + 1):
        if i <= num_video_frames and i % video_frame_interval == 0:
            video_frame = create_video_frame(i)
            flv_content += video_frame + calculate_previous_tag_size(video_frame)
        if i <= num_audio_frames and i % audio_frame_interval == 0:
            audio_frame = create_audio_frame()
            flv_content += audio_frame + calculate_previous_tag_size(audio_frame)

    # Calculate video duration based on frame count and frame rate
    # Assuming a constant frame rate of 15fps for the sake of simplicity
    duration = num_video_frames / 15.0

    # Update the metadata tag with the correct duration
    metadata_tag_updated = create_metadata_tag({
        "duration": duration,
        "width": 1280,
        "height": 720,
        "videocodecid": 7,
        "audiocodecid": 10
    })

    # Update the FLV content with the correct metadata
    flv_content = (flv_header + previous_tag_size0 +
                   metadata_tag_updated +
                   calculate_previous_tag_size(metadata_tag_placeholder) +
                   flv_content[len(metadata_tag_placeholder) + len(previous_tag_size) + len(previous_tag_size0) + len(flv_header):])

    # Write the bytes to an FLV file
    with open(output_path, 'wb') as flv_file:
        flv_file.write(flv_content)

def create_metadata_tag(metadata):
    # Construct the onMetaData tag with AMF0 encoded data
    # For simplicity, metadata is not fully encoded. In a real scenario, use an AMF0 library.
    # This is a simplified example and does not fully adhere to AMF0 encoding standards.
    # A real implementation should properly encode the data.
    metadata_str = f"duration={metadata['duration']}\0width={metadata['width']}\0height={metadata['height']}\0videocodecid={metadata['videocodecid']}\0audiocodecid={metadata['audiocodecid']}\0"
    data_length = len(metadata_str)
    tag_type = 0x12  # script data
    timestamp = 0
    stream_id = 0
    data_length_bytes = struct.pack('>I', data_length)[1:]  # 24-bit
    timestamp_bytes = struct.pack('>I', timestamp)[1:] + (timestamp >> 24).to_bytes(1, 'big')  # 24-bit + 8-bit extended
    stream_id_bytes = struct.pack('>I', stream_id)[1:]  # 24-bit
    return bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id_bytes + metadata_str.encode('utf-8')

def calculate_previous_tag_size(tag):
    # Calculate and return the PreviousTagSize for a given tag
    return len(tag).to_bytes(4, 'big')

def create_video_frame(frame_number):
    # Simulate generating a video frame (keyframe or interframe)
    # This is a placeholder. In a real implementation, actual H.264 NAL units should be used.
    tag_type = 0x09  # video data
    frame_type = 0x10 if frame_number == 1 else 0x20  # keyframe for the first frame, interframe for others
    codec_id = 0x07  # AVC
    frame_data = b'SomeVideoData'  # Placeholder
    data_length = len(frame_data)
    timestamp = frame_number * 67  # Assuming 15fps
    stream_id = 0
    data_length_bytes = struct.pack('>I', data_length)[1:]
    timestamp_bytes = struct.pack('>I', timestamp)[1:] + (timestamp >> 24).to_bytes(1, 'big')
    stream_id_bytes = struct.pack('>I', stream_id)[1:]
    return bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id_bytes + bytearray([frame_type | codec_id]) + frame_data

def create_audio_frame():
    # Simulate generating an audio frame
    tag_type = 0x08  # audio data
    sound_format = 0xA0  # AAC
    frame_data = b'SomeAudioData'  # Placeholder
    data_length = len(frame_data)
    timestamp = 0  # Not varying in this simple example
    stream_id = 0
    data_length_bytes = struct.pack('>I', data_length)[1:]
    timestamp_bytes = struct.pack('>I', timestamp)[1:] + (timestamp >> 24).to_bytes(1, 'big')
    stream_id_bytes = struct.pack('>I', stream_id)[1:]
    return bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id_bytes + bytearray([sound_format]) + frame_data

# Specify the output path for the FLV file
output_path = './tmp/complex_sample.flv'

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the complex FLV file
create_complex_flv_file(output_path)