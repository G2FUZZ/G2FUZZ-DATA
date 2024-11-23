# Extended code to generate a more complex FLV file with metadata and multiple data tags
import struct

# FLV header
flv_signature = b'FLV'
flv_version = b'\x01'
flv_flags = b'\x00'
flv_header_size = b'\x09\x00\x00\x00'

# FLV metadata
metadata_tag = b'\x12'  # Tag type for metadata
metadata_size = b'\x00\x00\x00\x2A'  # Size of the metadata (42 bytes)
# Example metadata content
metadata_content = b'\x02\x00\x0D\x6F\x6E\x4D\x65\x74\x61\x44\x61\x74\x61\x00\x40\x52\x00\x00\x00\x00\x00\x00\x00\x02\x00\x04\x64\x75\x72\x61\x00\x40\x4F\xF0\x00\x00\x00\x00\x00\x00\x09\x00\x0C\x77\x69\x64\x74\x68\x00\x40\x90\x00\x00\x00\x00\x00\x00\x09\x00\x0C\x68\x65\x69\x67\x68\x74\x00\x40\x7F\x80\x00\x00\x00\x00\x00\x00\x09\x00\x0E\x76\x69\x64\x65\x6F\x64\x61\x74\x61\x72\x61\x74\x65\x00\x40\x72\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# FLV data tags
data_tag = b'\x08'  # Tag type for video data
data_size = b'\x00\x00\x00\x12'  # Size of the video data (18 bytes)
# Example video data content
video_data = b'\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

file_path = "./tmp/generated_file.flv"

with open(file_path, 'wb') as file:
    file.write(flv_signature)
    file.write(flv_version)
    file.write(flv_flags)
    file.write(flv_header_size)
    file.write(struct.pack('>I', len(metadata_tag)))
    file.write(metadata_tag)
    file.write(metadata_size)
    file.write(metadata_content)
    file.write(struct.pack('>I', len(data_tag)))
    file.write(data_tag)
    file.write(data_size)
    file.write(video_data)