import os

# Create a directory for storing the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

def generate_flv_file(file_name, metadata, audio_tracks, video_frames):
    with open(file_name, 'wb') as file:
        # Write FLV header
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Write metadata
        file.write(b'\x12\x00\x00\x00\x00')
        file.write(len(metadata).to_bytes(3, byteorder='big'))
        file.write(metadata.encode())
        
        # Write audio tags
        for audio_track in audio_tracks:
            file.write(b'\x08')
            file.write(len(audio_track).to_bytes(3, byteorder='big'))
            file.write(audio_track.encode())
            
        # Write video tags
        for frame in video_frames:
            file.write(b'\x09')
            file.write(len(frame).to_bytes(3, byteorder='big'))
            file.write(frame)
    
    print(f'FLV file "{file_name}" with complex file structure has been generated.')

# Generate a FLV file with complex file structure
file_name = './tmp/complex_video.flv'
metadata = 'Title: Complex Video | Author: John Doe'
audio_tracks = ['Audio Track 1', 'Audio Track 2']
video_frames = [b'Video Frame 1', b'Video Frame 2', b'Video Frame 3']

generate_flv_file(file_name, metadata, audio_tracks, video_frames)