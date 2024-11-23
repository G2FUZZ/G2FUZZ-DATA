import os

def generate_flv_file(file_path, metadata, video_frames, audio_packets, script_data):
    with open(file_path, 'wb') as f:
        # Write FLV header
        f.write(b'\x46\x4c\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Write metadata tag
        metadata_tag = b'\x12' + len(metadata).to_bytes(3, byteorder='big') + metadata
        f.write(metadata_tag)
        
        # Write video frames
        for frame in video_frames:
            f.write(b'\x09' + len(frame).to_bytes(3, byteorder='big') + frame)
        
        # Write audio packets
        for packet in audio_packets:
            f.write(b'\x08' + len(packet).to_bytes(3, byteorder='big') + packet)
        
        # Write script data tag
        script_data_tag = b'\x12' + len(script_data).to_bytes(3, byteorder='big') + script_data
        f.write(script_data_tag)

# Generate FLV files with more complex file structures
for i in range(1, 4):
    metadata = f'FLV Metadata for File {i}'.encode()
    video_frames = [f'Video Frame {j} for File {i}'.encode() for j in range(1, 6)]
    audio_packets = [f'Audio Packet {j} for File {i}'.encode() for j in range(1, 6)]
    script_data = f'Script Data for File {i}'.encode()
    
    generate_flv_file(f'./tmp/complex_file_{i}.flv', metadata, video_frames, audio_packets, script_data)