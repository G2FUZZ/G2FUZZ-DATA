import os
import struct
import random

def create_enhanced_flv(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Generate onMetaData script tag
    def generate_on_meta_data(width, height, duration, file_size):
        # Simplified serialization of properties
        metadata = b'\x02\x00\x0aonMetaData'  # Start of onMetaData tag
        metadata += b'\x08'  # ECMA array marker
        metadata += struct.pack('>L', 4)  # Number of elements in the array
        
        # Width property
        metadata += b'\x00\x05width\x00' + struct.pack('>d', width)
        # Height property
        metadata += b'\x00\x06height\x00' + struct.pack('>d', height)
        # Duration property
        metadata += b'\x00\x08duration\x00' + struct.pack('>d', duration)
        # FileSize property (in bytes)
        metadata += b'\x00\x08filesize\x00' + struct.pack('>d', file_size)
        
        metadata += b'\x00\x00\x09'  # End of object marker
        
        return metadata
    
    # Generate a video tag (simplified)
    def generate_video_tag(timestamp):
        # Placeholder data for a video frame
        video_data = b'\x17\x00\x00\x00\x00' + b'\x00' * 10  # Keyframe, AVC frame, composition time 0
        tag_header = b'\x09' + struct.pack('>L', len(video_data))[1:] + struct.pack('>L', timestamp)[:3] + b'\x00\x00\x00'
        return tag_header + video_data
    
    # Generate an audio tag (simplified)
    def generate_audio_tag(timestamp):
        # Placeholder data for an audio frame
        audio_data = b'\xaf\x01' + b'\x00' * 4  # AAC frame
        tag_header = b'\x08' + struct.pack('>L', len(audio_data))[1:] + struct.pack('>L', timestamp)[:3] + b'\x00\x00\x00'
        return tag_header + audio_data
    
    # Video and audio settings
    width = 1280
    height = 720
    duration = 10  # seconds
    video_frame_rate = 30  # frames per second
    audio_sample_rate = 44100  # samples per second (placeholder, not actually used in data generation)
    
    # Generate onMetaData script tag
    script_tag_data = generate_on_meta_data(width, height, duration, 0)  # File size updated later
    script_tag_start = b'\x12' + struct.pack('>L', len(script_tag_data))[1:] + b'\x00\x00\x00\x00\x00'
    script_tag = script_tag_start + script_tag_data
    
    # Prepare the output file path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file_path = os.path.join(output_path, 'enhanced_video_with_audio.flv')
    
    # Write the initial part of the FLV file
    with open(output_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag)
        previous_tag_size = struct.pack('>L', len(script_tag))
        f.write(previous_tag_size)
        
        # Generate and write tags for video and audio frames
        for i in range(duration * video_frame_rate):
            timestamp = int((i / video_frame_rate) * 1000)  # Convert to milliseconds
            
            # Write video tag
            video_tag = generate_video_tag(timestamp)
            f.write(video_tag)
            f.write(struct.pack('>L', len(video_tag)))
            
            # Write audio tag (simplified, assuming constant frame rate)
            if i % (video_frame_rate // 2) == 0:  # Roughly simulate lower frame rate for audio
                audio_tag = generate_audio_tag(timestamp)
                f.write(audio_tag)
                f.write(struct.pack('>L', len(audio_tag)))
    
    # Update the file size in the onMetaData tag
    file_size = os.path.getsize(output_file_path)
    updated_script_tag_data = generate_on_meta_data(width, height, duration, file_size)
    updated_script_tag = script_tag_start + updated_script_tag_data
    with open(output_file_path, 'r+b') as f:
        f.seek(len(flv_header) + len(previous_tag_size_0))  # Jump to the script tag position
        f.write(updated_script_tag)
    
    print('Enhanced FLV file with video and audio streams created.')

# Specify the output directory
output_dir = './tmp/'
create_enhanced_flv(output_dir)