import os
import struct

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with audio and video data, metadata, and timestamps
def generate_extended_flv_file(file_path):
    # Simulating audio and video data for demonstration purposes
    audio_data = b'Audio data...'
    video_data = b'Video data...'
    
    with open(file_path, 'wb') as file:
        # FLV file header
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # FLV body with metadata, audio, and video data
        metadata = b'\x12\x00\x00\x00\x00\x00\x00\x02\x00\x0fOnMetaData\x08\x00\x00\x00\x02duration\x00@$\x00\x00\x00\x00\x00\x00\x03width\x00\x80\x00\x00\x00\x00\x00\x00\x04height\x00@\x00\x00\x00\x00\x00\x00\x00\x05videodatarate\x40\x1c\x00\x00\x00\x00\x00\x00\x06framerate@\x00\x00\x00\x00\x00\x00\x00\x07videocodecid\x00\x00\x00\x00\x00\x00\x00\x00\taudiodatarate`\x1f\x00\x00\x00\x00\x00\x00\naudiosamplerate@\x80\x00\x00\x00\x00\x00\x00\x0baudiosamplesize@\x00\x00\x00\x00\x00\x00\x00\x0cstereo@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09'
        file.write(metadata)
        
        timestamp = 0
        
        for i in range(5):  # Simulating multiple frames of audio and video data
            # Video tag
            file.write(b'\x09\x00\x00\x00\x02\x00\x00\x00\x00')
            file.write(struct.pack('>I', timestamp))
            file.write(struct.pack('>I', 0))
            file.write(struct.pack('>I', len(video_data)))
            file.write(video_data)
            
            timestamp += 40  # Increment timestamp for video frames
            
            # Audio tag
            file.write(b'\x08\x00\x00\x00\x02\x00\x00\x00\x00')
            file.write(struct.pack('>I', timestamp))
            file.write(struct.pack('>I', 0))
            file.write(struct.pack('>I', len(audio_data)))
            file.write(audio_data)
            
            timestamp += 20  # Increment timestamp for audio frames
    
    print('Extended FLV file with metadata, audio, and video data generated successfully.')

# Generate an extended FLV file with metadata, audio, and video data
generate_extended_flv_file('./tmp/extended.flv')