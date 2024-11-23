import eyed3
import os
import random

# Function to generate random audio data for multiple tracks
def generate_audio_data(track_name):
    audio_data = b"Random audio data for track: " + track_name.encode()
    return audio_data

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple audio tracks
num_tracks = 3
audio_tracks = {}
for i in range(1, num_tracks+1):
    track_name = f'Track_{i}'
    audio_tracks[track_name] = generate_audio_data(track_name)

# Create a new mp3 file with custom frames and multiple audio tracks
mp3_filename = './tmp/generated_complex_features.mp3'
with open(mp3_filename, 'wb') as f:
    for track_name, audio_data in audio_tracks.items():
        f.write(audio_data)

# Load the created mp3 file with custom frames and multiple audio tracks
audio_file = eyed3.load(mp3_filename)

# Check if the audio_file is loaded successfully
if audio_file is not None:
    audio_file.initTag()

    # Set ID3 tags
    audio_file.tag.artist = 'Generated Artist'
    audio_file.tag.album = 'Generated Album'
    audio_file.tag.title = 'Generated Album with Multiple Tracks'

    # Set custom frame for additional information
    custom_frame_id = 'X-ABC123'
    custom_frame_data = b"Custom data for advanced features."
    audio_file.tag.frame_set[custom_frame_id] = eyed3.id3.frames.RawFrame(custom_frame_id, custom_frame_data)

    # Set multiple audio tracks
    for track_name, audio_data in audio_tracks.items():
        audio_file.tag.frame_set[f'TIT2:{track_name}'] = eyed3.id3.frames.TextFrame('TIT2', track_name)
        audio_file.tag.frame_set[f'TRCK:{track_name}'] = eyed3.id3.frames.NumericTextFrame('TRCK', f'{random.randint(1, 10)}/{num_tracks}')
    
    # Save the changes
    audio_file.tag.save()
else:
    print("Error: Failed to load the audio file.")