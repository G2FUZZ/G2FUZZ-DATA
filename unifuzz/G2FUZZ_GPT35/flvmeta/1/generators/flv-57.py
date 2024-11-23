import os

def create_tag(tag_type, data):
    tag = tag_type + len(data).to_bytes(3, byteorder='big') + b'\x00\x00\x00\x00' + data
    return tag

def generate_flv_file(filename, metadata, video_tracks, audio_tracks, subtitles, cue_points):
    header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    previous_tag_size = b'\x00\x00\x00\x00'
    
    with open(filename, 'wb') as file:
        file.write(header)
        
        # Write metadata tag
        metadata_tag = create_tag(b'\x12', metadata)
        file.write(metadata_tag)
        
        # Write video tracks tags
        for idx, video_track in enumerate(video_tracks):
            video_tag = create_tag(b'\x09', video_track)
            file.write(video_tag)
            if idx < len(video_tracks) - 1:
                file.write(previous_tag_size)
        
        # Write audio tracks tags
        for idx, audio_track in enumerate(audio_tracks):
            audio_tag = create_tag(b'\x08', audio_track)
            file.write(audio_tag)
            if idx < len(audio_tracks) - 1:
                file.write(previous_tag_size)
        
        # Write subtitles tag
        subtitles_tag = create_tag(b'\x02', subtitles)
        file.write(subtitles_tag)
        
        # Write cue points tags
        for cue_point in cue_points:
            cue_point_tag = create_tag(b'\x04', cue_point)
            file.write(cue_point_tag)
        
        file.write(previous_tag_size)

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with additional complex features
metadata = b'Metadata: { "title": "Sample Video", "author": "John Doe", "duration": "00:01:30" }'
video_tracks = [b'\x00\x00\x00\x00\x00', b'\x01\x01\x01\x01\x01']  # Example video tracks
audio_tracks = [b'\x01\x01\x01\x01\x01', b'\x02\x02\x02\x02\x02']  # Example audio tracks
subtitles = b'Subtitles: English, Spanish, French'  # Example subtitles
cue_points = [b'Cue Point 1', b'Cue Point 2', b'Cue Point 3']  # Example cue points

filename = './tmp/complex_video.flv'
generate_flv_file(filename, metadata, video_tracks, audio_tracks, subtitles, cue_points)

print('FLV file with additional complex features has been generated and saved as complex_video.flv in ./tmp/ directory.')