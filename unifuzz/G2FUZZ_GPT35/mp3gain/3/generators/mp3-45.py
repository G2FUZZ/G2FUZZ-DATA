import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate mp3 files with additional complex file features
def generate_mp3_file(file_path, metadata, audio_files):
    with open(file_path, 'w') as f:
        f.write("#EXTM3U\n")
        
        for idx, (audio_file, duration) in enumerate(zip(audio_files, [120, 180, 150]), start=1):
            f.write(f"#EXTINF:{duration},{metadata['artist']} - {metadata['title']} Part {idx}\n")
            f.write("#EXTREPLAYGAIN: -7.5 dB\n")
            f.write("#EXTDUALCHANNEL\n")
            
            # Write metadata tags
            for tag, value in metadata.items():
                f.write(f"#{tag.upper()}:{value}\n")
            
            f.write(f"path_to_audio_file_{idx}.mp3\n")

# Define metadata for the mp3 files
metadata = {
    'artist': 'Artist Name',
    'title': 'Track Title',
    'album': 'Album Name',
    'genre': 'Electronic',
    'year': '2022',
    'comment': 'This is a sample comment',
    'composer': 'Composer Name',
    'track_number': '01',
}

# Define multiple audio files to be included in the mp3
audio_files = ['audio_file_1.mp3', 'audio_file_2.mp3', 'audio_file_3.mp3']

# Generate mp3 files with additional complex file features
file_path = './tmp/extended_complex_generated_file.mp3'
generate_mp3_file(file_path, metadata, audio_files)

print(f"Generated mp3 file with extended complex file features: {file_path}")