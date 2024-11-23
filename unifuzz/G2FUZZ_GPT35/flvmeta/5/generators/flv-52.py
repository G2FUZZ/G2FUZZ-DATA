import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with audio and video data packets, timestamps, and metadata
audio_data = b'\x12\x34\x56\x78'  # Example audio data
video_data = b'\x87\x65\x43\x21'  # Example video data
timestamp = 0  # Starting timestamp

with open('./tmp/complex_flv_file.flv', 'wb') as file:
    # Write FLV header
    file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # Write previous tag size
    file.write(b'\x00\x00\x00\x00')
    
    # Write audio data packet
    audio_tag = b'\x08\x00\x00\x00\x02' + timestamp.to_bytes(3, 'big') + len(audio_data).to_bytes(3, 'big') + b'\x00\x00\x00\x00' + audio_data
    file.write(audio_tag)
    
    # Update timestamp
    timestamp += 10
    
    # Write previous tag size
    file.write(len(audio_tag).to_bytes(4, 'big'))
    
    # Write video data packet
    video_tag = b'\x09\x00\x00\x00\x02' + timestamp.to_bytes(3, 'big') + len(video_data).to_bytes(3, 'big') + b'\x00\x00\x00\x00' + video_data
    file.write(video_tag)
    
    # Update timestamp
    timestamp += 10

print('Complex FLV file with audio, video data packets, timestamps, and metadata generated successfully.')