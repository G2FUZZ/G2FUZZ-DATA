import os

# Function to write audio data with a specific codec to the file
def write_audio_data(file, codec, data):
    file.write(f'{codec} compressed audio data: {data}\n'.encode())

# Function to write video data to the file
def write_video_data(file, data):
    file.write(f'Video data: {data}\n'.encode())

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a complex FLV file with multiple audio and video tracks
with open('./tmp/complex_file.flv', 'wb') as file:
    # Write metadata
    file.write(b'FLV File Metadata\n')

    # Write audio data with different codecs
    write_audio_data(file, 'MP3', 'audio_track1')
    write_audio_data(file, 'AAC', 'audio_track2')
    
    # Write video data
    write_video_data(file, 'video_track1')
    write_video_data(file, 'video_track2')